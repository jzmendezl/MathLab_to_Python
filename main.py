from antlr4 import *
from fastapi import FastAPI
from Models.ModelInput import TextInput
from gen.matlabLexer import matlabLexer
from gen.matlabParser import matlabParser
from Function.Translate import Translate



app = FastAPI()
BUFFER = ""

@app.get("/")
async def root():
  return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
  return {"message": f"Hello {name}"}

@app.post("/trasnlate")
async def trasnlate(text_input: TextInput):
  lexer = matlabLexer(InputStream(text_input.text))
  tokens = CommonTokenStream(lexer)
  parser = matlabParser(tokens)
  tree = parser.file_()
  lis = Translate()

  walker = ParseTreeWalker()
  walker.walk(lis, tree)
  return {"message": f" recived {lis.returnTranslatedCode()}"}
