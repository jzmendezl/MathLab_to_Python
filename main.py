from antlr4 import *
from fastapi import FastAPI
from Models.ModelInput import TextInput
from gen.matlabLexer import matlabLexer
from gen.matlabParser import matlabParser
from Function.Translate import Translate
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/translate")
async def translate(text_input: TextInput):
    lexer = matlabLexer(InputStream(text_input.text))
    tokens = CommonTokenStream(lexer)
    parser = matlabParser(tokens)
    tree = parser.file_()
    lis = Translate()

    walker = ParseTreeWalker()
    walker.walk(lis, tree)
    return {"message": f"{lis.returnTranslatedCode()}"}
