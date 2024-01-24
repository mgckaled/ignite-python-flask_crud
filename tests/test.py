import pytest
import requests

# CRUD
BASE_URL = "http://127.0.0.1:5000"
tasks = []


def test_create_task():
    """
    Testa a criação de uma nova tarefa via API.

    Verifica se a resposta tem o código de status 200, se contém a mensagem e se o ID da tarefa é adicionado à lista de tarefas.
    """
    new_task_data = {"title": "Nova tarefa", "description": "Descrição da nova tarefa"}
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data, timeout=10)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json["id"])


def test_get_tasks():
    """
    Testa a obtenção da lista de tarefas via API.

    Verifica se a resposta tem o código de status 200 e se contém a lista de tarefas e o total de tarefas.
    """
    response = requests.get(f"{BASE_URL}/tasks", timeout=10)
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json


def test_get_task():
    """
    Testa a obtenção de detalhes de uma tarefa específica via API.

    Verifica se a resposta tem o código de status 200, se o ID na resposta corresponde ao ID da tarefa solicitada.
    """
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}", timeout=10)
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json["id"]


def test_update_task():
    """
    Testa a atualização de detalhes de uma tarefa específica via API.

    Verifica se a resposta tem o código de status 200, se contém a mensagem e se a tarefa foi atualizada corretamente.
    """
    if tasks:
        task_id = tasks[0]
        payload = {
            "completed": True,
            "description": "Nova descrição",
            "title": "Título atualizado",
        }
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload, timeout=10)
        response_json = response.json()
        assert "message" in response_json

        # Nova requisição a tarefa especifica
        response = requests.get(f"{BASE_URL}/tasks/{task_id}", timeout=10)
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["title"] == payload["title"]
        assert response_json["description"] == payload["description"]
        assert response_json["completed"] == payload["completed"]


def test_delete_task():
    """
    Testa a exclusão de uma tarefa específica via API.

    Verifica se a resposta tem o código de status 200 e se a tarefa foi removida corretamente.
    """
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}", timeout=10)
        assert response.status_code == 200

        response = requests.get(f"{BASE_URL}/tasks/{task_id}", timeout=10)
        assert response.status_code == 404
