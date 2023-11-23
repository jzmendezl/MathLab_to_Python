# Generated from C:/Users/Kira/PycharmProjects/MathLab_to_Python/grammar/matlab.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .matlabParser import matlabParser
else:
    from matlabParser import matlabParser

# This class defines a complete listener for a parse tree produced by matlabParser.
class matlabListener(ParseTreeListener):

    # Enter a parse tree produced by matlabParser#file_.
    def enterFile_(self, ctx:matlabParser.File_Context):
        pass

    # Exit a parse tree produced by matlabParser#file_.
    def exitFile_(self, ctx:matlabParser.File_Context):
        pass


    # Enter a parse tree produced by matlabParser#primary_expression.
    def enterPrimary_expression(self, ctx:matlabParser.Primary_expressionContext):
        pass

    # Exit a parse tree produced by matlabParser#primary_expression.
    def exitPrimary_expression(self, ctx:matlabParser.Primary_expressionContext):
        pass


    # Enter a parse tree produced by matlabParser#open_par.
    def enterOpen_par(self, ctx:matlabParser.Open_parContext):
        pass

    # Exit a parse tree produced by matlabParser#open_par.
    def exitOpen_par(self, ctx:matlabParser.Open_parContext):
        pass


    # Enter a parse tree produced by matlabParser#close_par.
    def enterClose_par(self, ctx:matlabParser.Close_parContext):
        pass

    # Exit a parse tree produced by matlabParser#close_par.
    def exitClose_par(self, ctx:matlabParser.Close_parContext):
        pass


    # Enter a parse tree produced by matlabParser#open_bracket.
    def enterOpen_bracket(self, ctx:matlabParser.Open_bracketContext):
        pass

    # Exit a parse tree produced by matlabParser#open_bracket.
    def exitOpen_bracket(self, ctx:matlabParser.Open_bracketContext):
        pass


    # Enter a parse tree produced by matlabParser#close_bracket.
    def enterClose_bracket(self, ctx:matlabParser.Close_bracketContext):
        pass

    # Exit a parse tree produced by matlabParser#close_bracket.
    def exitClose_bracket(self, ctx:matlabParser.Close_bracketContext):
        pass


    # Enter a parse tree produced by matlabParser#postfix_expression.
    def enterPostfix_expression(self, ctx:matlabParser.Postfix_expressionContext):
        pass

    # Exit a parse tree produced by matlabParser#postfix_expression.
    def exitPostfix_expression(self, ctx:matlabParser.Postfix_expressionContext):
        pass


    # Enter a parse tree produced by matlabParser#index_expression.
    def enterIndex_expression(self, ctx:matlabParser.Index_expressionContext):
        pass

    # Exit a parse tree produced by matlabParser#index_expression.
    def exitIndex_expression(self, ctx:matlabParser.Index_expressionContext):
        pass


    # Enter a parse tree produced by matlabParser#colon.
    def enterColon(self, ctx:matlabParser.ColonContext):
        pass

    # Exit a parse tree produced by matlabParser#colon.
    def exitColon(self, ctx:matlabParser.ColonContext):
        pass


    # Enter a parse tree produced by matlabParser#semicolon.
    def enterSemicolon(self, ctx:matlabParser.SemicolonContext):
        pass

    # Exit a parse tree produced by matlabParser#semicolon.
    def exitSemicolon(self, ctx:matlabParser.SemicolonContext):
        pass


    # Enter a parse tree produced by matlabParser#index_expression_list.
    def enterIndex_expression_list(self, ctx:matlabParser.Index_expression_listContext):
        pass

    # Exit a parse tree produced by matlabParser#index_expression_list.
    def exitIndex_expression_list(self, ctx:matlabParser.Index_expression_listContext):
        pass


    # Enter a parse tree produced by matlabParser#comma.
    def enterComma(self, ctx:matlabParser.CommaContext):
        pass

    # Exit a parse tree produced by matlabParser#comma.
    def exitComma(self, ctx:matlabParser.CommaContext):
        pass


    # Enter a parse tree produced by matlabParser#array_expression.
    def enterArray_expression(self, ctx:matlabParser.Array_expressionContext):
        pass

    # Exit a parse tree produced by matlabParser#array_expression.
    def exitArray_expression(self, ctx:matlabParser.Array_expressionContext):
        pass


    # Enter a parse tree produced by matlabParser#unary_expression.
    def enterUnary_expression(self, ctx:matlabParser.Unary_expressionContext):
        pass

    # Exit a parse tree produced by matlabParser#unary_expression.
    def exitUnary_expression(self, ctx:matlabParser.Unary_expressionContext):
        pass


    # Enter a parse tree produced by matlabParser#unary_operator.
    def enterUnary_operator(self, ctx:matlabParser.Unary_operatorContext):
        pass

    # Exit a parse tree produced by matlabParser#unary_operator.
    def exitUnary_operator(self, ctx:matlabParser.Unary_operatorContext):
        pass


    # Enter a parse tree produced by matlabParser#op_sum.
    def enterOp_sum(self, ctx:matlabParser.Op_sumContext):
        pass

    # Exit a parse tree produced by matlabParser#op_sum.
    def exitOp_sum(self, ctx:matlabParser.Op_sumContext):
        pass


    # Enter a parse tree produced by matlabParser#op_sub.
    def enterOp_sub(self, ctx:matlabParser.Op_subContext):
        pass

    # Exit a parse tree produced by matlabParser#op_sub.
    def exitOp_sub(self, ctx:matlabParser.Op_subContext):
        pass


    # Enter a parse tree produced by matlabParser#op_mul.
    def enterOp_mul(self, ctx:matlabParser.Op_mulContext):
        pass

    # Exit a parse tree produced by matlabParser#op_mul.
    def exitOp_mul(self, ctx:matlabParser.Op_mulContext):
        pass


    # Enter a parse tree produced by matlabParser#op_div.
    def enterOp_div(self, ctx:matlabParser.Op_divContext):
        pass

    # Exit a parse tree produced by matlabParser#op_div.
    def exitOp_div(self, ctx:matlabParser.Op_divContext):
        pass


    # Enter a parse tree produced by matlabParser#op_not.
    def enterOp_not(self, ctx:matlabParser.Op_notContext):
        pass

    # Exit a parse tree produced by matlabParser#op_not.
    def exitOp_not(self, ctx:matlabParser.Op_notContext):
        pass


    # Enter a parse tree produced by matlabParser#op_pow.
    def enterOp_pow(self, ctx:matlabParser.Op_powContext):
        pass

    # Exit a parse tree produced by matlabParser#op_pow.
    def exitOp_pow(self, ctx:matlabParser.Op_powContext):
        pass


    # Enter a parse tree produced by matlabParser#op_and.
    def enterOp_and(self, ctx:matlabParser.Op_andContext):
        pass

    # Exit a parse tree produced by matlabParser#op_and.
    def exitOp_and(self, ctx:matlabParser.Op_andContext):
        pass


    # Enter a parse tree produced by matlabParser#op_or.
    def enterOp_or(self, ctx:matlabParser.Op_orContext):
        pass

    # Exit a parse tree produced by matlabParser#op_or.
    def exitOp_or(self, ctx:matlabParser.Op_orContext):
        pass


    # Enter a parse tree produced by matlabParser#op_doble_backslash.
    def enterOp_doble_backslash(self, ctx:matlabParser.Op_doble_backslashContext):
        pass

    # Exit a parse tree produced by matlabParser#op_doble_backslash.
    def exitOp_doble_backslash(self, ctx:matlabParser.Op_doble_backslashContext):
        pass


    # Enter a parse tree produced by matlabParser#op_greater.
    def enterOp_greater(self, ctx:matlabParser.Op_greaterContext):
        pass

    # Exit a parse tree produced by matlabParser#op_greater.
    def exitOp_greater(self, ctx:matlabParser.Op_greaterContext):
        pass


    # Enter a parse tree produced by matlabParser#op_less.
    def enterOp_less(self, ctx:matlabParser.Op_lessContext):
        pass

    # Exit a parse tree produced by matlabParser#op_less.
    def exitOp_less(self, ctx:matlabParser.Op_lessContext):
        pass


    # Enter a parse tree produced by matlabParser#op_greater_equal.
    def enterOp_greater_equal(self, ctx:matlabParser.Op_greater_equalContext):
        pass

    # Exit a parse tree produced by matlabParser#op_greater_equal.
    def exitOp_greater_equal(self, ctx:matlabParser.Op_greater_equalContext):
        pass


    # Enter a parse tree produced by matlabParser#op_less_equal.
    def enterOp_less_equal(self, ctx:matlabParser.Op_less_equalContext):
        pass

    # Exit a parse tree produced by matlabParser#op_less_equal.
    def exitOp_less_equal(self, ctx:matlabParser.Op_less_equalContext):
        pass


    # Enter a parse tree produced by matlabParser#op_not_equal.
    def enterOp_not_equal(self, ctx:matlabParser.Op_not_equalContext):
        pass

    # Exit a parse tree produced by matlabParser#op_not_equal.
    def exitOp_not_equal(self, ctx:matlabParser.Op_not_equalContext):
        pass


    # Enter a parse tree produced by matlabParser#op_equal.
    def enterOp_equal(self, ctx:matlabParser.Op_equalContext):
        pass

    # Exit a parse tree produced by matlabParser#op_equal.
    def exitOp_equal(self, ctx:matlabParser.Op_equalContext):
        pass


    # Enter a parse tree produced by matlabParser#multiplicative_expression.
    def enterMultiplicative_expression(self, ctx:matlabParser.Multiplicative_expressionContext):
        pass

    # Exit a parse tree produced by matlabParser#multiplicative_expression.
    def exitMultiplicative_expression(self, ctx:matlabParser.Multiplicative_expressionContext):
        pass


    # Enter a parse tree produced by matlabParser#additive_expression.
    def enterAdditive_expression(self, ctx:matlabParser.Additive_expressionContext):
        pass

    # Exit a parse tree produced by matlabParser#additive_expression.
    def exitAdditive_expression(self, ctx:matlabParser.Additive_expressionContext):
        pass


    # Enter a parse tree produced by matlabParser#relational_expression.
    def enterRelational_expression(self, ctx:matlabParser.Relational_expressionContext):
        pass

    # Exit a parse tree produced by matlabParser#relational_expression.
    def exitRelational_expression(self, ctx:matlabParser.Relational_expressionContext):
        pass


    # Enter a parse tree produced by matlabParser#equality_expression.
    def enterEquality_expression(self, ctx:matlabParser.Equality_expressionContext):
        pass

    # Exit a parse tree produced by matlabParser#equality_expression.
    def exitEquality_expression(self, ctx:matlabParser.Equality_expressionContext):
        pass


    # Enter a parse tree produced by matlabParser#and_expression.
    def enterAnd_expression(self, ctx:matlabParser.And_expressionContext):
        pass

    # Exit a parse tree produced by matlabParser#and_expression.
    def exitAnd_expression(self, ctx:matlabParser.And_expressionContext):
        pass


    # Enter a parse tree produced by matlabParser#or_expression.
    def enterOr_expression(self, ctx:matlabParser.Or_expressionContext):
        pass

    # Exit a parse tree produced by matlabParser#or_expression.
    def exitOr_expression(self, ctx:matlabParser.Or_expressionContext):
        pass


    # Enter a parse tree produced by matlabParser#expression.
    def enterExpression(self, ctx:matlabParser.ExpressionContext):
        pass

    # Exit a parse tree produced by matlabParser#expression.
    def exitExpression(self, ctx:matlabParser.ExpressionContext):
        pass


    # Enter a parse tree produced by matlabParser#assignment_expression.
    def enterAssignment_expression(self, ctx:matlabParser.Assignment_expressionContext):
        pass

    # Exit a parse tree produced by matlabParser#assignment_expression.
    def exitAssignment_expression(self, ctx:matlabParser.Assignment_expressionContext):
        pass


    # Enter a parse tree produced by matlabParser#eostmt.
    def enterEostmt(self, ctx:matlabParser.EostmtContext):
        pass

    # Exit a parse tree produced by matlabParser#eostmt.
    def exitEostmt(self, ctx:matlabParser.EostmtContext):
        pass


    # Enter a parse tree produced by matlabParser#statement.
    def enterStatement(self, ctx:matlabParser.StatementContext):
        pass

    # Exit a parse tree produced by matlabParser#statement.
    def exitStatement(self, ctx:matlabParser.StatementContext):
        pass


    # Enter a parse tree produced by matlabParser#statement_list.
    def enterStatement_list(self, ctx:matlabParser.Statement_listContext):
        pass

    # Exit a parse tree produced by matlabParser#statement_list.
    def exitStatement_list(self, ctx:matlabParser.Statement_listContext):
        pass


    # Enter a parse tree produced by matlabParser#identifier_list.
    def enterIdentifier_list(self, ctx:matlabParser.Identifier_listContext):
        pass

    # Exit a parse tree produced by matlabParser#identifier_list.
    def exitIdentifier_list(self, ctx:matlabParser.Identifier_listContext):
        pass


    # Enter a parse tree produced by matlabParser#global_statement.
    def enterGlobal_statement(self, ctx:matlabParser.Global_statementContext):
        pass

    # Exit a parse tree produced by matlabParser#global_statement.
    def exitGlobal_statement(self, ctx:matlabParser.Global_statementContext):
        pass


    # Enter a parse tree produced by matlabParser#clear_statement.
    def enterClear_statement(self, ctx:matlabParser.Clear_statementContext):
        pass

    # Exit a parse tree produced by matlabParser#clear_statement.
    def exitClear_statement(self, ctx:matlabParser.Clear_statementContext):
        pass


    # Enter a parse tree produced by matlabParser#expression_statement.
    def enterExpression_statement(self, ctx:matlabParser.Expression_statementContext):
        pass

    # Exit a parse tree produced by matlabParser#expression_statement.
    def exitExpression_statement(self, ctx:matlabParser.Expression_statementContext):
        pass


    # Enter a parse tree produced by matlabParser#assignment_statement.
    def enterAssignment_statement(self, ctx:matlabParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by matlabParser#assignment_statement.
    def exitAssignment_statement(self, ctx:matlabParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by matlabParser#array_element.
    def enterArray_element(self, ctx:matlabParser.Array_elementContext):
        pass

    # Exit a parse tree produced by matlabParser#array_element.
    def exitArray_element(self, ctx:matlabParser.Array_elementContext):
        pass


    # Enter a parse tree produced by matlabParser#array_list.
    def enterArray_list(self, ctx:matlabParser.Array_listContext):
        pass

    # Exit a parse tree produced by matlabParser#array_list.
    def exitArray_list(self, ctx:matlabParser.Array_listContext):
        pass


    # Enter a parse tree produced by matlabParser#selection_statement.
    def enterSelection_statement(self, ctx:matlabParser.Selection_statementContext):
        pass

    # Exit a parse tree produced by matlabParser#selection_statement.
    def exitSelection_statement(self, ctx:matlabParser.Selection_statementContext):
        pass


    # Enter a parse tree produced by matlabParser#elseif_clause.
    def enterElseif_clause(self, ctx:matlabParser.Elseif_clauseContext):
        pass

    # Exit a parse tree produced by matlabParser#elseif_clause.
    def exitElseif_clause(self, ctx:matlabParser.Elseif_clauseContext):
        pass


    # Enter a parse tree produced by matlabParser#iteration_statement.
    def enterIteration_statement(self, ctx:matlabParser.Iteration_statementContext):
        pass

    # Exit a parse tree produced by matlabParser#iteration_statement.
    def exitIteration_statement(self, ctx:matlabParser.Iteration_statementContext):
        pass


    # Enter a parse tree produced by matlabParser#jump_statement.
    def enterJump_statement(self, ctx:matlabParser.Jump_statementContext):
        pass

    # Exit a parse tree produced by matlabParser#jump_statement.
    def exitJump_statement(self, ctx:matlabParser.Jump_statementContext):
        pass


    # Enter a parse tree produced by matlabParser#translation_unit.
    def enterTranslation_unit(self, ctx:matlabParser.Translation_unitContext):
        pass

    # Exit a parse tree produced by matlabParser#translation_unit.
    def exitTranslation_unit(self, ctx:matlabParser.Translation_unitContext):
        pass


    # Enter a parse tree produced by matlabParser#func_ident_list.
    def enterFunc_ident_list(self, ctx:matlabParser.Func_ident_listContext):
        pass

    # Exit a parse tree produced by matlabParser#func_ident_list.
    def exitFunc_ident_list(self, ctx:matlabParser.Func_ident_listContext):
        pass


    # Enter a parse tree produced by matlabParser#func_return_list.
    def enterFunc_return_list(self, ctx:matlabParser.Func_return_listContext):
        pass

    # Exit a parse tree produced by matlabParser#func_return_list.
    def exitFunc_return_list(self, ctx:matlabParser.Func_return_listContext):
        pass


    # Enter a parse tree produced by matlabParser#function_declare_lhs.
    def enterFunction_declare_lhs(self, ctx:matlabParser.Function_declare_lhsContext):
        pass

    # Exit a parse tree produced by matlabParser#function_declare_lhs.
    def exitFunction_declare_lhs(self, ctx:matlabParser.Function_declare_lhsContext):
        pass


    # Enter a parse tree produced by matlabParser#function_declare.
    def enterFunction_declare(self, ctx:matlabParser.Function_declareContext):
        pass

    # Exit a parse tree produced by matlabParser#function_declare.
    def exitFunction_declare(self, ctx:matlabParser.Function_declareContext):
        pass



del matlabParser