# CABALA FastAPI Project

API REST desenvolvida com FastAPI em Python para cálculos de Cabala.

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- Git

## 🚀 Instalação e Configuração

### Clonando o repositório
```bash
git clone https://github.com/samuelcamargo/cabala-api-py
cd cabala-api-py
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

## 🛣️ Endpoints Disponíveis

### 1. Rota Principal
- **GET /** 
  - Retorna mensagem de boas-vindas
  - Exemplo: `curl http://localhost:8000/`

### 2. Cálculo de Cabala
- **GET /cabala/{data}**
  - Calcula os números da Cabala baseado na data fornecida
  - Aceita datas nos formatos: DD/MM/AAAA ou DD-MM-AAAA
  - Exemplo: `curl http://localhost:8000/cabala/10-02-1989`
  - Retorno:
    ```json
    {
      "data": "10/02/1989",
      "dinheiro": {"numero": 5, "orixa": "Oxum"},
      "pessoas": {"numero": 8, "orixa": "Ejionilê"},
      "coracao": {"numero": 13, "orixa": "Nanã"},
      "racional": {"numero": 7, "orixa": "Obaluaê"},
      "destino": {"numero": 11, "orixa": "Owonrin"},
      "fe": {"numero": 3, "orixa": "Ogum"}
    }
    ```

## 🏗️ Arquitetura do Projeto

O projeto segue os princípios da Clean Architecture, organizando o código em camadas bem definidas:

```
app/
├── __init__.py
├── main.py                 # Configuração principal da aplicação
├── controllers/            # Controladores da API
│   ├── __init__.py
│   └── cabala_controller.py
├── use_cases/             # Regras de negócio da aplicação
│   ├── __init__.py
│   └── calcular_cabala.py
├── entities/              # Entidades do domínio
│   ├── __init__.py
│   └── orixa.py
├── repositories/          # Camada de acesso a dados
│   ├── __init__.py
│   └── orixa_repository.py
└── schemas/              # Schemas de validação e serialização
    ├── __init__.py
    └── cabala_schema.py
```

### Descrição das Camadas

1. **Controllers (controllers/)**
   - Responsável por receber as requisições HTTP
   - Define os endpoints da API
   - Gerencia dependências usando FastAPI

2. **Use Cases (use_cases/)**
   - Contém a lógica de negócio da aplicação
   - Implementa os casos de uso específicos
   - Realiza os cálculos da Cabala

3. **Entities (entities/)**
   - Define as entidades principais do domínio
   - Representa os objetos fundamentais (ex: Orixá)

4. **Repositories (repositories/)**
   - Gerencia o acesso aos dados
   - Fornece uma interface para acessar os Orixás
   - Pode ser expandido para usar banco de dados

5. **Schemas (schemas/)**
   - Define os modelos de dados para request/response
   - Realiza validação dos dados de entrada
   - Garante a tipagem correta dos dados

## 🛠️ Tecnologias Utilizadas

- FastAPI: Framework web moderno e rápido
- Pydantic: Validação de dados e serialização
- Uvicorn: Servidor ASGI de alta performance

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
