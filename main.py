from antlr4 import *
from fastapi import FastAPI
from Models.ModelInput import TextInput
from gen.matlabLexer import matlabLexer
from gen.matlabParser import matlabParser
from Function.Translate import Translate
from fastapi import Request


app = FastAPI()


@app.get("/")
async def root():
  return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
  return {"message": f"Hello {name}"}

@app.post("/trasnlate")
async def trasnlate(text_input: TextInput):
  print(text_input.text)
  lexer = matlabLexer(text_input.text)
  stream = CommonTokenStream(lexer)
  parser = matlabParser(stream)
  tree = parser.file_()

  walker = ParseTreeWalker()
  listener = Translate()
  walker.walk(listener, tree)

  return {"message": f"{listener.returnTranslatedCode()}"}

# def read_input(arg):
#   if len(sys.argv) > 1:
#     file_input = open(sys.argv[1], "r", encoding="utf8")
#     code = file_input.readlines()
#     return InputStream(''.join(code))
#   else:
#     code = sys.stdin.readlines()
#     return InputStream(''.join(code))