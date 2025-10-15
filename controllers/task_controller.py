from model.task import Task

class TaskController:
    """Contrôleur pour gérer les tâches"""

    def __init__(self):
        self.tasks = []
        self.next_id = 1 

    def add_task(self, titre, description=""):
        """Ajoute une nouvelle tâche"""
        task = Task(titre, description, task_id=self.next_id)
        self.next_id += 1
        self.tasks.append(task)
        return task

    def delete_task(self, task_id):
        """Supprime une tâche par ID"""
        before = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.id != task_id]
        return len(self.tasks) < before

    def list_tasks(self):
        """Retourne toutes les tâches sous forme de dict"""
        return [t.to_dict() for t in self.tasks]
