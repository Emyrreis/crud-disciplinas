from behave import given, when, then
from app.crud import create_discipline, read_disciplines

@given('que tenho os dados de uma disciplina válida')
def step_given(context):
    context.data = ("Matemática", "2026-01-01", "2026-06-01", 40, True)

@when('eu cadastro a disciplina')
def step_when(context):
    create_discipline(*context.data)

@then('a disciplina deve ser adicionada com sucesso')
def step_then(context):
    assert len(read_disciplines()) > 0

    