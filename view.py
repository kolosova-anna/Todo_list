import tabulate as tl
from model import TodoList

class TodoView():
    # отвечает за отображение списка задач, взаимодействие с пользователем
    
    def __init__(self, todo_list: list):
        # свойства числа
        self.todo_list: list = todo_list
        #self.number = 0
    
    def pass_task(self, task: str) -> None:
        new_task = task
        self.todo_list.add_task(new_task)    
        print(f"Добавдена новая задача: {task}")

    def show_tasks(self, status: bool = None) -> None:
        # вывод списка задач
        if status is None:
            tasks = self.todo_list.todo_list
        else:
            tasks = [task for task in self.todo_list.todo_list if task.status == status]
        if not tasks:
            print("Список задач пуст")
            return
        print("Список задач:")
        headers = ["№", "Задача", "Статус"]
        rows = []
        for task in tasks:
            rows.append([task.task_id, task.text, "Выполнено" if task.status else "Не выполнено"])
        print(tl.tabulate(rows, headers=headers, tablefmt="grid"))

    def pass_change_task_status(self, task_id: int) -> None:
        task_id = task_id
        self.todo_list.change_task_status(task_id)
        print(f"Задача '{task_id}' отмечена как выполненная")

    def pass_delete_task(self, task_id: int) -> None:
        task_id = task_id
        self.todo_list.delete_task(task_id)
        print(f"Задача '{task_id}' удалена")

    def pass_edit_task_text(self, task_id: int, text: str) -> None:
        task_id = task_id
        text = text
        self.todo_list.edit_task_text(task_id, text)

    def pass_delete_completed_tasks(self) -> None:
        self.todo_list.delete_completed_tasks()


