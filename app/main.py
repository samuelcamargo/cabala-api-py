from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.cabala_controller import router as cabala_router

app = FastAPI(
    title="CABALA API",
    description="API para cálculos de CABALA",
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

# Incluindo as rotas
app.include_router(cabala_router, tags=["Cabala"]) 