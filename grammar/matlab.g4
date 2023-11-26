/*
BSD License
Copyright (c) 2013, Tom Everett
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. Neither the name of Tom Everett nor the names of its contributors
   may be used to endorse or promote products derived from this software
   without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/
/*
* Grammar based on yacc-keable for matlab by Danny Luk 12/1995
*
* http://www.angelfire.com/ar/CompiladoresUCSE/images/MATLAB.zip
*/

grammar matlab;

file_ : statement_list? EOF;

primary_expression
   : IDENTIFIER
   | CONSTANT
   | STRING_LITERAL
   | open_par expression close_par
   | open_bracket close_bracket
   | open_bracket array_list close_bracket
   ;

open_par
   : '('
   ;

close_par
    : ')'
    ;

open_bracket
    : '['
    ;

close_bracket
    : ']'
    ;

postfix_expression
   : primary_expression
   | array_expression
   | postfix_expression TRANSPOSE
   | postfix_expression NCTRANSPOSE
   ;

index_expression
   : colon
   | expression
   ;

colon
   : ':'
   ;

semicolon
   : ';'
   ;

index_expression_list
   : index_expression
   | index_expression_list comma index_expression
   ;

comma
    : ','
    ;

array_expression
   : IDENTIFIER open_par index_expression_list close_par
   ;

unary_expression
   : postfix_expression
   | unary_operator postfix_expression
   ;

unary_operator
   : op_sum
   | op_sub
   | op_not
   ;

op_sum
   : '+'
   ;

op_sub
    : '-'
    ;

op_mul
    : '*'
    ;

op_div
    : '/'
    ;

op_not
    : '~'
    ;

op_pow
    : '^'
    ;

op_and
    : '&'
    ;

op_or
    : '|'
    ;

op_doble_backslash
    : '\\'
    ;

op_greater
    : '>'
    ;

op_less
    : '<'
    ;

op_greater_equal
    : '>='
    ;

op_less_equal
    : '<='
    ;

op_not_equal
    : '~='
    ;

op_equal
    : '='
    ;


multiplicative_expression
   : unary_expression
   | multiplicative_expression op_mul unary_expression
   | multiplicative_expression op_div unary_expression
   | multiplicative_expression op_doble_backslash unary_expression
   | multiplicative_expression op_pow unary_expression
   | multiplicative_expression ARRAYMUL unary_expression
   | multiplicative_expression ARRAYDIV unary_expression
   | multiplicative_expression ARRAYRDIV unary_expression
   | multiplicative_expression ARRAYPOW unary_expression
   ;

additive_expression
   : multiplicative_expression
   | additive_expression op_sum multiplicative_expression
   | additive_expression op_sub multiplicative_expression
   ;

relational_expression
   : additive_expression
   | relational_expression op_less additive_expression
   | relational_expression op_greater additive_expression
   | relational_expression LE_OP additive_expression
   | relational_expression GE_OP additive_expression
   ;

equality_expression
   : relational_expression
   | equality_expression eq_op relational_expression
   | equality_expression ne_op relational_expression
   ;

and_expression
   : equality_expression
   | and_expression op_and equality_expression
   ;

or_expression
   : and_expression
   | or_expression op_or and_expression
   ;

expression
   : or_expression
   | expression colon or_expression
   ;

assignment_expression
   : postfix_expression op_equal expression
   ;

eostmt
   : comma
   | semicolon
   | CR
   ;

statement
   : global_statement
   | clear_statement
   | assignment_statement
   | expression_statement
   | selection_statement
   | iteration_statement
   | jump_statement
   ;

statement_list
   : statement
   | statement_list statement
   ;

identifier_list
   : IDENTIFIER
   | identifier_list IDENTIFIER
   ;

global_statement
   : GLOBAL identifier_list eostmt
   ;

clear_statement
   : CLEAR identifier_list eostmt
   ;

expression_statement
   : eostmt
   | expression eostmt
   ;

assignment_statement
   : assignment_expression eostmt
   ;

array_element
   : expression
   | expression_statement
   ;

array_list
   : array_element
   | array_list array_element
   ;

selection_statement
   : if expression statement_list end eostmt
   | if expression statement_list else statement_list end eostmt
   | if expression statement_list elseif_clause end eostmt
   | if expression statement_list elseif_clause else statement_list end eostmt
   ;

elseif_clause
   : elseif expression statement_list
   | elseif_clause elseif expression statement_list
   ;

iteration_statement
   : WHILE expression statement_list end eostmt
   | FOR IDENTIFIER op_equal expression statement_list end eostmt
   | FOR open_par IDENTIFIER op_equal expression close_par statement_list end eostmt
   ;

jump_statement
   : break eostmt
   | RETURN eostmt
   ;

translation_unit
   : statement_list
   | FUNCTION function_declare eostmt statement_list
   ;

func_ident_list
   : IDENTIFIER
   | func_ident_list comma IDENTIFIER
   ;

func_return_list
   : IDENTIFIER
   | open_bracket func_ident_list close_bracket
   ;

function_declare_lhs
   : IDENTIFIER
   | IDENTIFIER open_par close_par
   | IDENTIFIER open_par func_ident_list close_par
   ;

function_declare
   : function_declare_lhs
   | func_return_list op_equal function_declare_lhs
   ;


ARRAYMUL
   : '.*'
   ;


ARRAYDIV
   : '.\\'
   ;


ARRAYRDIV
   : './'
   ;


ARRAYPOW
   : '.^'
   ;


break
   : 'break'
   ;


RETURN
   : 'return'
   ;


FUNCTION
   : 'function'
   ;


FOR
   : 'for'
   ;


WHILE
   : 'while'
   ;


end
   : 'end'
   ;


GLOBAL
   : 'global'
   ;


if
   : 'if'
   ;


CLEAR
   : 'clear'
   ;


else
   : 'else'
   ;


elseif
   : 'elseif'
   ;


LE_OP
   : '<='
   ;


GE_OP
   : '>='
   ;


eq_op
   : '=='
   ;


ne_op
   : '~='
   ;


TRANSPOSE
   : 'transpose'
   ;


NCTRANSPOSE
   : '.\''
   ;


STRING_LITERAL
   : '\'' ( ~ '\'' | '\'\'' ) * '\''
   ;


IDENTIFIER
   : [a-zA-Z] [a-zA-Z0-9_]*
   ;


CONSTANT
   : NUMBER (E SIGN? NUMBER)?
   ;


fragment NUMBER
   : ('0' .. '9') + ('.' ('0' .. '9') +)?
   ;


fragment E
   : 'E' | 'e'
   ;


fragment SIGN
   : ('+' | '-')
   ;


CR
   : [\r\n] +
   ;


WS
   : [ \t] + -> skip
   ;

Comments
    : [/%] .*? [\r\n] -> skip
    ;