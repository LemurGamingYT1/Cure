from codegen.objects import Object, Position, Type
from codegen.c_manager import c_dec


class RGB:
    def __init__(self, codegen) -> None:
        codegen.add_toplevel_code("""#ifndef CURE_COLOR_H
typedef struct {
    unsigned char r;
    unsigned char g;
    unsigned char b;
} RGB;
#endif
""")
    
    @c_dec(is_method=True, is_static=True)
    def _RGB_type(self, _, call_position: Position) -> Object:
        return Object('"RGB"', Type('string'), call_position)
    
    @c_dec(param_types=('RGB',), is_method=True)
    def _RGB_to_string(self, codegen, call_position: Position, rgb: Object) -> Object:
        cls = f'({rgb})'
        code, buf_free = codegen.c_manager.fmt_length(
            codegen, call_position,
            '"RGB(%d, %d, %d)"',
            f'{cls}.r', f'{cls}.g', f'{cls}.b'
        )
        
        codegen.prepend_code(code)
        return Object(buf_free.object_name, Type('string'), call_position, free=buf_free)
    
    
    @c_dec(param_types=('RGB',), is_property=True)
    def _RGB_r(self, _, call_position: Position, rgb: Object) -> Object:
        return Object(f'(({rgb}).r)', Type('int'), call_position)
    
    @c_dec(param_types=('RGB',), is_property=True)
    def _RGB_g(self, _, call_position: Position, rgb: Object) -> Object:
        return Object(f'(({rgb}).g)', Type('int'), call_position)
    
    @c_dec(param_types=('RGB',), is_property=True)
    def _RGB_b(self, _, call_position: Position, rgb: Object) -> Object:
        return Object(f'(({rgb}).b)', Type('int'), call_position)
    
    @c_dec(
        param_types=('RGB',),
        is_property=True
    )
    def _RGB_to_hsv(self, codegen, call_position: Position, rgb: Object) -> Object:
        codegen.c_manager.include('<math.h>', codegen)
        
        cls = f'({rgb})'
        r = codegen.create_temp_var(Type('float'), call_position)
        g = codegen.create_temp_var(Type('float'), call_position)
        b = codegen.create_temp_var(Type('float'), call_position)
        hsv = codegen.create_temp_var(Type('HSV'), call_position)
        delta = codegen.create_temp_var(Type('float'), call_position)
        _max = codegen.create_temp_var(Type('float'), call_position)
        _min = codegen.create_temp_var(Type('float'), call_position)
        codegen.prepend_code(f"""float {r} = {cls}.r / 255.0f;
float {g} = {cls}.g / 255.0f;
float {b} = {cls}.b / 255.0f;
float {_min} = {r} > {g} ? ({r} > {b} ? {r} : {b}) : ({g} > {b} ? {g} : {b});
float {_max} = {r} < {g} ? ({r} < {b} ? {r} : {b}) : ({g} < {b} ? {g} : {b});
float {delta} = {_max} - {_min};
HSV {hsv};
if ({delta} == 0) {{
    {hsv}.h = 0;
}} else if ({_max} == {r}) {{
    {hsv}.h = 60 * fmod((({g} - {b}) / {delta}), 6);
}} else if ({_max} == {g}) {{
    {hsv}.h = 60 * ((({b} - {r}) / {delta}) + 2);
}} else {{
    {hsv}.h = 60 * ((({r} - {g}) / {delta}) + 4);
}}

if ({hsv}.h < 0) {{
    {hsv}.h += 360;
}}

{hsv}.s = {_max} == 0 ? 0 : ({delta} / {_max});
{hsv}.v = {_max};
""")
        
        return Object(hsv, Type('HSV'), call_position)
