from app.crud import create_discipline, read_disciplines

def test_create_discipline():
    disciplines = read_disciplines()
    disciplines.clear()

    create_discipline("Matemática", "2026-01-01", "2026-06-01", 40, True)

    assert len(disciplines) == 1