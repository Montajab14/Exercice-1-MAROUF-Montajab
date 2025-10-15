from controllers.task_controller import TaskController
from views.cli import CLI

def main():
    controller = TaskController()
    interface = CLI(controller)
    interface.demarrer()

if __name__ == "__main__":
    main()
