from behave import given, when, then
from app.crud import *

def setup_function():
    disciplines.clear()

@given('que tenho os dados de uma disciplina válida')
def step_given(context):
    context.data = ("Matemática", "2026-01-01", "2026-06-01", 40, True)

@when('eu cadastro a disciplina')
def step_when(context):
    create_discipline(*context.data)

@then('a disciplina deve ser adicionada com sucesso')
def step_then(context):
    assert len(read_disciplines()) > 0

@given('que tenho dados com vagas negativas')
def step_given_neg(context):
    disciplines.clear()
    context.data = ("Física", "2026-01-01", "2026-06-01", -10, False)

@when('eu tento criar a disciplina')
def step_when_try(context):
    try:
        create_discipline(*context.data)
        context.erro = False
    except:
        context.erro = True

@then('deve ocorrer um erro')
def step_then_error(context):
    assert context.erro is True

@given('que existem disciplinas cadastradas')
def step_given_list(context):
    disciplines.clear()
    create_discipline("Bio", "2026-01-01", "2026-06-01", 10, False)

@when('eu leio as disciplinas')
def step_when_list(context):
    context.lista = read_disciplines()

@then('devo receber uma lista')
def step_then_list(context):
    assert len(context.lista) > 0

@given('que existe uma disciplina cadastrada')
def step_given_update(context):
    disciplines.clear()
    create_discipline("Geo", "2026-01-01", "2026-06-01", 10, False)

@when('eu atualizo a disciplina')
def step_when_update(context):
    update_discipline(0, {"available_slots": 50})

@then('a disciplina deve ser atualizada')
def step_then_update(context):
    assert read_disciplines()[0]["available_slots"] == 50

@given('que já existe uma disciplina cadastrada')
def step_given_delete(context):
    disciplines.clear()
    create_discipline("Geo", "2026-01-01", "2026-06-01", 10, False)

@when('eu deleto a disciplina')
def step_when_delete(context):
    delete_discipline(0)

@then('a disciplina deve ser removida')
def step_then_delete(context):
    assert len(read_disciplines()) == 0
