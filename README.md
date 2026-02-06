# Codeflix Catalog Admin - Python

## Tecnologias

- Python 3.x
- Django 6.0.1
- Django REST Framework 3.16.1
- SQLite3
- Pytest 8.4.2

## Como Executar o Projeto

### Pré-requisitos

1. **Python 3.x** instalado na sua máquina
2. **Postman** para testar a API - [Download Postman](https://www.postman.com/downloads/)

### Instalação e Configuração

1. **Clone o repositório:**
   ```bash
   git clone git@github.com:flvSantos15/codeflix-catalog-admin-python.git
   cd codeflix-catalog-admin-python
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate  # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requeriments.txt
   ```

4. **Execute as migrações do banco de dados:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

O servidor estará rodando em: `http://localhost:8000`

## Documentação da API - Categories

A API disponibiliza endpoints para gerenciamento de categorias através do path `/api/categories/`.

### Model de Dados

**Category:**
- `id`: UUID (gerado automaticamente)
- `name`: String (máximo 255 caracteres, obrigatório)
- `description`: Text (opcional)
- `is_active`: Boolean (default: true)

### Endpoints Disponíveis

#### 1. Listar Todas as Categorias
- **Método:** `GET`
- **URL:** `http://localhost:8000/api/categories/`
- **Headers:** 
  - `Content-Type: application/json`
- **Resposta:** Array com todas as categorias

#### 2. Obter Categoria Específica
- **Método:** `GET`
- **URL:** `http://localhost:8000/api/categories/{id}/`
- **Parâmetros:**
  - `id`: UUID da categoria (path parameter)
- **Headers:** 
  - `Content-Type: application/json`
- **Resposta:** Objeto da categoria específica

#### 3. Criar Nova Categoria
- **Método:** `POST`
- **URL:** `http://localhost:8000/api/categories/`
- **Headers:** 
  - `Content-Type: application/json`
- **Body (JSON):**
  ```json
  {
    "name": "Nome da Categoria",
    "description": "Descrição detalhada da categoria",
    "is_active": true
  }
  ```
- **Campos obrigatórios:** `name`
- **Resposta:** UUID da categoria criada

#### 4. Atualizar Categoria (Completo)
- **Método:** `PUT`
- **URL:** `http://localhost:8000/api/categories/{id}/`
- **Parâmetros:**
  - `id`: UUID da categoria (path parameter)
- **Headers:** 
  - `Content-Type: application/json`
- **Body (JSON):**
  ```json
  {
    "name": "Nome Atualizado",
    "description": "Descrição atualizada",
    "is_active": false
  }
  ```
- **Resposta:** 204 No Content

#### 5. Atualizar Categoria (Parcial)
- **Método:** `PATCH`
- **URL:** `http://localhost:8000/api/categories/{id}/`
- **Parâmetros:**
  - `id`: UUID da categoria (path parameter)
- **Headers:** 
  - `Content-Type: application/json`
- **Body (JSON):**
  ```json
  {
    "name": "Apenas o nome atualizado"
  }
  ```
- **Resposta:** 204 No Content

#### 6. Excluir Categoria
- **Método:** `DELETE`
- **URL:** `http://localhost:8000/api/categories/{id}/`
- **Parâmetros:**
  - `id`: UUID da categoria (path parameter)
- **Headers:** 
  - `Content-Type: application/json`
- **Resposta:** 204 No Content

## Como Usar com Postman

### Configuração Inicial

1. **Abra o Postman** e crie uma nova Collection chamada "Codeflix Catalog"
2. **Configure a Collection:**
   - Base URL: `http://localhost:8000`
   - Header padrão: `Content-Type: application/json`

### Exemplos de Requisições

#### Exemplo 1: Criar Categoria
1. **Method:** POST
2. **URL:** `{{baseUrl}}/api/categories/`
3. **Body → raw → JSON:**
   ```json
   {
     "name": "Filmes de Ação",
     "description": "Filmes com muita ação e aventura",
     "is_active": true
   }
   ```
4. **Send**

#### Exemplo 2: Listar Categorias
1. **Method:** GET
2. **URL:** `{{baseUrl}}/api/categories/`
3. **Send**

#### Exemplo 3: Atualizar Categoria
1. **Method:** PATCH
2. **URL:** `{{baseUrl}}/api/categories/{UUID_DA_CATEGORIA}/`
3. **Body → raw → JSON:**
   ```json
   {
     "name": "Filmes de Ação e Aventura"
   }
   ```
4. **Send**

### Dicas Importantes

- **IDs:** As categorias usam UUID como identificador. Copie o ID retornado na criação para usar nas outras operações
- **Validação:** O campo `name` é obrigatório e não pode estar em branco
- **Status HTTP:** 
  - `200 OK`: Para listagens e buscas
  - `201 Created`: Para criação bem-sucedida
  - `204 No Content`: Para atualizações e exclusões
  - `404 Not Found`: Quando a categoria não existe
  - `400 Bad Request`: Para dados inválidos

## Testes

Para executar os testes da aplicação:

```bash
pytest
```

## Admin do Django

Acesse o painel administrativo do Django em:
- **URL:** `http://localhost:8000/admin/`
- **Crie um superusuário** para acessar:
  ```bash
  python manage.py createsuperuser
  ```
