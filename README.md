# CodeFactory Solutions - demonstracao DevOps

Versao inicial: 0.1.0. Projeto academico de DevOps e Integracao Continua.

## Objetivo

Demonstrar uma API simples com ambiente reproduzivel e verificacao automatizada, como parte da proposta de melhoria dos processos da CodeFactory Solutions.

## Tecnologias

Python 3.12, biblioteca padrao, unittest, Git, GitHub, Docker e GitHub Actions. Sem dependencias Python externas. Servidor destinado a demonstracao academica.

## Estrutura

- `app.py`: API HTTP, rotas `/` e `/health`.
- `tests/`: testes HTTP de integracao.
- `Dockerfile`: ambiente de execucao.
- `.github/workflows/ci.yml`: testes, build e verificacao do container.
- `docs/`: planejamento e lista de evidencias pendentes.

## Instalacao e execucao

Instale Python 3.12. Dentro da pasta do projeto:

```sh
python app.py
```

Abra http://localhost:8000 e http://localhost:8000/health. Encerre com Ctrl+C.

## Testes

```sh
python -m unittest discover -s tests -v
```

## Docker

Com Docker instalado e iniciado:

```sh
docker build -t codefactory:0.1.0 .
docker run -d --name codefactory -p 127.0.0.1:8000:8000 codefactory:0.1.0
docker ps
docker logs codefactory
```

Acesse `/health` e capture o container em execucao. Ao terminar: `docker rm -f codefactory`.

## Fluxo proposto

Branches `main`, `desenvolvimento` e `feature/health`. Alteracoes entram por Pull Request, com descricao, issue associada e pipeline aprovado. Commits pequenos e descritivos, com prefixos `feat:`, `test:`, `docs:` e `ci:`. Em trabalho individual, preservar a autoria real e explicar a autorrevisao; em grupo, cada pessoa realiza suas contribuicoes.

## Integracao continua

O workflow executa a cada push ou Pull Request: prepara Python, testa respostas HTTP, constroi a imagem, inicia o container e verifica `/health`. A falha em qualquer verificacao interrompe o job. Nao realiza deploy. A execucao remota ainda precisa ser verificada no repositorio do aluno.

## Licenca

MIT, conforme LICENSE.

## Referencias

- https://docs.github.com/en/actions/tutorials/build-and-test-code/python
- https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/
