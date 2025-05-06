import tabulate as tl

class TodoView():
    # отвечает за отображение списка задач, взаимодействие с пользователем
    
    def __init__(self, todo_list: list):
        # свойства числа
        self.todo_list: list = todo_list.todo_list
        #self.number = 0
    
    def print_tasks(self):
        # вывод списка задач
        if not self.todo_list:
            print("Список задач пуст")
        print("Список задач:")
        headers = ["№", "Задача", "Статус"]
        rows = []
        for task in self.todo_list:
            rows.append([task["id"] + 1, task["text"], "Выполнено" if task["status"] else "Не выполнено"])
        print(tl.tabulate(rows, headers=headers, tablefmt="grid"))

    def print_completed_tasks(self):
        # вывод выполненных задач из списка
        completed = False
        print("Выполненные задачи:")
        headers = ["№", "Задача"]
        rows = []
        for task in self.todo_list:
            if task["status"] == True:
                rows.append([task["id"] + 1, task["text"]])
                completed = True
        print(tl.tabulate(rows, headers=headers, tablefmt="grid"))
        if not completed:
            print("Нет выполненных задач")

    def print_pending_tasks(self):
        # вывод невыполненных задач из списка
        pending = False
        print("Активные задачи:")
        headers = ["№", "Задача"]
        rows = []
        for task in self.todo_list:
            if task["status"] == False:
                rows.append([task["id"] + 1, task["text"]])
                pending = True
        print(tl.tabulate(rows, headers=headers, tablefmt="grid"))
        if not pending:
            print("Все задачи выполнены")
