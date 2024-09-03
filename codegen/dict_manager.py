from codegen.objects import Object, Position, Free, Type, Arg
from codegen.array_manager import DEFAULT_CAPACITY
from codegen.c_manager import CManager, c_dec


class DictManager:
    def __init__(self, codegen) -> None:
        self.defined_types: list[tuple[str, str]] = []
        
        self.codegen = codegen
    
    def has_type(self, key_type: str, value_type: str) -> bool:
        for k, v in self.defined_types:
            if k == key_type and v == value_type:
                return True
        
        return False
    
    def define_dict(self, key_type: Type, value_type: Type) -> Type:
        dict_type = Type(
            f'dict[{key_type}: {value_type}]',
            f'{key_type.c_type}_{value_type.c_type}_dict'
        )
        
        if self.has_type(key_type.type, value_type.type):
            return dict_type
        
        pair_type = Type(
            f'dict_pair[{key_type}, {value_type}]',
            f'{key_type.c_type}_{value_type.c_type}_pair'
        )
        
        self.codegen.add_toplevel_code(f"""typedef struct {{
    {key_type.c_type} key;
    {value_type.c_type} value;
}} {pair_type.c_type};

typedef struct {{
    {pair_type.c_type}* elements;
    size_t length;
    size_t capacity;
}} {dict_type.c_type};
""")
        
        c_manager: CManager = self.codegen.c_manager
        
        @c_dec(
            func_name_override=f'{pair_type.c_type}_type', add_to_class=c_manager,
            is_property=True
        )
        def pair_type_(_, call_position: Position) -> Object:
            return Object(f'"{pair_type}"', Type('string'), call_position)
        
        @c_dec(
            func_name_override=f'{pair_type.c_type}_to_string', add_to_class=c_manager,
            is_method=True
        )
        def pair_to_string(codegen, call_position: Position, pair_obj: Object) -> Object:
            code, buf_free = codegen.fmt_length(
                codegen, call_position,
                'dict_pair[key=%s, value=%s]',
                codegen.call(
                    f'{key_type.c_type}_to_string',
                    [Arg(Object(f'(({pair_obj.code}).key)', key_type, call_position))],
                    call_position
                ).code,
                codegen.call(
                    f'{value_type.c_type}_to_string',
                    [Arg(Object(f'(({pair_obj.code}).value)', value_type, call_position))],
                    call_position
                ).code
            )
            
            codegen.prepend_code(code)
            return Object(buf_free.object_name, Type('string'), call_position, free=buf_free)
        
        @c_dec(
            param_types=(pair_type.c_type,),
            func_name_override=f'{pair_type.c_type}_key', add_to_class=c_manager,
            is_property=True
        )
        def pair_key(_, call_position: Position, pair_obj: Object) -> Object:
            return Object(f'(({pair_obj.code}).key)', key_type, call_position)
        
        @c_dec(
            param_types=(pair_type.c_type,),
            func_name_override=f'{pair_type.c_type}_value', add_to_class=c_manager,
            is_property=True
        )
        def pair_value(_, call_position: Position, pair_obj: Object) -> Object:
            return Object(f'(({pair_obj.code}).value)', value_type, call_position)
        
        @c_dec(func_name_override=f'{dict_type.c_type}_make', add_to_class=c_manager)
        def dict_make(codegen, call_position: Position) -> Object:
            dict_free = Free()
            d = codegen.create_temp_var(dict_type, call_position, free=dict_free)
            dict_free.object_name = f'{d}.elements'
            
            codegen.prepend_code(f"""{dict_type.c_type} {d} = {{
    .length = 0, .capacity = {DEFAULT_CAPACITY},
    .elements = ({pair_type.c_type}*)malloc({DEFAULT_CAPACITY} * sizeof({pair_type.c_type}))
}};
{codegen.c_manager.buf_check(f'{d}.elements')}
""")
            
            return Object(d, dict_type, call_position, free=dict_free)
        
        @c_dec(
            param_types=(dict_type.c_type, key_type.c_type),
            func_name_override=f'{dict_type.c_type}_get', add_to_class=c_manager,
            is_method=True,
        )
        def dict_get(codegen, call_position: Position, dict_obj: Object, key: Object) -> Object:
            value = codegen.create_temp_var(value_type, call_position)
            d = f'({dict_obj.code})'
            i = codegen.create_temp_var(Type('int'), call_position)
            codegen.prepend_code(f"""{value_type.c_type} {value};
for (size_t {i} = 0; {i} < {d}.length; {i}++) {{
    if ({d}.elements[{i}].key == ({key.code})) {{
        {value} = {d}.elements[{i}].value;
        break;
    }}
}}
""")
            
            return Object(value, value_type, call_position)
        
        @c_dec(
            param_types=(dict_type.c_type, key_type.c_type),
            func_name_override=f'{dict_type.c_type}_has', add_to_class=c_manager,
            is_method=True,
        )
        def dict_has(codegen, call_position: Position, dict_obj: Object, key: Object) -> Object:
            d = f'({dict_obj.code})'
            i = codegen.create_temp_var(Type('int'), call_position)
            has = codegen.create_temp_var(Type('bool'), call_position)
            codegen.prepend_code(f"""bool {has} = false;
for (size_t {i} = 0; {i} < {d}.length; {i}++) {{
    if ({d}.elements[{i}].key == ({key.code})) {{
        {has} = true;
        break;
    }}
}}
""")
            return Object(has, Type('bool'), call_position)
        
        @c_dec(
            param_types=(dict_type.c_type, key_type.c_type, value_type.c_type),
            func_name_override=f'{dict_type.c_type}_set', add_to_class=c_manager,
            is_method=True,
        )
        def dict_set(codegen, call_position: Position,
                     dict_obj: Object, key: Object, value: Object) -> Object:
            i = codegen.create_temp_var(Type('int'), call_position)
            d = f'({dict_obj.code})'
            codegen.prepend_code(f"""if ({dict_has(codegen, call_position, dict_obj, key).code}) {{
    for (size_t {i} = 0; {i} < {d}.length; {i}++) {{
        if ({d}.elements[{i}].key == ({key.code})) {{
            {d}.elements[{i}].value = {value.code};
            break;
        }}
    }}
}} else {{
    if ({d}.length == {d}.capacity) {{
        {d}.capacity *= 2;
        {d}.elements = ({pair_type.c_type}*)realloc(
            {d}.elements,
            {d}.capacity * sizeof({pair_type.c_type})
        );
        
        {codegen.c_manager.buf_check(f'{d}.elements')}
    }}
    {d}.elements[{d}.length].key = {key.code};
    {d}.elements[{d}.length].value = {value.code};
    {d}.length++;
}}
""")
            return Object.NULL(call_position)
        
        @c_dec(
            param_types=(dict_type.c_type,),
            func_name_override=f'{dict_type.c_type}_to_string', add_to_class=c_manager,
            is_method=True
        )
        def dict_to_string(codegen, call_position: Position, dict_obj: Object) -> Object:
            buf_free = Free()
            buf = codegen.create_temp_var(Type('string'), call_position, free=buf_free)
            size = codegen.create_temp_var(Type('int', 'size_t'), call_position)
            i = codegen.create_temp_var(Type('int'), call_position)
            key_repr = codegen.create_temp_var(Type('string'), call_position)
            value_repr = codegen.create_temp_var(Type('string'), call_position)
            written = codegen.create_temp_var(Type('int', 'size_t'), call_position)
            remaining = codegen.create_temp_var(Type('int', 'size_t'), call_position)
            d = f'({dict_obj.code})'
            get_key = Arg(Object(f'{d}.elements[{i}].key', key_type, call_position))
            get_value = Arg(Object(f'{d}.elements[{i}].value', value_type, call_position))
            
            codegen.prepend_code(f"""
size_t {size} = 3;  // Start with 3 for '{{', '}}', and null terminator
for (size_t {i} = 0; {i} < {d}.length; {i}++) {{
""")
            codegen.prepend_code(f"""
    string {key_repr} = {codegen.call(f'{key_type}_to_string', [get_key], call_position).code};
    string {value_repr} = {codegen.call(f'{value_type}_to_string', [get_value], call_position).code};
    {size} += strlen({key_repr}) + strlen({value_repr}) + 4;  // 4 for '{{', ':', ' ', and '}}'
    if ({i} < {d}.length - 1) {size} += 2;  // For ", "
}}
string {buf} = (string)malloc({size});
{codegen.c_manager.buf_check(buf)}
size_t {remaining} = {size};
int {written} = snprintf({buf}, {remaining}, "{{");
{remaining} -= {written};

for (size_t {i} = 0; {i} < {d}.length; {i}++) {{
""")
            codegen.prepend_code(f"""
    string {key_repr} = {codegen.call(f'{key_type}_to_string', [get_key], call_position).code};
    string {value_repr} = {codegen.call(f'{value_type}_to_string', [get_value], call_position).code};
    {written} = snprintf({buf} + strlen({buf}), {remaining}, "{{%s: %s}}", {key_repr}, {value_repr});
    {remaining} -= {written};
    
    if ({i} < {d}.length - 1) {{
        {written} = snprintf({buf} + strlen({buf}), {remaining}, ", ");
        {remaining} -= {written};
    }}
}}
strncat({buf}, "}}", {remaining});
""")

            return Object(buf, Type('string'), call_position, free=buf_free)
        
        @c_dec(
            func_name_override=f'{dict_type.c_type}_type',
            add_to_class=c_manager,
            is_method=True, is_static=True
        )
        def dict_type_(_, call_position: Position) -> Object:
            return Object(f'"dict[{key_type}: {value_type}]"', Type('string'), call_position)
        
        @c_dec(
            param_types=(dict_type.c_type,),
            func_name_override=f'{dict_type.c_type}_keys',
            is_property=True,
            add_to_class=c_manager
        )
        def dict_keys(codegen, call_position: Position, dict_obj: Object) -> Object:
            key_arr_type = codegen.array_manager.define_array(key_type)
            keys = codegen.create_temp_var(key_arr_type, call_position)
            i = codegen.create_temp_var(Type('int'), call_position)
            d = f'({dict_obj.code})'
            codegen.prepend_code(f"""{key_arr_type.c_type} {keys} = {codegen.call(
    f'{key_arr_type.c_type}_make', [], call_position
).code};
for (size_t {i} = 0; {i} < {d}.length; {i}++) {{
    """)
            codegen.prepend_code(f"""{codegen.call(
        f'{key_arr_type.c_type}_add',
        [
            Arg(Object(keys, key_arr_type, call_position)),
            Arg(Object(f'{d}.elements[{i}].key', key_type, call_position))
        ],
        call_position
    ).code};
}}""")
            
            return Object(keys, key_arr_type, call_position)
        
        @c_dec(
            param_types=(dict_type.c_type,),
            func_name_override=f'{dict_type.c_type}_values',
            is_property=True,
            add_to_class=c_manager
        )
        def dict_values(codegen, call_position: Position, dict_obj: Object) -> Object:
            val_arr_type = codegen.array_manager.define_array(value_type)
            values = codegen.create_temp_var(val_arr_type, call_position)
            i = codegen.create_temp_var(Type('int'), call_position)
            d = f'({dict_obj.code})'
            codegen.prepend_code(f"""{val_arr_type.c_type} {values} = {codegen.call(
    f'{val_arr_type.c_type}_make', [], call_position
).code};
for (size_t {i} = 0; {i} < {d}.length; {i}++) {{
    """)
            codegen.prepend_code(f"""{codegen.call(
        f'{val_arr_type.c_type}_add',
        [
            Arg(Object(values, val_arr_type, call_position)),
            Arg(Object(f'{d}.elements[{i}].value', value_type, call_position))
        ],
        call_position
    ).code};
}}""")
            
            return Object(values, val_arr_type, call_position)
        
        @c_dec(
            param_types=(dict_type.c_type,),
            func_name_override=f'{dict_type.c_type}_length', add_to_class=c_manager,
            is_property=True
        )
        def dict_length(_, call_position: Position, dict_obj: Object) -> Object:
            return Object(f'(({dict_obj.code}).length)', Type('int'), call_position)
        
        @c_dec(
            param_types=(dict_type.c_type, key_type.c_type),
            func_name_override=f'index_{dict_type.c_type}',
            add_to_class=c_manager
        )
        def index_dict(codegen, call_position: Position, dict_obj: Object, key: Object) -> Object:
            return dict_get(codegen, call_position, dict_obj, key)
        
        @c_dec(
            param_types=(dict_type.c_type, 'int'),
            return_type=pair_type,
            func_name_override=f'iter_{dict_type.c_type}', add_to_class=c_manager
        )
        def iter_dict(_, call_position: Position, dict_obj: Object, i: Object) -> Object:
            return Object(f'(({dict_obj.code}).elements[{i.code}])', pair_type, call_position)
        
        self.defined_types.append((key_type.type, value_type.type))
        return dict_type
