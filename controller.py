from model import TodoList
from view import TodoView

class TodoController():
    # обрабатывает пользовательский ввод, вызывает соответствующие методы TodoList и обновляет TodoView
    
    def __init__(self, todo_view: TodoView):
        self.todo_view = todo_view
        #self.todo_view = TodoView(self.todo_list)

    def get_number(self) -> str:
    # получение числа от пользователя (выбранный пункт меню)
        print("\nВведите число, соответствующее выбранному пункту меню:\n")
        self.number = self.todo_view.check_input()
        return str(self.number)
    
    def get_task(self) -> str: 
        # запрашиваем новую задачу у пользователя для добавления в список
        return input("Введите текст задачи:\n")
    
    def run(self) -> None:
    # выводит меню пользователю и вызывает соответствующие функции классов TodoList, TodoView и TodoController
        todo_list = TodoList()
        view = TodoView(todo_list)
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
            choice = self.get_number()
            match choice:
                case '1':
                    task = self.get_task()
                    view.pass_task(task)
                case '2':
                    view.show_tasks()
                case '3':
                    view.show_tasks(False)
                case '4':
                    view.show_tasks(True)
                case '5':
                    task_id = view.pass_check_task_id()
                    view.pass_change_task_status(task_id)
                case '6':
                    task_id = view.pass_check_task_id()
                    text = self.get_task()
                    view.pass_edit_task_text(task_id, text)
                case '7':
                    task_id = view.pass_check_task_id()
                    view.pass_delete_task(task_id)
                case '8':
                    view.pass_delete_completed_tasks()
                case '0':
                    break
                case _:
                    print("Раздел с введенным номером не найден")