# CABALA FastAPI Project

API REST desenvolvida com FastAPI em Python.

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- Git

## 🚀 Instalação e Configuração

### Clonando o repositório
```bash
git clone [url-do-seu-repositorio]
cd [nome-do-diretorio]
```

### Configurando o Ambiente Virtual

#### Windows
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
venv\Scripts\activate
```

#### Linux/MacOS
```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate
```

### Instalando Dependências
```bash
pip install -r requirements.txt
```

## 🎯 Executando o Projeto

### Iniciando o servidor
```bash
uvicorn app.main:app --reload
```

O servidor estará rodando em: http://localhost:8000

## 📚 Documentação da API

Após iniciar o servidor, você pode acessar:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🛣️ Rotas Disponíveis

- `GET /`: Retorna mensagem de boas-vindas
- `GET /hello/{nome}`: Retorna uma saudação personalizada

## 💻 Exemplos de Uso

### Rota de Boas-vindas
```bash
curl http://localhost:8000/
```

### Rota de Saudação
```bash
curl http://localhost:8000/hello/seu-nome
```

## 🛠️ Tecnologias Utilizadas

- FastAPI
- Uvicorn
- Pydantic

## ⚙️ Variáveis de Ambiente

Por padrão, o servidor roda em:
- Host: localhost
- Porta: 8000

Para alterar estas configurações, você pode executar:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 80 --reload
```

## 🤝 Contribuindo

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Faça o Commit de suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Faça o Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🆘 Suporte

Em caso de dúvidas, por favor, abra uma issue no repositório.

AXE
