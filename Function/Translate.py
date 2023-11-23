from gen.matlabLexer import matlabLexer
from gen.matlabParser import matlabParser
from gen.matlabVisitor import matlabVisitor
from gen.matlabListener import matlabListener

from antlr4 import *

class Translate(matlabListener):

  def __init__(self):
    self.translatedCode = "HOLA MUNDO"
  def returnTranslatedCode(self):
    return self.translatedCode