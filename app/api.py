from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="school",
        user="user",
        password="password"
    )

@app.route("/")
def home():
    return "API de Disciplinas rodando!"

@app.route("/disciplinas", methods=["POST"])
def criar_disciplina():
    data = request.json

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO disciplinas (titulo, dtinicio, dtfinal, vagas, verao)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        data["titulo"],
        data["dtinicio"],
        data["dtfinal"],
        data["vagas"],
        data["verao"]
    ))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"msg": "Disciplina criada com sucesso"}), 201

@app.route("/disciplinas", methods=["GET"])
def listar_disciplinas():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM disciplinas;")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(rows)

@app.route("/disciplinas/<int:id>", methods=["PUT"])
def atualizar_disciplina(id):
    data = request.json

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE disciplinas
        SET titulo=%s, dtinicio=%s, dtfinal=%s, vagas=%s, verao=%s
        WHERE id=%s
    """, (
        data["titulo"],
        data["dtinicio"],
        data["dtfinal"],
        data["vagas"],
        data["verao"],
        id
    ))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"msg": "Disciplina atualizada"})

@app.route("/disciplinas/<int:id>", methods=["DELETE"])
def deletar_disciplina(id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM disciplinas WHERE id=%s", (id,))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"msg": "Disciplina deletada"})


if __name__ == "__main__":
    app.run(debug=True)