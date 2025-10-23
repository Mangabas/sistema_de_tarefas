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

### Gerenciamento de Urls

```python
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.TaskList.as_view(), name='list'),
    path('task/<int:pk>/', views.DetailTask.as_view(), name='task_detail'),
    path('task/create/', views.CreateTask.as_view(), name='create_task'),
    path('task/<int:pk>/update/', views.UpdateTask.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', views.DeleteTask.as_view(), name='delete_task'),
    path('task/<int:pk>/toggle/', views.toggle, name='toggle_task'),

]
```

### Modelagem (Task)

```python
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Task(TimeStampModel):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
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
