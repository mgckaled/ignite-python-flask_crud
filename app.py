from flask import Flask, jsonify, request

from models.task import Task

app = Flask(__name__)

tasks = []
TASK_ID_CONTROL = 1


@app.route("/")
def init_server():
    """
    Rota inicial que verifica se o servidor está em execução.

    Returns:
        str: Mensagem indicando que o servidor está em execução.
    """
    return "Server is running"


@app.route("/tasks", methods=["POST"])
def create_task():
    """
    Rota para criar uma nova tarefa.

    Returns:
        jsonify: Resposta JSON indicando se a tarefa foi criada com sucesso.
    """
    global TASK_ID_CONTROL
    data = request.get_json()
    new_task = Task(
        id=TASK_ID_CONTROL, title=data["title"], description=data.get("description", "")
    )
    TASK_ID_CONTROL += 1
    tasks.append(new_task)
    print(tasks)  # Remova ou substitua por logging, se necessário.
    return jsonify({"message": "Nova tarefa criada com sucesso"})


@app.route("/tasks", methods=["GET"])
def get_tasks():
    """
    Rota para obter a lista de todas as tarefas.

    Returns:
        jsonify: Resposta JSON contendo a lista de tarefas e o total de tarefas.
    """
    task_list = [task.to_dict() for task in tasks]

    output = {"tasks": task_list, "total_tasks": len(task_list)}
    return jsonify(output)


@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    """
    Rota para obter detalhes de uma tarefa específica.

    Args:
        id (int): O identificador único da tarefa.

    Returns:
        jsonify: Resposta JSON contendo detalhes da tarefa ou uma mensagem de erro se não for encontrada.
    """
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())

    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404


if __name__ == "__main__":
    app.run(debug=True)
