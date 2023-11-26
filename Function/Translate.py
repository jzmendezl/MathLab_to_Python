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
  ifFlag = False
  elseFlag = False
  arrayListFlag = False
  arrayElementFlag = False
  closeBracketFlag = False
  funtionFlag = False
  anyFlag = False
  posArrayFlag = False
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

  def enterEostmt(self, ctx:matlabParser.EostmtContext):
    if self.ifFlag:
      self.program += ":"
      self.program += "\n"
      self.indent += 1
      self.ifFlag = False

    if self.forFlag:
      self.program += ":"
      self.program += "\n"
      self.indent += 1
      self.forFlag = False






  def enterGlobal_statement(self, ctx:matlabParser.Global_statementContext):
    self.program += self.indentation() + "global "

  def enterIdentifier_list(self, ctx:matlabParser.Identifier_listContext):
    self.program += self.indentation() + ctx.getText()

  def enterComma(self, ctx:matlabParser.CommaContext):
    if self.posArrayFlag:
      self.program += " : "
      self.posArrayFlag = False
    else:
      self.program += ", "


  def enterColon(self, ctx:matlabParser.ColonContext):
    self.program += ":"

  def enterSemicolon(self, ctx:matlabParser.SemicolonContext):
    if not self.arrayElementFlag:
      self.program += "\n"

  def entertClear_statement(self, ctx:matlabParser.Clear_statementContext):
    self.program += self.indentation() + "clear "

  def enterAssignment_statement(self, ctx:matlabParser.Assignment_statementContext):
    self.program += self.indentation()

  def enterPrimary_expression(self, ctx:matlabParser.Primary_expressionContext):
    if ctx.IDENTIFIER():
      # print(ctx.IDENTIFIER().getText())
      if ctx.IDENTIFIER().getText() in self.vars:
        self.program += self.vars[ctx.IDENTIFIER().getText()]
      else:
        if ctx.IDENTIFIER().getText() == "any":
          self.anyFlag = True
        self.program += ctx.IDENTIFIER().getText()
    if ctx.CONSTANT():
      self.program += ctx.CONSTANT().getText()
    if ctx.STRING_LITERAL():
      self.program += ctx.STRING_LITERAL().getText()

    if ctx.getChildCount() > 2 and ctx.getChild(2).getText() == "]":
      self.arrayElementFlag = True

  def enterOpen_par(self, ctx:matlabParser.Open_parContext):
    if self.arrayListFlag:
      pass
    else:
      self.program += "("

  def enterClose_par(self, ctx:matlabParser.Close_parContext):
    if self.closeBracketFlag:
      self.program += "]"
      self.closeBracketFlag = False
    elif self.anyFlag:
      # self.program += ""
      self.anyFlag = False
    else:
      self.program += ")"

  def enterOpen_bracket(self, ctx:matlabParser.Open_bracketContext):
    self.program += "np.array([["


  def enterClose_bracket(self, ctx:matlabParser.Close_bracketContext):
    self.program += "]"
    if self.arrayElementFlag:
      self.program += "])"
      self.arrayElementFlag = False

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
    if self.forFlag:
      self.program += " in "

    else:
      self.program += " = "



  def enterEq_op(self, ctx:matlabParser.Eq_opContext):
    if self.anyFlag:
        print("ANY")
        self.program += ") == "
        # self.anyFlag = False
    else:
      self.program += " == "

  def enterNe_op(self, ctx:matlabParser.Ne_opContext):
    self.program += " != "

  def enterArray_expression(self, ctx:matlabParser.Array_expressionContext):
    if ctx.IDENTIFIER():
      if ctx.IDENTIFIER().getText() in self.vars:
        self.program += self.indentation() + self.vars[ctx.IDENTIFIER().getText()]
        self.funtionFlag = True
      else:
        self.program += ctx.IDENTIFIER().getText()

    if ctx.getChild(1).getText() == "(" and not self.funtionFlag:
      self.arrayListFlag = True
      self.program += "["

    if ctx.getChild(3).getText() == ")" and not self.funtionFlag:
      self.closeBracketFlag = True


  def enterArray_element(self, ctx:matlabParser.Array_elementContext):
    if ctx.getChild(-1).getText() == ";":
      self.program += "], ["
      self.arrayElementFlag = True
    else:
      if self.program[-1] == "[":
        self.program += ""
      else:
        self.program += ", "

  def enterIf(self, ctx:matlabParser.IfContext):
    self.program += self.indentation() + "if "
    self.ifFlag = True

  def enterElse(self, ctx:matlabParser.ElseContext):
    self.indent -= 1
    self.program += "\n"
    self.program += self.indentation() + "else:"
    self.program += "\n"
    self.indent += 1
    self.elseFlag = True



  def enterElseif(self, ctx:matlabParser.ElseifContext):
    self.indent -= 1
    self.program += "\n"
    self.program += self.indentation() + "elif "
    self.ifFlag = True
  def enterIteration_statement(self, ctx:matlabParser.Iteration_statementContext):
    if ctx.WHILE():
      self.program += "\n"
      self.program += self.indentation() + "while "
      self.whileFlag = True
    if ctx.FOR():
      self.program += self.indentation() + "for "
      self.forFlag = True

    if ctx.IDENTIFIER():
      self.program += ctx.IDENTIFIER().getText()

  def exitIteration_statement(self, ctx:matlabParser.Iteration_statementContext):
    if ctx.end():
      self.whileFlag = False
      self.indent -= 1
      self.program += "\n"

  def enterBreak(self, ctx:matlabParser.BreakContext):
    self.program += self.indentation() + "break"
    self.program += "\n"
    self.indent -= 1

  def enterEnd(self, ctx:matlabParser.EndContext):
    if self.ifFlag:
      print("END IF")

      # self.program += "\n"
      self.indent -= 1
      self.ifFlag = False

    if self.elseFlag:
      self.indent -= 1
      self.elseFlag = False


  def enterIndex_expression_list(self, ctx:matlabParser.Index_expression_listContext):
    if ctx.comma():
      self.posArrayFlag = True




  def exitExpression(self, ctx:matlabParser.ExpressionContext):
    if self.whileFlag:
      self.program += ":"
      self.program += "\n"
      self.indent += 1
      self.whileFlag = False



  def returnTranslatedCode(self):
    return self.program