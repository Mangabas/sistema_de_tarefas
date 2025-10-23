# Sistema de Tarefas 📝

Sistema completo de gerenciamento de tarefas (To-Do List) desenvolvido com Django, permitindo criar, editar, visualizar e excluir tarefas com controle de usuários.

## 📋 Sobre o Projeto

Este é um sistema web de gerenciamento de tarefas que permite aos usuários:
- Criar suas próprias tarefas com título e descrição
- Marcar tarefas como concluídas ou pendentes
- Editar e excluir tarefas existentes
- Visualizar detalhes completos de cada tarefa
- Sistema de autenticação com registro e login de usuários
- Cada usuário visualiza apenas suas próprias tarefas
- Paginação automática (5 tarefas por página)
- Interface responsiva e amigável

## 🚀 Tecnologias Utilizadas

- **Django 5.2.7** - Framework web Python
- **PostgreSQL** - Banco de dados (configurado via variáveis de ambiente)
- **Python-decouple** - Gerenciamento de variáveis de ambiente
- **HTML/CSS** - Interface do usuário
- **Class-Based Views** - Para operações CRUD

## 📁 Estrutura do Projeto

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

## ⚙️ Pré-requisitos

- **Python 3.8+** instalado
- **PostgreSQL** instalado e rodando (ou SQLite para testes)
- **pip** (gerenciador de pacotes Python)

## 🔧 Configuração e Instalação

### 1. Clone o Repositório

```bash
git clone <url-do-repositorio>
cd sistema_tarefas
```

### 2. Instalar Dependências

```bash
pip install django
pip install python-decouple
pip install psycopg2-binary
```

Ou crie um arquivo `requirements.txt`:

```txt
Django==5.2.7
python-decouple==3.8
psycopg2-binary==2.9.9
```

E instale com:

```bash
pip install -r requirements.txt
```

### 3. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
SECRET_KEY=sua-chave-secreta-aqui
DB_NAME=nome_do_banco
DB_USER=usuario_do_banco
DB_PASSWORD=senha_do_banco
DB_HOST=localhost
DB_PORT=5432
```

> **Nota:** Para gerar uma SECRET_KEY, você pode usar:
> ```python
> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```

### 4. Criar o Banco de Dados

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

## 👤 Credenciais de Teste

Após criar o superusuário, você pode usar essas credenciais para acessar o sistema.

**Exemplo de superusuário:**
- **Usuário:** `admin`
- **Senha:** `admin123`

> **Importante:** Crie o superusuário usando o comando `createsuperuser` antes de tentar fazer login.

## 📌 Funcionalidades Detalhadas

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

## 🔐 Painel Administrativo

Acesse o painel administrativo do Django em: **http://127.0.0.1:8000/admin/**

Use as credenciais do superusuário que você criou.

No admin, você pode:
- Gerenciar todos os usuários
- Visualizar e editar todas as tarefas
- Acessar logs e permissões do sistema

## 🎨 Interface

O sistema possui uma interface limpa e responsiva com:
- Header com navegação e informações do usuário
- Botões de ação para criar, editar e excluir tarefas
- Cards visuais para cada tarefa
- Indicadores de status (Concluída/Pendente)
- Footer com informações do sistema

## 🛠️ Comandos Úteis

```bash
# Criar migrações após alterar models
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Rodar servidor
python manage.py runserver

# Rodar em porta específica
python manage.py runserver 8080

# Shell interativo do Django
python manage.py shell
```

## 📝 Observações

- O projeto usa PostgreSQL em produção (configurado via .env)
- Para desenvolvimento local, você pode usar SQLite alterando DATABASES em settings.py
- Certifique-se de nunca commitar o arquivo `.env` com dados sensíveis
- DEBUG está ativado - desative em produção
- Adicione domínios em ALLOWED_HOSTS para deploy

## 🐛 Solução de Problemas

**Erro de conexão com banco de dados:**
- Verifique se o PostgreSQL está rodando
- Confirme as credenciais no arquivo `.env`

**Erro ao executar migrate:**
- Certifique-se de que todas as dependências estão instaladas
- Verifique se o banco de dados existe

**Página não carrega estilos:**
- Execute `python manage.py collectstatic` (se necessário)
- Verifique se DEBUG=True está ativo no settings.py

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais.

---

**Desenvolvido com ❤️ usando Django**
