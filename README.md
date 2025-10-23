# Sistema de Tarefas

Sistema simples de gerenciamento de tarefas desenvolvido com Django.

## Requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)

## Como Configurar e Executar

### 1. Instalar Dependências

```bash
pip install django
```

### 2. Criar o Banco de Dados

```bash
python manage.py migrate
```

### 3. Criar um Superusuário (Opcional)

```bash
python manage.py createsuperuser
```

Siga as instruções para criar um usuário administrador.

### 4. Rodar o Servidor

```bash
python manage.py runserver
```

O sistema estará disponível em: http://127.0.0.1:8000/

## Credenciais de Teste

Se você criou um superusuário durante a configuração, use as credenciais que você definiu.

**Exemplo de credenciais para teste:**
- Usuário: `admin`
- Senha: `admin123`

> **Nota:** Você precisa criar este usuário usando o comando `createsuperuser` mencionado acima.

## Funcionalidades

- Criar tarefas
- Listar tarefas
- Editar tarefas
- Excluir tarefas
- Visualizar detalhes das tarefas
- Sistema de autenticação de usuários

## Acessar o Admin do Django

Após criar um superusuário, você pode acessar o painel administrativo em:
http://127.0.0.1:8000/admin/
