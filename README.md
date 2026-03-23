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
- Atualizacao de status do chamado
- Dashboard com contagem por status
- Tela administrativa com `Ticket` registrado no admin

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

## Proximos passos

- [x] Base do projeto Django com autenticacao
- [x] CRUD inicial de chamados
- [ ] Comentarios por chamado
- [ ] Regras de transicao de status com permissao por perfil
- [ ] Dashboard com metricas de tempo medio de resolucao
- [ ] Testes automatizados para fluxo principal
- [ ] Deploy (Render/Railway)

## Decisoes tecnicas

- Usar apps separados (`tickets` e `users`) para facilitar evolucao.
- Comecar com SQLite para foco em logica e entrega rapida.
- Priorizar simplicidade nas telas para manter foco no backend.
