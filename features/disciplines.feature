Feature: Gerenciamento de disciplinas

Scenario: Criar disciplina com sucesso
  Given que tenho os dados de uma disciplina válida
  When eu cadastro a disciplina
  Then a disciplina deve ser adicionada com sucesso

Scenario: Não permitir vagas negativas
  Given que tenho dados com vagas negativas
  When eu tento criar a disciplina
  Then deve ocorrer um erro

Scenario: Listar disciplinas
  Given que existem disciplinas cadastradas
  When eu leio as disciplinas
  Then devo receber uma lista

Scenario: Atualizar disciplina
  Given que existe uma disciplina cadastrada
  When eu atualizo a disciplina
  Then a disciplina deve ser atualizada

Scenario: Deletar disciplina
  Given que já existe uma disciplina cadastrada
  When eu deleto a disciplina
  Then a disciplina deve ser removida
