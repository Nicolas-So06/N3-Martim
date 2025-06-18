from fastapi import APIRouter, HTTPException, Query
from src.models.pessoa_model import Pessoa
import src.repositories.pessoa_repository as pessoa_repo

routes = APIRouter()

@routes.post("/cadastrar")
def cadastrar_pessoa(pessoa: Pessoa):
    try:
        pessoa_repo.create_pessoa(pessoa.model_dump())
        return {"mensagem": "Pessoa cadastrada com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@routes.get("/pesquisar_nome")
def pesquisar_por_nome(nome: str = Query(...)):
    return pessoa_repo.find_pessoa_by_nome(nome)

@routes.get("/pesquisar_rua")
def pesquisar_por_rua(rua: str = Query(...)):
    return pessoa_repo.find_pessoa_by_rua(rua)

@routes.get("/pesquisar_filhos")
def pesquisar_por_filho(nome_filho: str = Query(...)):
    return pessoa_repo.find_pessoa_by_filho(nome_filho)