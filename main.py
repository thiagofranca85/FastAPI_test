from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{id}")
def read_item(id: int, idade: int, nome: Union[str, None] = None):
    return {"id": id, "idade": idade, "nome": nome}