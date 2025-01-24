from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Minha API",
    description="Descrição da minha API",
    version="1.0.0"
)

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"mensagem": "Bem-vindo à minha API!"}

@app.get("/hello/{nome}")
async def hello(nome: str):
    return {"mensagem": f"Olá, {nome}!"} 