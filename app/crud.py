disciplines = []

def create_discipline(titulo, dtinicio, dtfinal, vagas, verao):
    if vagas < 0:
        raise ValueError("Número de vagas inválido")

    discipline = {
        "title": titulo,
        "start_dt": dtinicio,
        "end_dt": dtfinal,
        "available_slots": vagas,
        "summer": verao
    }

    disciplines.append(discipline)
    return discipline


def read_disciplines():
    return disciplines


def update_discipline(index, new_discipline):
    if index >= len(disciplines):
        raise IndexError("Disciplina não encontrada")

    disciplines[index].update(new_discipline)


def delete_discipline(index):
    if index >= len(disciplines):
        raise IndexError("Disciplina não encontrada")

    disciplines.pop(index)