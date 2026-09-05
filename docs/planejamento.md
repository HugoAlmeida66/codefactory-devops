# Plano de adocao e evidencias

Este documento e preparatorio. Nao comprova execucoes no GitHub ou Docker.

## Diagnostico e proposta

A CodeFactory cresceu de dois para oito profissionais sem padronizar processos. Integracoes manuais, ambientes diferentes e conhecimento concentrado contribuem para atrasos e defeitos. A proposta combina responsabilidades compartilhadas, documentacao versionada, pequenas entregas revisadas e verificacoes automatizadas.

Git permite rastrear alteracoes e recuperar versoes. GitHub centraliza o trabalho, discussoes e revisoes. Docker padroniza o ambiente de execucao e reduz etapas de configuracao de novos colaboradores. A integracao continua detecta regressao nas rotas e problemas de build antes da incorporacao de alteracoes. Essas ferramentas apoiam a cultura de colaboracao; sua instalacao isolada nao assegura a mudanca cultural.

## Recursos remotos a configurar

- Issues: documentacao inicial, API e testes, containerizacao, pipeline.
- Milestone: Entrega v0.1.0, agrupando as quatro issues.
- Labels: documentacao, melhoria, infraestrutura e testes.
- Project: colunas A fazer, Em andamento e Concluido; vincular as issues.
- Wiki: pagina de onboarding e fluxo de contribuicao.
- Insights: capturar atividade real e explicar as informacoes disponiveis.

## Evidencias exigidas

1. Organizacao (10 pontos): link e capturas do repositorio, README e licenca.
2. Versionamento (20): registrar git init, add, commit, push e pull; pelo menos tres branches, merge, conflito real e sua resolucao, historico coerente.
3. Recursos (15): capturas de Issues, Milestones, Labels, Wiki, Insights e Projects efetivamente configurados.
4. Colaboracao ou commits individuais (15): autores reais, datas, mensagens e Pull Requests. Nao simular outros participantes ou datas.
5. Docker (20): capturar container rodando e resposta da API. Justificativa: reproduzir a mesma versao do Python e o mesmo comando de inicio, facilitando onboarding e verificacoes.
6. CI (20): capturar execucao do pipeline e explicar testes, build e verificacao HTTP. O YAML sozinho nao comprova a execucao.

## Relatorio final previsto

Capa com nome e RU; contexto e diagnostico; proposta DevOps; organizacao; versionamento; recursos do GitHub; colaboracao ou commits individuais; Docker; integracao continua; conclusao; referencias. Inserir capturas reais com legendas explicativas e link do repositorio. Exportar um unico PDF depois de completar as evidencias.

## Limites e acompanhamento

A API e demonstrativa e nao persiste dados. Comparar futuramente tempo de preparacao do ambiente, frequencia de integracao, falhas detectadas e tempo para corrigir problemas. Nao ha metricas anteriores coletadas; melhorias sao esperadas, nao resultados medidos.
