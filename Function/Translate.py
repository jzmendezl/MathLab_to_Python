from gen.matlabLexer import matlabLexer
from gen.matlabParser import matlabParser
from gen.matlabVisitor import matlabVisitor
from gen.matlabListener import matlabListener

from antlr4 import *

class Translate(matlabListener):
  program = ""
  indent = 0
  vars = {
    "pi": "np.pi",
    "disp": "print",
    "inf": "np.inf",
    "NaN": "np.nan",
    "eye": "np.eye",
    "zeros": "np.zeros",
    "ones": "np.ones",
    "rand": "np.random.rand",
    "randn": "np.random.randn",
    "size": "np.size",
    "length": "np.length",
    "num2str": "str",
  }
  opr = dict()
  whileFlag = False
  forFlag = False
  arrayListFlag = False
  deep = []

  def indentation(self):
    return self.indent*"\t"

  def enterFile_(self, ctx:matlabParser.File_Context):
    self.program += "import sys\n"
    self.program += "import numpy as np\n"
    self.program += "\n"
    self.program += "def main():\n"
    self.indent += 1

  def exitFile_(self, ctx:matlabParser.File_Context):
    self.program += "\n\n"
    self.program += "if __name__ == \"__main__\":\n"
    self.program += "\tmain()\n"

    print(self.program)
  def enterGlobal_statement(self, ctx:matlabParser.Global_statementContext):
    self.program += self.indentation() + "global "

  def enterIdentifier_list(self, ctx:matlabParser.Identifier_listContext):
    self.program += self.indentation() + ctx.getText()

  def enterComma(self, ctx:matlabParser.CommaContext):
    self.program += ", "

  def enterColon(self, ctx:matlabParser.ColonContext):
    self.program += ":"

  def enterSemicolon(self, ctx:matlabParser.SemicolonContext):
    self.program += "\n"

  def entertClear_statement(self, ctx:matlabParser.Clear_statementContext):
    self.program += self.indentation() + "clear "

  def enterAssignment_statement(self, ctx:matlabParser.Assignment_statementContext):
    self.program += self.indentation()

  def enterPrimary_expression(self, ctx:matlabParser.Primary_expressionContext):
    if ctx.IDENTIFIER():
      if ctx.IDENTIFIER().getText() in self.vars:
        if self.arrayListFlag:
          self.program += ", "
        self.program += self.vars[ctx.IDENTIFIER().getText()]
      else:
        self.program += ctx.IDENTIFIER().getText()
    if ctx.CONSTANT():
      self.program += ctx.CONSTANT().getText()
      if self.arrayListFlag:
        self.program += ", "
    if ctx.STRING_LITERAL():
      self.program += ctx.STRING_LITERAL().getText()

  def enterOpen_par(self, ctx:matlabParser.Open_parContext):
    self.program += "("

  def enterClose_par(self, ctx:matlabParser.Close_parContext):
    self.program += ")"

  def enterOpen_bracket(self, ctx:matlabParser.Open_bracketContext):
    self.program += "["

  def enterClose_bracket(self, ctx:matlabParser.Close_bracketContext):
    self.program += "]"

  def enterOp_and(self, ctx:matlabParser.Op_andContext):
    self.program += " and "

  def enterOp_or(self, ctx:matlabParser.Op_orContext):
    self.program += " or "

  def enterOp_not(self, ctx:matlabParser.Op_notContext):
    self.program += " not "

  def enterOp_sum(self, ctx:matlabParser.Op_sumContext):
    self.program += " + "

  def enterOp_sub(self, ctx:matlabParser.Op_subContext):
    self.program += " - "

  def enterOp_mul(self, ctx:matlabParser.Op_mulContext):
    self.program += " * "

  def enterOp_div(self, ctx:matlabParser.Op_divContext):
    self.program += " / "

  def enterOp_pow(self, ctx:matlabParser.Op_powContext):
    self.program += " ** "

  def enterOp_less(self, ctx:matlabParser.Op_lessContext):
    self.program += " < "

  def enterOp_less_equal(self, ctx:matlabParser.Op_less_equalContext):
    self.program += " <= "

  def enterOp_greater(self, ctx:matlabParser.Op_greaterContext):
    self.program += " > "

  def enterOp_greater_equal(self, ctx:matlabParser.Op_greater_equalContext):
    self.program += " >= "

  def enterOp_equal(self, ctx:matlabParser.Op_equalContext):
    self.program += " = "

  def enterArray_expression(self, ctx:matlabParser.Array_expressionContext):
    self.program += self.indentation()
    if ctx.IDENTIFIER():
      if ctx.IDENTIFIER().getText() in self.vars:
        if self.arrayListFlag:
          self.program += ", "
        self.program += self.vars[ctx.IDENTIFIER().getText()]
      else:
        self.program += ctx.IDENTIFIER().getText()

  def enterArray_list(self, ctx:matlabParser.Array_listContext):
    self.arrayListFlag = True
    self.deep.append(ctx.depth())

  def exitArray_list(self, ctx:matlabParser.Array_listContext):
    if ctx.depth() == min(self.deep):
      self.arrayListFlag = False


  def enterSelection_statement(self, ctx:matlabParser.Selection_statementContext):
    if ctx.IF():
      self.program += self.indentation() + "if "
    if ctx.ELSE():
      self.program += self.indentation() + "else "

    if ctx.END():
      self.indent -= 1
      self.program += "\n"

  def enterElseif_clause(self, ctx:matlabParser.Elseif_clauseContext):
    self.program += self.indentation() + "elif "

  def enterIteration_statement(self, ctx:matlabParser.Iteration_statementContext):
    if ctx.WHILE():
      self.program += "\n"
      self.program += self.indentation() + "while "
      self.whileFlag = True
    if ctx.FOR():
      self.program += self.indentation() + "for "

  def exitIteration_statement(self, ctx:matlabParser.Iteration_statementContext):
    if ctx.END():
      self.whileFlag = False
      self.indent -= 1
      self.program += "\n"





  def exitExpression(self, ctx:matlabParser.ExpressionContext):
    if self.whileFlag:
      self.program += ":"
      self.program += "\n"
      self.indent += 1
      self.whileFlag = False

    if self.forFlag:
      self.program += ":"
      self.forFlag = False







  def returnTranslatedCode(self):
    return self.program