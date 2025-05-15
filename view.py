import tabulate as tl
from model import TodoList

class TodoView():
    # отвечает за отображение списка задач, взаимодействие с пользователем
    
    def __init__(self, todo_list: list):
        # свойства числа
        self.todo_list: list = todo_list

    def check_input(self) -> int:
    # проверка введенного пользователем числа
        while True:
            try:
                number = int(input())
                return number
            except ValueError:
                print("Ошибка. Введите число")

    def get_task_id(self) -> int:
        # получения номера задачи для дальнейшей работы с ней
        print("Введите номер задачи:\n")
        task_id = self.check_input()
        return task_id
    
    def pass_task(self, task: str) -> None:
        new_task = task
        self.todo_list.add_task(new_task)    
        print(f"Добавдена новая задача: {task}")

    def show_tasks(self, status: bool = None) -> None:
        # вывод списка задач
        tasks = self.todo_list.get_tasks()
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
        text = self.todo_list.get_task_by_id(task_id)
        self.todo_list.change_task_status(task_id)
        print(f"Задача '{text}' отмечена как выполненная")

    def pass_delete_task(self, task_id: int) -> None:
        task_id = task_id
        text = self.todo_list.get_task_by_id(task_id)
        self.todo_list.delete_task(task_id)
        print(f"Задача '{text}' удалена")

    def pass_edit_task_text(self, task_id: int, text: str) -> None:
        task_id = task_id
        old_text = self.todo_list.get_task_by_id(task_id)
        new_text = text
        self.todo_list.edit_task_text(task_id, new_text)
        print(f"Текст задачи {task_id} изменен с '{old_text}' на '{new_text}'")

    def pass_delete_completed_tasks(self) -> None:
        completed = self.todo_list.delete_completed_tasks()
        if completed:
            print("Все выполненные задачи удалены")
        else:
            print("Выполненных задач в списке не найдено")

    def pass_check_task_id(self) -> int:
        task_id = self.get_task_id()
        while True:
            index = self.todo_list.check_task_id(task_id)
            if index is not None:
                return index
            else:
                print(f"Задача под номером {task_id} не найдена")
                self.show_tasks()
                try:
                    task_id = self.get_task_id()
                except ValueError:
                    print("Ошибка ввода")

