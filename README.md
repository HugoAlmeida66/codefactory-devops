# CodeFactory Solutions - DevOps e Integração Contínua

![Integração contínua](https://github.com/HugoAlmeida66/codefactory-devops/actions/workflows/ci.yml/badge.svg?branch=main)

**Versão inicial: 0.1.0.** Projeto acadêmico individual de Hugo da Silva Almeida.

## Objetivo

Demonstrar práticas de DevOps aplicadas à empresa fictícia CodeFactory Solutions: versionamento rastreável, documentação compartilhada, containerização e verificações automatizadas. A API simples permite avaliar o fluxo de integração sem complexidade desnecessária.

## Tecnologias

Python 3.12, biblioteca padrão, unittest, Git, GitHub, Docker e GitHub Actions. Não há dependências Python externas. O servidor é destinado à demonstração acadêmica, sem banco de dados ou autenticação.

## Estrutura

```text
codefactory-devops/
  .github/workflows/ci.yml
  .github/pull_request_template.md
  docs/conflito.md
  docs/fluxo.md
  docs/planejamento.md
  tests/test_app.py
  app.py
  Dockerfile
  .dockerignore
  .gitignore
  LICENSE
  README.md
```

## Instalação

Instale Git e Python 3.12. Para execução em container, tenha Docker instalado e iniciado.

```sh
git clone https://github.com/HugoAlmeida66/codefactory-devops.git
cd codefactory-devops
```

## Execução

```sh
python app.py
```

Abra http://localhost:8000 e http://localhost:8000/health. Encerre com Ctrl+C. A variável PORT permite alterar a porta local; no container, mantenha a porta interna 8000 para preservar o healthcheck.

| Requisição | Resultado |
| --- | --- |
| GET / | HTTP 200, empresa e versão |
| GET /health | HTTP 200, status ok |
| GET /inexistente | HTTP 404, erro em JSON |

## Testes

```sh
python -m unittest discover -s tests -v
```

Os três testes iniciam um servidor real em porta temporária e verificam a rota inicial, o endpoint de saúde e o tratamento de rota inexistente. O servidor é encerrado ao final.

## Docker

```sh
docker build -t codefactory:0.1.0 .
docker run -d --name codefactory -p 127.0.0.1:8000:8000 codefactory:0.1.0
docker ps
docker logs codefactory
```

Acesse http://localhost:8000/health. Ao terminar: `docker rm -f codefactory`.

O Dockerfile usa python:3.12-slim, copia somente a aplicação e executa como usuário sem privilégios (10001). Um healthcheck consulta a API. O container padroniza o runtime e o comando de inicialização. A tag da imagem base pode receber atualizações; fixar um digest seria uma evolução para reproduções estritas.

## Branches e contribuição

- main: versão consolidada.
- desenvolvimento: integração antes da versão final.
- feature/container-ci: Docker e pipeline.
- feature/revisao-fluxo: exercício de conflito na política de integração.

Use commits pequenos e descritivos (feat:, test:, docs:, ci:). Abra Pull Request com objetivo, validação e issue relacionada. Neste trabalho individual há autorrevisão, sem simular aprovação de outro participante. A resolução didática de conflito foi feita por merge local; consulte [o registro verificável](docs/conflito.md). As integrações de Docker/CI e da entrega para main utilizam Pull Requests.

## Integração contínua

O workflow executa em pushes, Pull Requests e acionamento manual. Prepara Python, executa testes HTTP, constrói a imagem Docker, inicia o container e verifica /health. A etapa final registra logs e remove o container mesmo se uma verificação falhar. Não há deploy.

Consulte as [execuções reais no Actions](https://github.com/HugoAlmeida66/codefactory-devops/actions). O Docker é executado no runner Linux do GitHub, sem depender de instalação no computador do aluno.

## Organização

- [Issues e labels](https://github.com/HugoAlmeida66/codefactory-devops/issues?q=is%3Aissue)
- [Milestone da versão inicial](https://github.com/HugoAlmeida66/codefactory-devops/milestone/1)
- [Projects](https://github.com/HugoAlmeida66/codefactory-devops/projects)
- [Wiki de onboarding](https://github.com/HugoAlmeida66/codefactory-devops/wiki)
- [Insights](https://github.com/HugoAlmeida66/codefactory-devops/pulse)

## Licença

MIT. Consulte [LICENSE](LICENSE).

## Referências

- [GitHub: criação e testes de projetos Python](https://docs.github.com/en/actions/tutorials/build-and-test-code/python)
- [Docker: escrita de um Dockerfile](https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/)
- [Git: branches e merges](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
