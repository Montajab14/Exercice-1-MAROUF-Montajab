from flask import Flask, request, jsonify

# Import correct du contrôleur (classe)
from controllers.task_controller import TaskController

app = Flask(__name__)

# Instancier correctement le contrôleur (une seule instance partagée)
controller = TaskController()


@app.route('/recup', methods=['GET'])
def get_model():
    """Récupérer toutes les tâches"""
    recup = controller.list_tasks()  
    if not recup:
        return jsonify({"message": "Aucune tâche dans la liste..."}), 200
    return jsonify(recup), 200


@app.route('/task', methods=['POST'])
def add_task():
    """Créer une nouvelle tâche"""
    data = request.get_json()
    if not data or "titre" not in data:
        return jsonify({"error": "Le champ 'titre' est obligatoire!"}), 400

    titre = data["titre"]
    description = data.get("description", "")

    task = controller.add_task(titre, description)
    return jsonify({
        "message": "Tâche ajoutée avec succès !",
        "task": task.to_dict()
    }), 201


@app.route('/recup/<int:recup_id>', methods=['GET'])
def get_recup(recup_id):
    """Récupérer une tâche spécifique"""
    tasks = controller.list_tasks()
    for t in tasks:
        if t["id"] == recup_id:
            return jsonify(t), 200
    return jsonify({"error": f"Aucune tâche trouvée avec l'ID {recup_id}."}), 404


@app.route('/task/<int:recup_id>', methods=['PUT'])
def update_task(recup_id):
    """Mettre à jour une tâche (titre et/ou description)"""
    data = request.get_json() or {}

    # On parcourt les objets Task stockés dans controller.tasks
    for task in controller.tasks:
        if task.id == recup_id:
            task.titre = data.get("titre", task.titre)
            task.description = data.get("description", task.description)
            return jsonify({
                "message": f"Tâche {recup_id} mise à jour avec succès.",
                "task": task.to_dict()
            }), 200

    return jsonify({"error": f"Aucune tâche trouvée avec l'ID {recup_id}."}), 404


@app.route('/task/<int:recup_id>', methods=['DELETE'])
def delete_task(recup_id):
    """Supprimer une tâche"""
    if controller.delete_task(recup_id):
        return jsonify({"message": f"Tâche {recup_id} supprimée avec succès."}), 200
    return jsonify({"error": f"Aucune tâche trouvée avec l'ID {recup_id}."}), 404


if __name__ == '__main__':
    app.run(debug=True)
