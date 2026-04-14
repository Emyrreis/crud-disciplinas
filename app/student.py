from datetime import datetime

students = []


def calculate_age(nascimento):
    data_nasc = datetime.strptime(nascimento, "%Y-%m-%d")
    hoje = datetime.today()
    idade = hoje.year - data_nasc.year - (
        (hoje.month, hoje.day) < (data_nasc.month, data_nasc.day)
    )
    return idade


def create_student(nome, nascimento, email, cpf, telefone, sexo, naturalidade):
    
    if calculate_age(nascimento) < 18:
        raise ValueError("Aluno menor de idade")

    for s in students:
        if s["email"] == email:
            raise ValueError("Email já cadastrado")
        if s["cpf"] == cpf:
            raise ValueError("CPF já cadastrado")
        if s["telefone"] == telefone:
            raise ValueError("Telefone já cadastrado")

    if not telefone.startswith("63"):
        raise ValueError("Telefone inválido")

    capitais = ["Palmas", "São Paulo", "Rio de Janeiro", "Brasília"]
    if naturalidade not in capitais:
        raise ValueError("Cidade não permitida")

    student = {
        "nome": nome,
        "nascimento": nascimento,
        "email": email,
        "cpf": cpf,
        "telefone": telefone,
        "sexo": sexo,
        "naturalidade": naturalidade
    }

    students.append(student)
    return student