from app.crud import *

def setup_function():
    disciplines.clear()
    
def test_create_discipline():
    disciplines = read_disciplines()
    disciplines.clear()

    create_discipline("Matemática", "2026-01-01", "2026-06-01", 40, True)

    assert len(disciplines) == 1

def test_negative_slots():
    try:
        create_discipline("Portugês", "2026", "2026", -1, True)
    except ValueError:
        assert True

def test_read_empty():
    assert read_disciplines() == []

def test_update_discipline():
    create_discipline("Geografia", "2026", "2026", 30, True)
    update_discipline(0, {"available_slots": 50})
    assert read_disciplines()[0]["available_slots"] == 50

def test_update_invalid_index():
    try:
        update_discipline(0, {"available_slots": 50})
    except IndexError:
        assert True

def test_delete_discipline():
    create_discipline("História", "2026", "2026", 30, True)
    delete_discipline(0)
    assert len(read_disciplines()) == 0

def test_delete_invalid_index():
    try:
        delete_discipline(0)
    except IndexError:
        assert True

def test_multiple_disciplines():
    create_discipline("Matemática", "2026", "2026", 30, True)
    create_discipline("Física", "2026", "2026", 20, False)
    assert len(read_disciplines()) == 2