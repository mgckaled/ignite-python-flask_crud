import uuid

from flask import Flask, jsonify, request

from models.task import Task

app = Flask(__name__)

tasks = []


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
    data = request.get_json()
    new_task = Task(
        title=data["title"],
        description=data.get("description", ""),
        completed=data.get("completed", False),
    )
    new_task.id = str(uuid.uuid4())
    tasks.append(new_task)
    print(tasks)
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


@app.route(
    "/tasks/<uuid:id>", methods=["GET"]
)  # Altera para aceitar UUID como parâmetro
def get_task(id):
    """
    Rota para obter detalhes de uma tarefa específica.

    Args:
        id (uuid): O identificador único da tarefa.

    Returns:
        jsonify: Resposta JSON contendo detalhes da tarefa ou uma mensagem de erro se não for encontrada.
    """
    for t in tasks:
        if str(t.id) == str(id):  # Converte ambos para string para comparar UUIDs
            return jsonify(t.to_dict())

    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404


@app.route("/tasks/<uuid:id>", methods=["PUT"])
def update_task(id):
    """
    Rota para atualizar uma tarefa existente.

    Args:
        id (uuid): O identificador único da tarefa a ser atualizada.

    Returns:
        jsonify: Resposta JSON indicando se a tarefa foi atualizada com sucesso ou uma mensagem de erro se não for encontrada.
    """
    task = None
    for t in tasks:
        if str(t.id) == str(id):
            task = t
    if task is None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

    data = request.get_json()
    task.title = data["title"]
    task.description = data["description"]
    task.completed = data["completed"]
    return jsonify({"message": "Tarefa atualizada com sucesso"})


if __name__ == "__main__":
    app.run(debug=True)
