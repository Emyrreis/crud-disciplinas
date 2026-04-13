Objetivo do Projeto:

Este projeto foi desenvolvido como parte da disciplina de Teste e Qualidade de Software, com o objetivo de aplicar na prática:
criação de um CRUD em Python
testes unitários
testes comportamentais (BDD)
medição de cobertura de testes
automação com integração contínua

O foco principal foi garantir a qualidade do software através de testes automatizados.

Tecnologias Utilizadas:
Python 3 → linguagem principal do projeto
pytest → testes unitários
behave → testes baseados em comportamento
coverage → análise de cobertura de testes
GitHub Actions → automação dos testes (CI/CD)

Como executar o projeto:
1. Clonar o repositório
git clone <url-do-repositorio>
cd crud-disciplinas
2. Instalar dependências
pip install pytest behave coverage
3. Executar testes unitários (pytest)
python -m pytest
4. Verificar cobertura de testes
coverage run -m pytest
coverage report
5. Executar testes BDD
python -m behave

O que será testado:
criação de disciplinas
validação de erros (ex: vagas negativas)
leitura de dados
atualização
remoção
