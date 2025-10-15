# ToDoList - Application Flask (MVC)

Une application **ToDoList** simple et efficace développée en **Python avec Flask**, suivant le **modèle MVC (Modèle - Vue - Contrôleur)**.  
Elle permet de créer, afficher, modifier et supprimer des tâches, tout en illustrant une architecture claire et maintenable.

---

## 🚀 Fonctionnalités

- ➕ **Ajouter** une tâche  
- 📅 **Afficher** la liste des tâches
- ❌ **Supprimer** une tâche  
 

---

## 🧱 Structure du projet

```bash
todolist/
│
├── app.py                # Point d’entrée principal de l’application Flask
├── main.py             
│
├── model/               # Couche Modèle
│   └── task.py     # Définition de la classe Task (ORM / SQLAlchemy)
│
├── controllers/           # Couche Contrôleur
│   └── task_controller.py # Gestion des routes et de la logique métier
│
├── views/                # Couche Vue
│   └── cli.py         
│
├── requirements.txt      # Dépendances Python
└── README.md             # Ce fichier
