class CLI:
    def __init__(self, controller):
        self.controller = controller

    def afficher_menu(self):
        print("\n=== ToDo List ===")
        print("1. Ajouter une tâche")
        print("2. Supprimer une tâche")
        print("3. Lister les tâches")
        print("4. Quitter")

    def ajouter_tache(self):
        titre = input("Titre de la tâche : ")
        description = input("Description (facultative) : ")
        task = self.controller.add_task(titre, description)
        print(f"Tâche ajoutée avec succès : {task.id} - {task.titre}")

    def supprimer_tache(self):
        try:
            task_id = int(input("ID de la tâche à supprimer : "))
            if self.controller.delete_task(task_id):
                print("Tâche supprimée avec succès.")
            else:
                print("Aucune tâche trouvée avec cet ID.")
        except ValueError:
            print("Veuillez entrer un ID valide (nombre entier).")

    def lister_taches(self):
        tasks = self.controller.list_tasks()
        if not tasks:
            print("Aucune tâche à afficher.")
        else:
            print("\n--- Liste des tâches ---")
            for t in tasks:
                print(f"[{t['id']}] {t['titre']} - {t['description']}")

    def demarrer(self):
        """Boucle principale de l'application"""
        while True:
            self.afficher_menu()
            choix = input("Votre choix : ")
            if choix == "1":
                self.ajouter_tache()
            elif choix == "2":
                self.supprimer_tache()
            elif choix == "3":
                self.lister_taches()
            elif choix == "4":
                print("Au revoir")
                break
            else:
                print("Choix invalide, veuillez réessayer.")
