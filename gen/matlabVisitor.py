# Generated from C:/Users/Kira/PycharmProjects/MathLab_to_Python/grammar/matlab.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .matlabParser import matlabParser
else:
    from matlabParser import matlabParser

# This class defines a complete generic visitor for a parse tree produced by matlabParser.

class matlabVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by matlabParser#file_.
    def visitFile_(self, ctx:matlabParser.File_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#primary_expression.
    def visitPrimary_expression(self, ctx:matlabParser.Primary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#open_par.
    def visitOpen_par(self, ctx:matlabParser.Open_parContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#close_par.
    def visitClose_par(self, ctx:matlabParser.Close_parContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#open_bracket.
    def visitOpen_bracket(self, ctx:matlabParser.Open_bracketContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#close_bracket.
    def visitClose_bracket(self, ctx:matlabParser.Close_bracketContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#postfix_expression.
    def visitPostfix_expression(self, ctx:matlabParser.Postfix_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#index_expression.
    def visitIndex_expression(self, ctx:matlabParser.Index_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#colon.
    def visitColon(self, ctx:matlabParser.ColonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#semicolon.
    def visitSemicolon(self, ctx:matlabParser.SemicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#index_expression_list.
    def visitIndex_expression_list(self, ctx:matlabParser.Index_expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#comma.
    def visitComma(self, ctx:matlabParser.CommaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#array_expression.
    def visitArray_expression(self, ctx:matlabParser.Array_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#unary_expression.
    def visitUnary_expression(self, ctx:matlabParser.Unary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#unary_operator.
    def visitUnary_operator(self, ctx:matlabParser.Unary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#op_sum.
    def visitOp_sum(self, ctx:matlabParser.Op_sumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#op_sub.
    def visitOp_sub(self, ctx:matlabParser.Op_subContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#op_mul.
    def visitOp_mul(self, ctx:matlabParser.Op_mulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#op_div.
    def visitOp_div(self, ctx:matlabParser.Op_divContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#op_not.
    def visitOp_not(self, ctx:matlabParser.Op_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#op_pow.
    def visitOp_pow(self, ctx:matlabParser.Op_powContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#op_and.
    def visitOp_and(self, ctx:matlabParser.Op_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#op_or.
    def visitOp_or(self, ctx:matlabParser.Op_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#op_doble_backslash.
    def visitOp_doble_backslash(self, ctx:matlabParser.Op_doble_backslashContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#op_greater.
    def visitOp_greater(self, ctx:matlabParser.Op_greaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#op_less.
    def visitOp_less(self, ctx:matlabParser.Op_lessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#op_greater_equal.
    def visitOp_greater_equal(self, ctx:matlabParser.Op_greater_equalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#op_less_equal.
    def visitOp_less_equal(self, ctx:matlabParser.Op_less_equalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#op_not_equal.
    def visitOp_not_equal(self, ctx:matlabParser.Op_not_equalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#op_equal.
    def visitOp_equal(self, ctx:matlabParser.Op_equalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#multiplicative_expression.
    def visitMultiplicative_expression(self, ctx:matlabParser.Multiplicative_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#additive_expression.
    def visitAdditive_expression(self, ctx:matlabParser.Additive_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#relational_expression.
    def visitRelational_expression(self, ctx:matlabParser.Relational_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#equality_expression.
    def visitEquality_expression(self, ctx:matlabParser.Equality_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#and_expression.
    def visitAnd_expression(self, ctx:matlabParser.And_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#or_expression.
    def visitOr_expression(self, ctx:matlabParser.Or_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#expression.
    def visitExpression(self, ctx:matlabParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#assignment_expression.
    def visitAssignment_expression(self, ctx:matlabParser.Assignment_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#eostmt.
    def visitEostmt(self, ctx:matlabParser.EostmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#statement.
    def visitStatement(self, ctx:matlabParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#statement_list.
    def visitStatement_list(self, ctx:matlabParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#identifier_list.
    def visitIdentifier_list(self, ctx:matlabParser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#global_statement.
    def visitGlobal_statement(self, ctx:matlabParser.Global_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#clear_statement.
    def visitClear_statement(self, ctx:matlabParser.Clear_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#expression_statement.
    def visitExpression_statement(self, ctx:matlabParser.Expression_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#assignment_statement.
    def visitAssignment_statement(self, ctx:matlabParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#array_element.
    def visitArray_element(self, ctx:matlabParser.Array_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#array_list.
    def visitArray_list(self, ctx:matlabParser.Array_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#selection_statement.
    def visitSelection_statement(self, ctx:matlabParser.Selection_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#elseif_clause.
    def visitElseif_clause(self, ctx:matlabParser.Elseif_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#iteration_statement.
    def visitIteration_statement(self, ctx:matlabParser.Iteration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#jump_statement.
    def visitJump_statement(self, ctx:matlabParser.Jump_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#translation_unit.
    def visitTranslation_unit(self, ctx:matlabParser.Translation_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#func_ident_list.
    def visitFunc_ident_list(self, ctx:matlabParser.Func_ident_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#func_return_list.
    def visitFunc_return_list(self, ctx:matlabParser.Func_return_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#function_declare_lhs.
    def visitFunction_declare_lhs(self, ctx:matlabParser.Function_declare_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#function_declare.
    def visitFunction_declare(self, ctx:matlabParser.Function_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#break.
    def visitBreak(self, ctx:matlabParser.BreakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#end.
    def visitEnd(self, ctx:matlabParser.EndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#if.
    def visitIf(self, ctx:matlabParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#else.
    def visitElse(self, ctx:matlabParser.ElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#elseif.
    def visitElseif(self, ctx:matlabParser.ElseifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#eq_op.
    def visitEq_op(self, ctx:matlabParser.Eq_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#ne_op.
    def visitNe_op(self, ctx:matlabParser.Ne_opContext):
        return self.visitChildren(ctx)



del matlabParser