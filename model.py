from dataclasses import dataclass
from typing import List

@dataclass
class Task():
    # содержит свойства для описания задачи и её статуса
    task_id: int
    text: str
    status: bool = False


class TodoList():
    # хранит список задач. Позволяет добавить, отметить выполнение, удалить, редактировать и получить список задач
    
    def __init__(self):
        # свойства списка задач
        self.todo_list: List[Task] = [
                Task(task_id=0, text="Купить продукты"),
                Task(task_id=1, text="Погулять с собакой"),
                Task(task_id=2, text="Доделать рабочие задачи")
            ]

    def add_task(self, task: str) -> None:
        # добавление задачи в список
        if self.todo_list:
            task_id = max(task.task_id for task in self.todo_list) + 1
        else:
            task_id = 0
        new_task = Task(task_id=task_id, text=task, status=False)
        self.todo_list.append(new_task)

    def change_task_status(self, task_id: int) -> None:
        # изменение статуса задачи
        for task in self.todo_list:
            if task.task_id == task_id:
                task.status = True
        
    def delete_task(self, task_id: int) -> None:
        # удаление задачи из списка, присвоение новых номеров оставшимся задачам
        for task in self.todo_list:
            if task.task_id == task_id:
                self.todo_list.remove(task)

    def delete_completed_tasks(self) -> bool:
        # удаление всех выполненных задач, присвоение новых номеров оставшимся задачам
        completed = False
        for task in self.todo_list[:]:
            if task.status == True:
                self.todo_list.remove(task)
                completed = True
        return completed

    def edit_task_text(self, task_id: int, text: str) -> None:
        # изменение текста задачи
        for task in self.todo_list:
            if task.task_id == task_id:
                task.text = text

    def check_task_id(self, task_id: int) -> int:
        # проверка наличия задачи с указанным id
        for task in self.todo_list:
            if task.task_id == task_id:
                return task_id
        return None
    
    def get_tasks(self, status: bool = None) -> list:
        # вывод списка задач
        if status is None:
            tasks = self.todo_list
        else:
            tasks = [task for task in self.todo_list if task.status == status]
        return tasks
    
    def get_task_by_id(self, task_id: int) -> str:
        # получение текста задачи по id
        for task in self.todo_list:
            if task.task_id == task_id:
                text = task.text
                return text