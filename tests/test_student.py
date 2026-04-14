import pytest
from app.student import create_student


def test_create_valid_student():
    student = create_student(
        "João",
        "2000-01-01",
        "joao@email.com",
        "12345678",
        "63999999999",
        "M",
        "Palmas"
    )
    assert student["nome"] == "João"


def test_underage_student():
    with pytest.raises(ValueError):
        create_student(
            "Pedro",
            "2010-01-01",
            "pedro@email.com",
            "012345789",
            "6311111111",
            "M",
            "Palmas"
        )


def test_duplicate_email():
    create_student(
        "Ana",
        "2000-01-01",
        "ana@email.com",
        "11111111111",
        "6377777777",
        "F",
        "Palmas"
    )

    with pytest.raises(ValueError):
        create_student(
            "Ana2",
            "2000-01-01",
            "ana@email.com",
            "22222222222",
            "63955555555",
            "F",
            "Palmas"
        )


def test_duplicate_cpf():
    create_student(
        "Carlos",
        "2000-01-01",
        "carlos@email.com",
        "12345678900",
        "6346312789",
        "M",
        "Palmas"
    )

    with pytest.raises(ValueError):
        create_student(
            "Carlos2",
            "2000-01-01",
            "carlos2@email.com",
            "12345678900",
            "63988888888",
            "M",
            "Palmas"
        )


def test_duplicate_phone():
    create_student(
        "Maria",
        "2000-01-01",
        "maria@email.com",
        "47859612347",
        "6333333333",
        "F",
        "Palmas"
    )

    with pytest.raises(ValueError):
        create_student(
            "Maria2",
            "2000-01-01",
            "maria2@email.com",
            "22222222222",
            "6333333333",
            "F",
            "Palmas"
        )