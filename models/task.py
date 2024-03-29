import uuid


class Task:
    """
    Representa uma tarefa com atributos como identificador, título, descrição e status de conclusão.
    """

    def __init__(self, title, description, completed=False) -> None:
        """
        Inicializa uma nova instância da classe Task.

        Args:
            title (str): O título da tarefa.
            description (str): A descrição da tarefa.
            completed (bool, optional): Indica se a tarefa está concluída. Padrão é False.
        """
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.completed = completed

    def to_dict(self):
        """
        Converte a instância da classe Task em um dicionário.

        Returns:
            dict: Um dicionário contendo os atributos da tarefa.
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
        }
