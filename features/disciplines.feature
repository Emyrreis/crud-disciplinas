Feature: Gerenciamento de disciplinas

Scenario: Criar disciplina com sucesso
  Given que tenho os dados de uma disciplina válida
  When eu cadastro a disciplina
  Then a disciplina deve ser adicionada com sucesso