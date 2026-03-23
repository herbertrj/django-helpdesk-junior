# Help Desk - Sistema de Gestao de Chamados

Projeto de portifolio para vaga junior/estagio com foco em Django e Python.

## Objetivo

Construir um sistema realista de abertura e acompanhamento de chamados para demonstrar:

- modelagem de dados com Django ORM;
- autenticacao e controle de acesso;
- organizacao de codigo por apps;
- regras de negocio basicas de atendimento;
- dashboard simples para analise.

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

## Roadmap (nivel junior forte)

- [x] Base do projeto Django com autenticacao
- [x] CRUD inicial de chamados
- [ ] Comentarios/interacoes por chamado
- [ ] Regras de transicao de status com permissao por perfil
- [ ] Dashboard com metricas de tempo medio de resolucao
- [ ] Testes automatizados para fluxo principal
- [ ] Deploy (Render/Railway)

## Plano de commits recomendado

### Hoje (Dia 1)

1. `chore: iniciar projeto django e apps principais`
2. `feat: adicionar autenticacao com login, logout e cadastro`
3. `feat: criar fluxo inicial de chamados com dashboard basico`
4. `docs: adicionar README com setup e roadmap`

### Dia 2

5. `feat: adicionar comentarios em chamados`
6. `refactor: separar regras de negocio em camada de servicos`

### Dia 3

7. `feat: validar transicoes de status por perfil de usuario`
8. `test: cobrir criacao e atualizacao de chamados`

### Dia 4

9. `feat: melhorar dashboard com indicadores de resolucao`
10. `style: melhorar layout das telas principais`

### Dia 5

11. `docs: adicionar capturas de tela e decisoes tecnicas`
12. `chore: preparar projeto para deploy`

## Decisoes tecnicas iniciais

- Usar apps separados (`tickets` e `users`) para facilitar evolucao.
- Comecar com SQLite para foco em logica e entrega rapida.
- Priorizar simplicidade nas telas para manter foco no backend.
