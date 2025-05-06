class Task():
    # содержит свойства для описания задачи и её статуса
    
    def __init__(self, task_id, text, status=False):
        # свойства задачи и статуса
        self.task_id = task_id
        self.text = text
        self.status = status


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

    def change_task_status(self, task_id):
        # изменение статуса задачи
        #task_id = TodoController.get_task_id(self)
        for task in self.todo_list:
            if task["id"] == task_id:
                task["status"] = True
                print(f"Задача '{task["text"]}' отмечена как выполненная")
        
    def delete_task(self, task_id):
        # удаление задачи из списка
        for task in self.todo_list:
            if task["id"] == task_id:
                self.todo_list.remove(task)
                print(f"Задача '{task["text"]}' удалена")

    def delete_completed_tasks(self):
        # удаление всех выполненных задач
        completed = False
        for task in self.todo_list[:]:
            if task["status"] == True:
                self.todo_list.remove(task)
                completed = True
        if completed:
            print("Все выполненные задачи удалены")
        else:
            print(f"Выполненных задач в списке не найдено")

    def edit_task_text(self, task_id):
        # изменение текста задачи
        for task in self.todo_list:
            if task["id"] == task_id:
                old_text = task["text"]
                task["text"] = self.get_task()
                print(f"Текст задачи {task_id + 1} изменен с '{old_text}' на '{task["text"]}'")


class TodoView():
    # отвечает за отображение списка задач, взаимодействие с пользователем
    
    def __init__(self, todo_list):
        # свойства числа
        self.todo_list = todo_list.todo_list
        #self.number = 0
    
    def print_tasks(self):
        # вывод списка задач
        if not self.todo_list:
            print("Список задач пуст")
        for task in self.todo_list:
            print(f'№: {task["id"] + 1}, Задача: {task["text"]}, Статус: {task["status"]}')

    def print_completed_tasks(self):
        # вывод выполненных задач из списка
        completed = False
        for task in self.todo_list:
            if task["status"] == True:
                print(f"№: {task["id"] + 1}, Задача: {task["text"]}, Статус: {task["status"]}")
                completed = True
        if not completed:
            print("Нет выполненных задач")

    def print_pending_tasks(self):
        # вывод невыполненных задач из списка
        pending = False
        for task in self.todo_list:
            if task["status"] == False:
                print(f"№: {task["id"] + 1}, Задача: {task["text"]}, Статус: {task["status"]}")
                pending = True
        if not pending:
            print("Все задачи выполнены")

    
class TodoController():
    # обрабатывает пользовательский ввод, вызывает соответствующие методы TodoList и обновляет TodoView
    
    def __init__(self, todo_list):
        self.todo_list = todo_list.todo_list
        #self.todo_view = TodoView(self.todo_list)

    def check_input(self):
    # проверка введенного пользователем числа
        while True:
            try:
                number = int(input())
                return number
            except ValueError:
                print("Ошибка. Введите число")
    
    def check_task_id(self):
        # проверка наличия задачи в списке
        while True:
            try:
                task_id = self.check_input()
                print(f'Принято {task_id}')
                for task in self.todo_list:
                    #print(f'№: {task["id"] + 1}, Задача: {task["text"]}, Статус: {task["status"]}')
                    #print("DEBUG:", self.todo_list)
                    if task["id"] == (task_id - 1):
                        print(f'Отдал {task_id}')
                        return task_id - 1
                print(f"Задача под номером {task_id} не найдена")
            except ValueError:
                print("Ошибка ввода")

    def get_number(self):
    # получение числа от пользователя (выбранный пункт меню)
        print("Введите число, соответствующее выбранному пункту меню:\n")
        self.number = self.check_input()
        return str(self.number)
    
    def get_task_id(self):
        # получения номера задачи для дальнейшей работы с ней
        print("Введите номер задачи:\n")
        task_id = self.check_task_id()
        return task_id


def main():
    # выводит меню пользователю и вызывает соответствующие функции классов TodoList, TodoView и TodoController
    todo_list = TodoList()
    todo_view = TodoView(todo_list)
    controller = TodoController(todo_list)
    print("\n Вас приветствует меню списка задач!")
    print("Выберите нужный раздел меню:")
    print("1. Добавить новую задачу")
    print("2. Показать список всех задач")
    print("3. Показать список активных задач")
    print("4. Показать список выполненных задач")
    print("5. Отметить задачу как выполненную")
    print("6. Редактировать задачу")
    print("7. Удалить задачу")
    print("8. Удалить все выполненные задачи")
    print("0. Выйти")
    while True:
        choice = controller.get_number()
        match choice:
            case '1':
                todo_list.add_task()
            case '2':
                todo_view.print_tasks()
            case '3':
                todo_view.print_pending_tasks()
            case '4':
                todo_view.print_completed_tasks()
            case '5':
                task_id = controller.get_task_id()
                todo_list.change_task_status(task_id)
            case '6':
                task_id = controller.get_task_id()
                todo_list.edit_task_text(task_id)
            case '7':
                task_id = controller.get_task_id()
                todo_list.delete_task(task_id)
            case '8':
                todo_list.delete_completed_tasks()
            case '0':
                break
            case _:
                print("Раздел с введенным номером не найден")

if __name__ == "__main__":
    main()
