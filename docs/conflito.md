# Resolução de conflito entre branches

Esta foi uma demonstração didática deliberada, executada no repositório real. Não corresponde a um incidente de produção nem à participação de outra pessoa.

## Situação

O arquivo `docs/fluxo.md` foi criado no commit `a423d2d`. A branch `feature/revisao-fluxo` alterou sua única linha no commit `44dd3bf`, exigindo revisão por Pull Request. A branch `desenvolvimento` alterou a mesma linha no commit `3700278`, exigindo pipeline aprovado.

Ao executar `git merge --no-ff feature/revisao-fluxo` em `desenvolvimento`, o Git produziu:

```text
Auto-merging docs/fluxo.md
CONFLICT (content): Merge conflict in docs/fluxo.md
Automatic merge failed; fix conflicts and then commit the result.
```

`git status --short` indicou `UU docs/fluxo.md`. Os marcadores mostraram as duas políticas concorrentes.

## Resolução

O conteúdo final preserva os dois requisitos:

```text
Politica: revisar o codigo por Pull Request e exigir pipeline aprovado antes da integracao.
```

Após editar o arquivo, foram executados `git add docs/fluxo.md` e `git commit -m "merge: resolver conflito preservando revisao e pipeline"`. O merge resultante é `096154d`, com dois pais. Isso demonstra que a resolução foi registrada no histórico, e não apenas descrita.

## Conferência

```sh
git show --format=fuller 096154d
git show 3700278:docs/fluxo.md
git show 44dd3bf:docs/fluxo.md
git show 096154d:docs/fluxo.md
git log --graph --oneline --all
```

O primeiro commit de merge foi executado localmente para demonstrar a resolução. A integração de Docker/CI e a entrega para `main` utilizam Pull Requests no GitHub.
