from fastapi import FastAPI
from src.routers import pessoa_routes

app = FastAPI(
    title="API de Pessoas",
    description="Uma API para cadastrar e pesquisar pessoas, seus endereços e filhos.",
    version="1.0.0"
)

app.include_router(pessoa_routes.routes, tags=["Pessoas"])

@app.get("/")
def read_root():
    return {"API": "Bem-vindo à API clients!"}
