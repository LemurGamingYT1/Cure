# Generated from cure/Cure.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,50,283,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,5,0,46,8,0,10,0,12,0,49,9,0,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,3,1,58,8,1,1,1,1,1,3,1,62,8,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,71,8,2,1,3,1,3,1,3,1,3,1,3,3,3,78,8,3,1,4,1,4,5,4,82,8,4,
        10,4,12,4,85,9,4,1,4,1,4,1,5,1,5,1,5,1,5,5,5,93,8,5,10,5,12,5,96,
        9,5,1,5,3,5,99,8,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,
        8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,11,3,11,
        126,8,11,1,11,1,11,1,11,1,12,5,12,132,8,12,10,12,12,12,135,9,12,
        1,12,1,12,1,12,1,12,3,12,141,8,12,1,12,1,12,1,12,3,12,146,8,12,1,
        12,1,12,1,13,3,13,151,8,13,1,13,1,13,3,13,155,8,13,1,13,1,13,1,13,
        1,14,1,14,1,15,1,15,1,15,5,15,165,8,15,10,15,12,15,168,9,15,1,16,
        1,16,3,16,172,8,16,1,16,1,16,1,17,1,17,1,17,5,17,179,8,17,10,17,
        12,17,182,9,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,3,19,191,8,19,
        1,19,1,19,1,20,1,20,1,20,3,20,198,8,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,5,20,211,8,20,10,20,12,20,214,9,20,
        3,20,216,8,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,3,20,232,8,20,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,3,21,245,8,21,1,21,3,21,248,8,21,1,21,1,
        21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,
        21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,273,8,21,1,21,3,
        21,276,8,21,5,21,278,8,21,10,21,12,21,281,9,21,1,21,0,1,42,22,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,0,5,1,
        0,21,25,1,0,21,22,1,0,23,25,1,0,26,31,1,0,32,33,311,0,47,1,0,0,0,
        2,52,1,0,0,0,4,70,1,0,0,0,6,77,1,0,0,0,8,79,1,0,0,0,10,88,1,0,0,
        0,12,100,1,0,0,0,14,105,1,0,0,0,16,108,1,0,0,0,18,112,1,0,0,0,20,
        118,1,0,0,0,22,121,1,0,0,0,24,133,1,0,0,0,26,150,1,0,0,0,28,159,
        1,0,0,0,30,161,1,0,0,0,32,169,1,0,0,0,34,175,1,0,0,0,36,183,1,0,
        0,0,38,187,1,0,0,0,40,231,1,0,0,0,42,247,1,0,0,0,44,46,3,4,2,0,45,
        44,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,
        0,49,47,1,0,0,0,50,51,5,0,0,1,51,1,1,0,0,0,52,61,5,20,0,0,53,54,
        5,43,0,0,54,57,3,2,1,0,55,56,5,37,0,0,56,58,3,2,1,0,57,55,1,0,0,
        0,57,58,1,0,0,0,58,59,1,0,0,0,59,60,5,44,0,0,60,62,1,0,0,0,61,53,
        1,0,0,0,61,62,1,0,0,0,62,3,1,0,0,0,63,71,3,24,12,0,64,71,3,18,9,
        0,65,71,3,16,8,0,66,71,3,10,5,0,67,71,3,26,13,0,68,71,3,42,21,0,
        69,71,3,20,10,0,70,63,1,0,0,0,70,64,1,0,0,0,70,65,1,0,0,0,70,66,
        1,0,0,0,70,67,1,0,0,0,70,68,1,0,0,0,70,69,1,0,0,0,71,5,1,0,0,0,72,
        78,3,4,2,0,73,74,5,9,0,0,74,78,3,42,21,0,75,78,5,11,0,0,76,78,5,
        8,0,0,77,72,1,0,0,0,77,73,1,0,0,0,77,75,1,0,0,0,77,76,1,0,0,0,78,
        7,1,0,0,0,79,83,5,41,0,0,80,82,3,6,3,0,81,80,1,0,0,0,82,85,1,0,0,
        0,83,81,1,0,0,0,83,84,1,0,0,0,84,86,1,0,0,0,85,83,1,0,0,0,86,87,
        5,42,0,0,87,9,1,0,0,0,88,89,5,1,0,0,89,90,3,42,21,0,90,94,3,8,4,
        0,91,93,3,12,6,0,92,91,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,
        1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,97,99,3,14,7,0,98,97,1,0,0,0,
        98,99,1,0,0,0,99,11,1,0,0,0,100,101,5,5,0,0,101,102,5,1,0,0,102,
        103,3,42,21,0,103,104,3,8,4,0,104,13,1,0,0,0,105,106,5,5,0,0,106,
        107,3,8,4,0,107,15,1,0,0,0,108,109,5,7,0,0,109,110,3,42,21,0,110,
        111,3,8,4,0,111,17,1,0,0,0,112,113,5,10,0,0,113,114,5,20,0,0,114,
        115,5,2,0,0,115,116,3,42,21,0,116,117,3,8,4,0,117,19,1,0,0,0,118,
        119,5,4,0,0,119,120,5,15,0,0,120,21,1,0,0,0,121,122,5,43,0,0,122,
        123,5,20,0,0,123,125,5,39,0,0,124,126,3,30,15,0,125,124,1,0,0,0,
        125,126,1,0,0,0,126,127,1,0,0,0,127,128,5,40,0,0,128,129,5,44,0,
        0,129,23,1,0,0,0,130,132,3,22,11,0,131,130,1,0,0,0,132,135,1,0,0,
        0,133,131,1,0,0,0,133,134,1,0,0,0,134,136,1,0,0,0,135,133,1,0,0,
        0,136,137,5,6,0,0,137,138,5,20,0,0,138,140,5,39,0,0,139,141,3,34,
        17,0,140,139,1,0,0,0,140,141,1,0,0,0,141,142,1,0,0,0,142,145,5,40,
        0,0,143,144,5,46,0,0,144,146,3,2,1,0,145,143,1,0,0,0,145,146,1,0,
        0,0,146,147,1,0,0,0,147,148,3,8,4,0,148,25,1,0,0,0,149,151,3,2,1,
        0,150,149,1,0,0,0,150,151,1,0,0,0,151,152,1,0,0,0,152,154,5,20,0,
        0,153,155,7,0,0,0,154,153,1,0,0,0,154,155,1,0,0,0,155,156,1,0,0,
        0,156,157,5,38,0,0,157,158,3,42,21,0,158,27,1,0,0,0,159,160,3,42,
        21,0,160,29,1,0,0,0,161,166,3,28,14,0,162,163,5,36,0,0,163,165,3,
        28,14,0,164,162,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,166,167,
        1,0,0,0,167,31,1,0,0,0,168,166,1,0,0,0,169,171,3,2,1,0,170,172,5,
        47,0,0,171,170,1,0,0,0,171,172,1,0,0,0,172,173,1,0,0,0,173,174,5,
        20,0,0,174,33,1,0,0,0,175,180,3,32,16,0,176,177,5,36,0,0,177,179,
        3,32,16,0,178,176,1,0,0,0,179,182,1,0,0,0,180,178,1,0,0,0,180,181,
        1,0,0,0,181,35,1,0,0,0,182,180,1,0,0,0,183,184,3,42,21,0,184,185,
        5,37,0,0,185,186,3,42,21,0,186,37,1,0,0,0,187,188,5,20,0,0,188,190,
        5,39,0,0,189,191,3,30,15,0,190,189,1,0,0,0,190,191,1,0,0,0,191,192,
        1,0,0,0,192,193,5,40,0,0,193,39,1,0,0,0,194,195,3,2,1,0,195,197,
        5,41,0,0,196,198,3,30,15,0,197,196,1,0,0,0,197,198,1,0,0,0,198,199,
        1,0,0,0,199,200,5,42,0,0,200,232,1,0,0,0,201,202,5,43,0,0,202,203,
        3,2,1,0,203,204,5,37,0,0,204,205,3,2,1,0,205,206,5,44,0,0,206,215,
        5,41,0,0,207,212,3,36,18,0,208,209,5,36,0,0,209,211,3,36,18,0,210,
        208,1,0,0,0,211,214,1,0,0,0,212,210,1,0,0,0,212,213,1,0,0,0,213,
        216,1,0,0,0,214,212,1,0,0,0,215,207,1,0,0,0,215,216,1,0,0,0,216,
        217,1,0,0,0,217,218,5,42,0,0,218,232,1,0,0,0,219,232,5,18,0,0,220,
        232,5,16,0,0,221,232,5,13,0,0,222,232,5,14,0,0,223,232,5,15,0,0,
        224,232,5,17,0,0,225,232,5,19,0,0,226,232,5,20,0,0,227,228,5,39,
        0,0,228,229,3,42,21,0,229,230,5,40,0,0,230,232,1,0,0,0,231,194,1,
        0,0,0,231,201,1,0,0,0,231,219,1,0,0,0,231,220,1,0,0,0,231,221,1,
        0,0,0,231,222,1,0,0,0,231,223,1,0,0,0,231,224,1,0,0,0,231,225,1,
        0,0,0,231,226,1,0,0,0,231,227,1,0,0,0,232,41,1,0,0,0,233,234,6,21,
        -1,0,234,248,3,38,19,0,235,248,3,40,20,0,236,237,5,34,0,0,237,248,
        3,42,21,8,238,239,5,22,0,0,239,248,3,42,21,7,240,241,5,3,0,0,241,
        242,5,20,0,0,242,244,5,39,0,0,243,245,3,30,15,0,244,243,1,0,0,0,
        244,245,1,0,0,0,245,246,1,0,0,0,246,248,5,40,0,0,247,233,1,0,0,0,
        247,235,1,0,0,0,247,236,1,0,0,0,247,238,1,0,0,0,247,240,1,0,0,0,
        248,279,1,0,0,0,249,250,10,6,0,0,250,251,7,1,0,0,251,278,3,42,21,
        7,252,253,10,5,0,0,253,254,7,2,0,0,254,278,3,42,21,6,255,256,10,
        4,0,0,256,257,7,3,0,0,257,278,3,42,21,5,258,259,10,3,0,0,259,260,
        7,4,0,0,260,278,3,42,21,4,261,262,10,2,0,0,262,263,5,1,0,0,263,264,
        3,42,21,0,264,265,5,5,0,0,265,266,3,42,21,3,266,278,1,0,0,0,267,
        268,10,11,0,0,268,269,5,35,0,0,269,275,5,20,0,0,270,272,5,39,0,0,
        271,273,3,30,15,0,272,271,1,0,0,0,272,273,1,0,0,0,273,274,1,0,0,
        0,274,276,5,40,0,0,275,270,1,0,0,0,275,276,1,0,0,0,276,278,1,0,0,
        0,277,249,1,0,0,0,277,252,1,0,0,0,277,255,1,0,0,0,277,258,1,0,0,
        0,277,261,1,0,0,0,277,267,1,0,0,0,278,281,1,0,0,0,279,277,1,0,0,
        0,279,280,1,0,0,0,280,43,1,0,0,0,281,279,1,0,0,0,28,47,57,61,70,
        77,83,94,98,125,133,140,145,150,154,166,171,180,190,197,212,215,
        231,244,247,272,275,277,279
    ]

