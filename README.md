# Help Desk — Gestão de chamados de suporte

## Problema que este projeto resolve

Em um time de suporte ou TI interno, demandas chegam por e-mail, mensagem ou boca a boca e se perdem. Não há um lugar único para **abrir**, **acompanhar** e **resolver** chamados, nem visão de quantos estão abertos ou quanto tempo leva para fechar.

Este sistema foi desenvolvido para **centralizar o atendimento**: o usuário abre um chamado, acompanha o status e troca mensagens no próprio ticket; quem atende (suporte) atualiza o fluxo e vê indicadores no painel. O foco é **gestão de demandas** e **controle do fluxo de atendimento**, não só um CRUD genérico.

## O que o sistema faz (em poucas palavras)

- Cadastro e login de usuários.
- Abertura de chamados com título, descrição, prioridade e responsável.
- Lista com filtro por status; detalhe com histórico de **comentários**.
- **Transição de status** com regras (aberto → em andamento → resolvido) e **permissão** para quem é staff ou responsável pelo chamado.
- **Dashboard** com totais por status, taxa de resolução e tempo médio até resolver.
- Painel administrativo Django para gestão dos dados.
- **Testes** cobrindo criação de chamado e regras de status.

## Stack

| Camada | Tecnologia |
|--------|------------|
| Backend | Python 3.13, Django 4.2 |
| Banco (dev) | SQLite |
| Interface | Templates Django, CSS |
| Servidor (produção) | Gunicorn, WhiteNoise |

## Arquitetura

O backend foi organizado para **separar responsabilidades** e facilitar evolução:

```text
core/          Configuração global (settings, URLs raiz), ponto de entrada WSGI
tickets/       Domínio de chamados: models, views, forms, URLs, serviços de negócio
users/         Cadastro de usuário (signup) integrado à autenticação do Django
templates/     Telas HTML (lista, detalhe, formulários, dashboard)
static/        Estilos e assets estáticos
```

**Fluxo de dados:** requisição → view → (quando faz sentido) **camada de serviço** (`tickets/services.py`) para regras de status → model → template ou redirect.

**Autenticação:** `django.contrib.auth` (sessão), rotas protegidas com `@login_required`.

**Regras de negócio:** validação de transição de status e quem pode alterar ficam concentradas no serviço, em vez de espalhadas só nas views.

## Como rodar localmente

**Pré-requisitos:** Python 3.10+ (o projeto foi testado com 3.13).

1. Clonar o repositório e entrar na pasta do projeto.

2. Criar e ativar o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Instalar dependências:

```bash
pip install -r requirements.txt
```

4. Aplicar migrações:

```bash
python manage.py migrate
```

5. (Opcional) Criar superusuário para acessar `/admin/` e marcar usuários como *staff* (suporte):

```bash
python manage.py createsuperuser
```

6. Subir o servidor:

```bash
python manage.py runserver
```

7. No navegador: `http://127.0.0.1:8000` — será pedido login; use `/accounts/signup/` para criar conta ou o admin para o superusuário.

## Testes

```bash
python manage.py test
```

Cobre fluxo de criação de chamado, permissões de atualização de status e transições inválidas.

## Deploy (base)

Há preparação inicial para ambiente tipo PaaS:

- `Procfile` (Gunicorn)
- WhiteNoise para arquivos estáticos
- Variáveis documentadas em `.env.example`

Em produção, defina pelo menos: `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=False`, `DJANGO_ALLOWED_HOSTS` com o domínio real.

## Decisões técnicas (por quê assim)

- **Apps `tickets` e `users` separados:** isolar domínio de chamados do cadastro de usuário, alinhado a como projetos Django costumam crescer.
- **SQLite no desenvolvimento:** simplicidade para rodar em qualquer máquina; em produção costuma-se PostgreSQL ou serviço gerenciado.
- **Serviço para status:** concentrar regras de transição e permissão evita duplicar lógica e facilita testes.
- **Templates + CSS simples:** prioridade em backend, regras e dados; interface limpa sem depender de framework front pesado.
- **Testes no fluxo principal:** mostrar que o comportamento crítico do sistema está verificado automaticamente.
