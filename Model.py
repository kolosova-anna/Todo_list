class Task():
    # содержит свойства для описания задачи и её статуса
    
    def __init__(self, task_id: int, text: str, status: bool = False):
        # свойства задачи и статуса
        self.task_id: int = task_id
        self.text: str = text
        self.status: bool = status


class TodoList():
    # хранит список задач. Позволяет добавить, отметить выполнение, удалить, редактировать и получить список задач
    
    def __init__(self):
        # свойства списка задач
        self.todo_list = []
    
    def get_task(self):
        # запрашиваем новую задачу у пользователя для добавления в список
        return input("Введите текст задачи:\n")

    def add_task(self):
        # добавление задачи в список
        task = self.get_task()
        self.todo_list.append({"id": len(self.todo_list), "text": task, "status": False})

    def change_task_status(self, task_id: int):
        # изменение статуса задачи
        for task in self.todo_list:
            if task["id"] == task_id:
                task["status"] = True
                print(f"Задача '{task["text"]}' отмечена как выполненная")
        
    def delete_task(self, task_id: int):
        # удаление задачи из списка, присвоение новых номеров оставшимся задачам
        for task in self.todo_list:
            if task["id"] == task_id:
                self.todo_list.remove(task)
                print(f"Задача '{task["text"]}' удалена")
        for index, task in enumerate(self.todo_list):
            task["id"] = index

    def delete_completed_tasks(self):
        # удаление всех выполненных задач, присвоение новых номеров оставшимся задачам
        completed = False
        for task in self.todo_list[:]:
            if task["status"] == True:
                self.todo_list.remove(task)
                completed = True
        if completed:
            print("Все выполненные задачи удалены")
        else:
            print(f"Выполненных задач в списке не найдено")
        for index, task in enumerate(self.todo_list):
            task["id"] = index

    def edit_task_text(self, task_id: int):
        # изменение текста задачи
        for task in self.todo_list:
            if task["id"] == task_id:
                old_text = task["text"]
                task["text"] = self.get_task()
                print(f"Текст задачи {task_id + 1} изменен с '{old_text}' на '{task["text"]}'")