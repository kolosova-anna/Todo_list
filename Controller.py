from Model import TodoList
from View import TodoView

class TodoController():
    # обрабатывает пользовательский ввод, вызывает соответствующие методы TodoList и обновляет TodoView
    
    def __init__(self, todo_list: list):
        self.todo_list: list = todo_list.todo_list
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
                for task in self.todo_list:
                    if task["id"] == (task_id - 1):
                        return task_id - 1
                print(f"Задача под номером {task_id} не найдена")
            except ValueError:
                print("Ошибка ввода")

    def get_number(self):
    # получение числа от пользователя (выбранный пункт меню)
        print("\nВведите число, соответствующее выбранному пункту меню:\n")
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