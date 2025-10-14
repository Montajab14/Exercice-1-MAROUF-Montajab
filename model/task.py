class Task:
    # Contient les classes métiers
    def __init__(self, titre, description="", task_id=None):
        self.id = task_id
        self.titre = titre
        self.description = description
        
    def to_dict(self):
        return{
            "id":self.id,
            "titre":self.titre,
            "description":self.description,
        }