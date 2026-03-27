# Help Desk - Sistema de Gestao de Chamados

Projeto de portfolio feito para praticar Django em um cenario mais proximo do dia a dia: abertura e acompanhamento de chamados.

## Sobre o projeto

A ideia aqui e simples: ter um sistema funcional, organizado e facil de evoluir.
Neste primeiro momento, foquei em acertar o basico (autenticacao, CRUD de chamados e dashboard inicial) antes de partir para funcionalidades mais avancadas.

## Stack

- Python 3.13
- Django 4.2
- SQLite (desenvolvimento)
- Templates Django + CSS simples

## Funcionalidades ja implementadas

- Cadastro, login e logout de usuarios
- Criacao de chamados
- Lista de chamados com filtro por status
- Detalhe de chamado
- Comentarios por chamado
- Atualizacao de status com permissao por perfil
- Dashboard com taxa e tempo medio de resolucao
- Tela administrativa com `Ticket` registrado no admin
- Testes automatizados para fluxo principal

## Estrutura do projeto

```text
core/      -> configuracoes globais e rotas principais
tickets/   -> dominio de chamados (model, views, forms, urls)
users/     -> cadastro de usuario
templates/ -> telas HTML
static/    -> estilos CSS
```

## Como rodar localmente

1. Criar e ativar ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Executar migracoes:

```bash
python manage.py migrate
```

4. Criar superusuario (opcional, recomendado):

```bash
python manage.py createsuperuser
```

5. Rodar servidor:

```bash
python manage.py runserver
```

## Rodar testes

```bash
python manage.py test
```

## Deploy (base)

Este projeto ja possui configuracao inicial para deploy:

- `Procfile` para executar com Gunicorn
- `whitenoise` para servir arquivos estaticos
- variaveis de ambiente em `.env.example`

Em producao, configure pelo menos:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG=False`
- `DJANGO_ALLOWED_HOSTS=seu-dominio.com`

## Proximos passos

- [x] Base do projeto Django com autenticacao
- [x] CRUD inicial de chamados
- [x] Comentarios por chamado
- [x] Regras de transicao de status com permissao por perfil
- [x] Dashboard com metricas de tempo medio de resolucao
- [x] Testes automatizados para fluxo principal
- [x] Deploy (configuracao inicial)
- [ ] Publicar projeto em plataforma (Render/Railway)
- [ ] Adicionar imagens do sistema no README

## Decisoes tecnicas

- Usar apps separados (`tickets` e `users`) para facilitar evolucao.
- Comecar com SQLite para foco em logica e entrega rapida.
- Priorizar simplicidade nas telas para manter foco no backend.