class CureParser ( Parser ):

    grammarFileName = "Cure.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'in'", "'new'", "'use'", "'else'", 
                     "'func'", "'while'", "'break'", "'return'", "'foreach'", 
                     "'continue'", "'''", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'nil'", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
                     "'>'", "'<'", "'>='", "'<='", "'&&'", "'||'", "'!'", 
                     "'.'", "','", "':'", "'='", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "'$'", "'->'", "'&'" ]

    symbolicNames = [ "<INVALID>", "IF", "IN", "NEW", "USE", "ELSE", "FUNC", 
                      "WHILE", "BREAK", "RETURN", "FOREACH", "CONTINUE", 
                      "APOSTROPHE", "INT", "FLOAT", "STRING", "HEX", "BOOL", 
                      "BIN", "NIL", "ID", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "EEQ", "NEQ", "GT", "LT", "GTE", "LTE", "AND", "OR", 
                      "NOT", "DOT", "COMMA", "COLON", "ASSIGN", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                      "DOLLAR", "RETURNS", "AMPERSAND", "COMMENT", "MULTILINE_COMMENT", 
                      "WHITESPACE" ]

    RULE_parse = 0
    RULE_type = 1
    RULE_stmt = 2
    RULE_bodyStmts = 3
    RULE_body = 4
    RULE_ifStmt = 5
    RULE_elseifStmt = 6
    RULE_elseStmt = 7
    RULE_whileStmt = 8
    RULE_foreachStmt = 9
    RULE_useStmt = 10
    RULE_funcModifications = 11
    RULE_funcAssign = 12
    RULE_varAssign = 13
    RULE_arg = 14
    RULE_args = 15
    RULE_param = 16
    RULE_params = 17
    RULE_dict_element = 18
    RULE_call = 19
    RULE_atom = 20
    RULE_expr = 21

    ruleNames =  [ "parse", "type", "stmt", "bodyStmts", "body", "ifStmt", 
                   "elseifStmt", "elseStmt", "whileStmt", "foreachStmt", 
                   "useStmt", "funcModifications", "funcAssign", "varAssign", 
                   "arg", "args", "param", "params", "dict_element", "call", 
                   "atom", "expr" ]

    EOF = Token.EOF
    IF=1
    IN=2
    NEW=3
    USE=4
    ELSE=5
    FUNC=6
    WHILE=7
    BREAK=8
    RETURN=9
    FOREACH=10
    CONTINUE=11
    APOSTROPHE=12
    INT=13
    FLOAT=14
    STRING=15
    HEX=16
    BOOL=17
    BIN=18
    NIL=19
    ID=20
    ADD=21
    SUB=22
    MUL=23
    DIV=24
    MOD=25
    EEQ=26
    NEQ=27
    GT=28
    LT=29
    GTE=30
    LTE=31
    AND=32
    OR=33
    NOT=34
    DOT=35
    COMMA=36
    COLON=37
    ASSIGN=38
    LPAREN=39
    RPAREN=40
    LBRACE=41
    RBRACE=42
    LBRACK=43
    RBRACK=44
    DOLLAR=45
    RETURNS=46
    AMPERSAND=47
    COMMENT=48
    MULTILINE_COMMENT=49
    WHITESPACE=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CureParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CureParser.StmtContext)
            else:
                return self.getTypedRuleContext(CureParser.StmtContext,i)


        def getRuleIndex(self):
            return CureParser.RULE_parse

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParse" ):
                return visitor.visitParse(self)
            else:
                return visitor.visitChildren(self)




    def parse(self):

        localctx = CureParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 9363034989786) != 0):
                self.state = 44
                self.stmt()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(CureParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CureParser.ID, 0)

        def LBRACK(self):
            return self.getToken(CureParser.LBRACK, 0)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CureParser.TypeContext)
            else:
                return self.getTypedRuleContext(CureParser.TypeContext,i)


        def RBRACK(self):
            return self.getToken(CureParser.RBRACK, 0)

        def COLON(self):
            return self.getToken(CureParser.COLON, 0)

        def getRuleIndex(self):
            return CureParser.RULE_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = CureParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(CureParser.ID)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 53
                self.match(CureParser.LBRACK)
                self.state = 54
                self.type_()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==37:
                    self.state = 55
                    self.match(CureParser.COLON)
                    self.state = 56
                    self.type_()


                self.state = 59
                self.match(CureParser.RBRACK)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcAssign(self):
            return self.getTypedRuleContext(CureParser.FuncAssignContext,0)


        def foreachStmt(self):
            return self.getTypedRuleContext(CureParser.ForeachStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(CureParser.WhileStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(CureParser.IfStmtContext,0)


        def varAssign(self):
            return self.getTypedRuleContext(CureParser.VarAssignContext,0)


        def expr(self):
            return self.getTypedRuleContext(CureParser.ExprContext,0)


        def useStmt(self):
            return self.getTypedRuleContext(CureParser.UseStmtContext,0)


        def getRuleIndex(self):
            return CureParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = CureParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.funcAssign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.foreachStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.whileStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 66
                self.ifStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 67
                self.varAssign()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 68
                self.expr(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 69
                self.useStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyStmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(CureParser.StmtContext,0)


        def RETURN(self):
            return self.getToken(CureParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(CureParser.ExprContext,0)


        def CONTINUE(self):
            return self.getToken(CureParser.CONTINUE, 0)

        def BREAK(self):
            return self.getToken(CureParser.BREAK, 0)

        def getRuleIndex(self):
            return CureParser.RULE_bodyStmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBodyStmts" ):
                return visitor.visitBodyStmts(self)
            else:
                return visitor.visitChildren(self)




    def bodyStmts(self):

        localctx = CureParser.BodyStmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bodyStmts)
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 4, 6, 7, 10, 13, 14, 15, 16, 17, 18, 19, 20, 22, 34, 39, 43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.stmt()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.match(CureParser.RETURN)
                self.state = 74
                self.expr(0)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.match(CureParser.CONTINUE)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.match(CureParser.BREAK)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(CureParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CureParser.RBRACE, 0)

        def bodyStmts(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CureParser.BodyStmtsContext)
            else:
                return self.getTypedRuleContext(CureParser.BodyStmtsContext,i)


        def getRuleIndex(self):
            return CureParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = CureParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(CureParser.LBRACE)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 9363034992602) != 0):
                self.state = 80
                self.bodyStmts()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self.match(CureParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CureParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(CureParser.ExprContext,0)


        def body(self):
            return self.getTypedRuleContext(CureParser.BodyContext,0)


        def elseifStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CureParser.ElseifStmtContext)
            else:
                return self.getTypedRuleContext(CureParser.ElseifStmtContext,i)


        def elseStmt(self):
            return self.getTypedRuleContext(CureParser.ElseStmtContext,0)


        def getRuleIndex(self):
            return CureParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = CureParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(CureParser.IF)
            self.state = 89
            self.expr(0)
            self.state = 90
            self.body()
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 91
                    self.elseifStmt() 
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 97
                self.elseStmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseifStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(CureParser.ELSE, 0)

        def IF(self):
            return self.getToken(CureParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(CureParser.ExprContext,0)


        def body(self):
            return self.getTypedRuleContext(CureParser.BodyContext,0)


        def getRuleIndex(self):
            return CureParser.RULE_elseifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseifStmt" ):
                return visitor.visitElseifStmt(self)
            else:
                return visitor.visitChildren(self)




    def elseifStmt(self):

        localctx = CureParser.ElseifStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_elseifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(CureParser.ELSE)
            self.state = 101
            self.match(CureParser.IF)
            self.state = 102
            self.expr(0)
            self.state = 103
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(CureParser.ELSE, 0)

        def body(self):
            return self.getTypedRuleContext(CureParser.BodyContext,0)


        def getRuleIndex(self):
            return CureParser.RULE_elseStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseStmt" ):
                return visitor.visitElseStmt(self)
            else:
                return visitor.visitChildren(self)




    def elseStmt(self):

        localctx = CureParser.ElseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_elseStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(CureParser.ELSE)
            self.state = 106
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(CureParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(CureParser.ExprContext,0)


        def body(self):
            return self.getTypedRuleContext(CureParser.BodyContext,0)


        def getRuleIndex(self):
            return CureParser.RULE_whileStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = CureParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(CureParser.WHILE)
            self.state = 109
            self.expr(0)
            self.state = 110
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForeachStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(CureParser.FOREACH, 0)

        def ID(self):
            return self.getToken(CureParser.ID, 0)

        def IN(self):
            return self.getToken(CureParser.IN, 0)

        def expr(self):
            return self.getTypedRuleContext(CureParser.ExprContext,0)


        def body(self):
            return self.getTypedRuleContext(CureParser.BodyContext,0)


        def getRuleIndex(self):
            return CureParser.RULE_foreachStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForeachStmt" ):
                return visitor.visitForeachStmt(self)
            else:
                return visitor.visitChildren(self)




    def foreachStmt(self):

        localctx = CureParser.ForeachStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_foreachStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(CureParser.FOREACH)
            self.state = 113
            self.match(CureParser.ID)
            self.state = 114
            self.match(CureParser.IN)
            self.state = 115
            self.expr(0)
            self.state = 116
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UseStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def USE(self):
            return self.getToken(CureParser.USE, 0)

        def STRING(self):
            return self.getToken(CureParser.STRING, 0)

        def getRuleIndex(self):
            return CureParser.RULE_useStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUseStmt" ):
                return visitor.visitUseStmt(self)
            else:
                return visitor.visitChildren(self)




    def useStmt(self):

        localctx = CureParser.UseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_useStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(CureParser.USE)
            self.state = 119
            self.match(CureParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncModificationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(CureParser.LBRACK, 0)

        def ID(self):
            return self.getToken(CureParser.ID, 0)

        def LPAREN(self):
            return self.getToken(CureParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CureParser.RPAREN, 0)

        def RBRACK(self):
            return self.getToken(CureParser.RBRACK, 0)

        def args(self):
            return self.getTypedRuleContext(CureParser.ArgsContext,0)


        def getRuleIndex(self):
            return CureParser.RULE_funcModifications

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncModifications" ):
                return visitor.visitFuncModifications(self)
            else:
                return visitor.visitChildren(self)




    def funcModifications(self):

        localctx = CureParser.FuncModificationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_funcModifications)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(CureParser.LBRACK)
            self.state = 122
            self.match(CureParser.ID)
            self.state = 123
            self.match(CureParser.LPAREN)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9363034988552) != 0):
                self.state = 124
                self.args()


            self.state = 127
            self.match(CureParser.RPAREN)
            self.state = 128
            self.match(CureParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CureParser.FUNC, 0)

        def ID(self):
            return self.getToken(CureParser.ID, 0)

        def LPAREN(self):
            return self.getToken(CureParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CureParser.RPAREN, 0)

        def body(self):
            return self.getTypedRuleContext(CureParser.BodyContext,0)


        def funcModifications(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CureParser.FuncModificationsContext)
            else:
                return self.getTypedRuleContext(CureParser.FuncModificationsContext,i)


        def params(self):
            return self.getTypedRuleContext(CureParser.ParamsContext,0)


        def RETURNS(self):
            return self.getToken(CureParser.RETURNS, 0)

        def type_(self):
            return self.getTypedRuleContext(CureParser.TypeContext,0)


        def getRuleIndex(self):
            return CureParser.RULE_funcAssign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncAssign" ):
                return visitor.visitFuncAssign(self)
            else:
                return visitor.visitChildren(self)




    def funcAssign(self):

        localctx = CureParser.FuncAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_funcAssign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 130
                self.funcModifications()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
            self.match(CureParser.FUNC)
            self.state = 137
            self.match(CureParser.ID)
            self.state = 138
            self.match(CureParser.LPAREN)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 139
                self.params()


            self.state = 142
            self.match(CureParser.RPAREN)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 143
                self.match(CureParser.RETURNS)
                self.state = 144
                self.type_()


            self.state = 147
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def ID(self):
            return self.getToken(CureParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(CureParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(CureParser.ExprContext,0)


        def type_(self):
            return self.getTypedRuleContext(CureParser.TypeContext,0)


        def ADD(self):
            return self.getToken(CureParser.ADD, 0)

        def SUB(self):
            return self.getToken(CureParser.SUB, 0)

        def MUL(self):
            return self.getToken(CureParser.MUL, 0)

        def DIV(self):
            return self.getToken(CureParser.DIV, 0)

        def MOD(self):
            return self.getToken(CureParser.MOD, 0)

        def getRuleIndex(self):
            return CureParser.RULE_varAssign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarAssign" ):
                return visitor.visitVarAssign(self)
            else:
                return visitor.visitChildren(self)




    def varAssign(self):

        localctx = CureParser.VarAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_varAssign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 149
                self.type_()


            self.state = 152
            self.match(CureParser.ID)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 65011712) != 0):
                self.state = 153
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 65011712) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 156
            self.match(CureParser.ASSIGN)
            self.state = 157
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CureParser.ExprContext,0)


        def getRuleIndex(self):
            return CureParser.RULE_arg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg" ):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)




    def arg(self):

        localctx = CureParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CureParser.ArgContext)
            else:
                return self.getTypedRuleContext(CureParser.ArgContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CureParser.COMMA)
            else:
                return self.getToken(CureParser.COMMA, i)

        def getRuleIndex(self):
            return CureParser.RULE_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = CureParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.arg()
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 162
                self.match(CureParser.COMMA)
                self.state = 163
                self.arg()
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(CureParser.TypeContext,0)


        def ID(self):
            return self.getToken(CureParser.ID, 0)

        def AMPERSAND(self):
            return self.getToken(CureParser.AMPERSAND, 0)

        def getRuleIndex(self):
            return CureParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = CureParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.type_()
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 170
                self.match(CureParser.AMPERSAND)


            self.state = 173
            self.match(CureParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CureParser.ParamContext)
            else:
                return self.getTypedRuleContext(CureParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CureParser.COMMA)
            else:
                return self.getToken(CureParser.COMMA, i)

        def getRuleIndex(self):
            return CureParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = CureParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.param()
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 176
                self.match(CureParser.COMMA)
                self.state = 177
                self.param()
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dict_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CureParser.ExprContext)
            else:
                return self.getTypedRuleContext(CureParser.ExprContext,i)


        def COLON(self):
            return self.getToken(CureParser.COLON, 0)

        def getRuleIndex(self):
            return CureParser.RULE_dict_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDict_element" ):
                return visitor.visitDict_element(self)
            else:
                return visitor.visitChildren(self)




    def dict_element(self):

        localctx = CureParser.Dict_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_dict_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.expr(0)
            self.state = 184
            self.match(CureParser.COLON)
            self.state = 185
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CureParser.ID, 0)

        def LPAREN(self):
            return self.getToken(CureParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CureParser.RPAREN, 0)

        def args(self):
            return self.getTypedRuleContext(CureParser.ArgsContext,0)


        def getRuleIndex(self):
            return CureParser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = CureParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(CureParser.ID)
            self.state = 188
            self.match(CureParser.LPAREN)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9363034988552) != 0):
                self.state = 189
                self.args()


            self.state = 192
            self.match(CureParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CureParser.TypeContext)
            else:
                return self.getTypedRuleContext(CureParser.TypeContext,i)


        def LBRACE(self):
            return self.getToken(CureParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CureParser.RBRACE, 0)

        def args(self):
            return self.getTypedRuleContext(CureParser.ArgsContext,0)


        def LBRACK(self):
            return self.getToken(CureParser.LBRACK, 0)

        def COLON(self):
            return self.getToken(CureParser.COLON, 0)

        def RBRACK(self):
            return self.getToken(CureParser.RBRACK, 0)

        def dict_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CureParser.Dict_elementContext)
            else:
                return self.getTypedRuleContext(CureParser.Dict_elementContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CureParser.COMMA)
            else:
                return self.getToken(CureParser.COMMA, i)

        def BIN(self):
            return self.getToken(CureParser.BIN, 0)

        def HEX(self):
            return self.getToken(CureParser.HEX, 0)

        def INT(self):
            return self.getToken(CureParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CureParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(CureParser.STRING, 0)

        def BOOL(self):
            return self.getToken(CureParser.BOOL, 0)

        def NIL(self):
            return self.getToken(CureParser.NIL, 0)

        def ID(self):
            return self.getToken(CureParser.ID, 0)

        def LPAREN(self):
            return self.getToken(CureParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(CureParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(CureParser.RPAREN, 0)

        def getRuleIndex(self):
            return CureParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = CureParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.type_()
                self.state = 195
                self.match(CureParser.LBRACE)
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9363034988552) != 0):
                    self.state = 196
                    self.args()


                self.state = 199
                self.match(CureParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.match(CureParser.LBRACK)
                self.state = 202
                self.type_()
                self.state = 203
                self.match(CureParser.COLON)
                self.state = 204
                self.type_()
                self.state = 205
                self.match(CureParser.RBRACK)
                self.state = 206
                self.match(CureParser.LBRACE)
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9363034988552) != 0):
                    self.state = 207
                    self.dict_element()
                    self.state = 212
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==36:
                        self.state = 208
                        self.match(CureParser.COMMA)
                        self.state = 209
                        self.dict_element()
                        self.state = 214
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 217
                self.match(CureParser.RBRACE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 219
                self.match(CureParser.BIN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 220
                self.match(CureParser.HEX)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 221
                self.match(CureParser.INT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 222
                self.match(CureParser.FLOAT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 223
                self.match(CureParser.STRING)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 224
                self.match(CureParser.BOOL)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 225
                self.match(CureParser.NIL)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 226
                self.match(CureParser.ID)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 227
                self.match(CureParser.LPAREN)
                self.state = 228
                self.expr(0)
                self.state = 229
                self.match(CureParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.uop = None # Token
            self.op = None # Token

        def call(self):
            return self.getTypedRuleContext(CureParser.CallContext,0)


        def atom(self):
            return self.getTypedRuleContext(CureParser.AtomContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CureParser.ExprContext)
            else:
                return self.getTypedRuleContext(CureParser.ExprContext,i)


        def NOT(self):
            return self.getToken(CureParser.NOT, 0)

        def SUB(self):
            return self.getToken(CureParser.SUB, 0)

        def NEW(self):
            return self.getToken(CureParser.NEW, 0)

        def ID(self):
            return self.getToken(CureParser.ID, 0)

        def LPAREN(self):
            return self.getToken(CureParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CureParser.RPAREN, 0)

        def args(self):
            return self.getTypedRuleContext(CureParser.ArgsContext,0)


        def ADD(self):
            return self.getToken(CureParser.ADD, 0)

        def MUL(self):
            return self.getToken(CureParser.MUL, 0)

        def DIV(self):
            return self.getToken(CureParser.DIV, 0)

        def MOD(self):
            return self.getToken(CureParser.MOD, 0)

        def EEQ(self):
            return self.getToken(CureParser.EEQ, 0)

        def NEQ(self):
            return self.getToken(CureParser.NEQ, 0)

        def GT(self):
            return self.getToken(CureParser.GT, 0)

        def LT(self):
            return self.getToken(CureParser.LT, 0)

        def GTE(self):
            return self.getToken(CureParser.GTE, 0)

        def LTE(self):
            return self.getToken(CureParser.LTE, 0)

        def AND(self):
            return self.getToken(CureParser.AND, 0)

        def OR(self):
            return self.getToken(CureParser.OR, 0)

        def IF(self):
            return self.getToken(CureParser.IF, 0)

        def ELSE(self):
            return self.getToken(CureParser.ELSE, 0)

        def DOT(self):
            return self.getToken(CureParser.DOT, 0)

        def getRuleIndex(self):
            return CureParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CureParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 234
                self.call()
                pass

            elif la_ == 2:
                self.state = 235
                self.atom()
                pass

            elif la_ == 3:
                self.state = 236
                localctx.uop = self.match(CureParser.NOT)
                self.state = 237
                self.expr(8)
                pass

            elif la_ == 4:
                self.state = 238
                localctx.uop = self.match(CureParser.SUB)
                self.state = 239
                self.expr(7)
                pass

            elif la_ == 5:
                self.state = 240
                self.match(CureParser.NEW)
                self.state = 241
                self.match(CureParser.ID)
                self.state = 242
                self.match(CureParser.LPAREN)
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9363034988552) != 0):
                    self.state = 243
                    self.args()


                self.state = 246
                self.match(CureParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 279
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 277
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = CureParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 249
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 250
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 251
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = CureParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 252
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 253
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 254
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = CureParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 255
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 256
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4227858432) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 257
                        self.expr(5)
                        pass

                    elif la_ == 4:
                        localctx = CureParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 258
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 259
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==32 or _la==33):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 260
                        self.expr(4)
                        pass

                    elif la_ == 5:
                        localctx = CureParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 261
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 262
                        self.match(CureParser.IF)
                        self.state = 263
                        self.expr(0)
                        self.state = 264
                        self.match(CureParser.ELSE)
                        self.state = 265
                        self.expr(3)
                        pass

                    elif la_ == 6:
                        localctx = CureParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 267
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 268
                        self.match(CureParser.DOT)
                        self.state = 269
                        self.match(CureParser.ID)
                        self.state = 275
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                        if la_ == 1:
                            self.state = 270
                            self.match(CureParser.LPAREN)
                            self.state = 272
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9363034988552) != 0):
                                self.state = 271
                                self.args()


                            self.state = 274
                            self.match(CureParser.RPAREN)


                        pass

             
                self.state = 281
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[21] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 11)
         




