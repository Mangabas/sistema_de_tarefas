# Sistema de Tarefas 

Sistema completo de gerenciamento de tarefas (To-Do List) desenvolvido com Django, permitindo criar, editar, visualizar e excluir tarefas com controle de usuários.

##  Sobre o Projeto

Este é um sistema web de gerenciamento de tarefas que permite aos usuários:
- Criar suas próprias tarefas com título e descrição
- Marcar tarefas como concluídas ou pendentes
- Editar e excluir tarefas existentes
- Visualizar detalhes completos de cada tarefa
- Sistema de autenticação com registro e login de usuários
- Cada usuário visualiza apenas suas próprias tarefas
- Paginação automática (5 tarefas por página)
- Interface responsiva e amigável

##  Tecnologias Utilizadas

- **Django 5.2.7** - Framework web Python
- **PostgreSQL** - Banco de dados (configurado via variáveis de ambiente)
- **Python-decouple** - Gerenciamento de variáveis de ambiente
- **HTML/CSS** - Interface do usuário
- **Class-Based Views** - Para operações CRUD

##  Estrutura do Projeto

```
sistema_tarefas/
├── manage.py
├── sistema_tarefas/         # Configurações do projeto
└── tasks/                   # Aplicação de tarefas
    ├── templates/           # Templates HTML
    │   └── registration/    # Login e Registro
    ├── static/
    │   └── css/             # Estilização de Templates
    └── migrations/          # Migrações do banco
```

##  Pré-requisitos

- **Python 3.8+** instalado
- **PostgreSQL** instalado e rodando (ou SQLite para testes)
- **pip** (gerenciador de pacotes Python)

## 🔧 Configuração e Instalação

### 1. Instalar Dependências

```bash
pip install django
pip install python-decouple
pip install psycopg2
pip install psycopg2-binary
```

### 2. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
SECRET_KEY=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```

### 3. Criar o Banco de Dados

Execute as migrações para criar as tabelas:

```bash
python manage.py migrate
```

### 5. Criar um Superusuário (Administrador)

```bash
python manage.py createsuperuser
```

Siga as instruções no terminal para definir:
- Nome de usuário
- E-mail (opcional)
- Senha

### 6. Rodar o Servidor de Desenvolvimento

```bash
python manage.py runserver
```

O sistema estará disponível em: **http://127.0.0.1:8000/**

##  Credenciais de Teste

Após criar o superusuário, você pode usar essas credenciais para acessar o sistema.

**Exemplo de superusuário:**
- **Usuário:** `admin`
- **Senha:** `admin`

##  Funcionalidades Detalhadas

### Autenticação de Usuários
- **Registro:** Novos usuários podem se cadastrar em `/register/`
- **Login:** Acesso em `/login/`
- **Logout:** Sair do sistema em `/logout/`
- **Proteção:** Todas as páginas de tarefas exigem autenticação

### Gerenciamento de Tarefas

| Funcionalidade | URL | Método | Descrição |
|---------------|-----|--------|-----------|
| Listar tarefas | `/` | GET | Lista todas as tarefas do usuário logado |
| Criar tarefa | `/task/create/` | GET/POST | Formulário para criar nova tarefa |
| Detalhes | `/task/<id>/` | GET | Visualiza detalhes de uma tarefa |
| Editar | `/task/<id>/update/` | GET/POST | Edita uma tarefa existente |
| Excluir | `/task/<id>/delete/` | POST | Remove uma tarefa |
| Alternar status | `/task/<id>/toggle/` | POST | Marca como concluída/pendente |

### Modelo de Dados (Task)

```python
class Task(models.Model):
    title = CharField          # Título da tarefa (único, máx. 200 caracteres)
    description = TextField    # Descrição detalhada (opcional)
    completed = BooleanField   # Status: concluída ou pendente
    user = ForeignKey          # Usuário proprietário da tarefa
    created_at = DateTimeField # Data/hora de criação (automático)
    updated_at = DateTimeField # Data/hora da última atualização (automático)
```

### Recursos Especiais
- **Isolamento de dados:** Cada usuário vê apenas suas próprias tarefas
- **Ordenação inteligente:** Tarefas pendentes aparecem primeiro
- **Timestamps automáticos:** created_at e updated_at gerenciados automaticamente
- **Paginação:** 5 tarefas por página para melhor performance
- **Validação:** Título único por usuário

##  Interface

O sistema possui uma interface limpa e responsiva com:
- Header com navegação e informações do usuário
- Botões de ação para criar, editar e excluir tarefas
- Cards visuais para cada tarefa
- Indicadores de status (Concluída/Pendente)
- Footer com informações do sistema


**Desenvolvido com usando Django**
