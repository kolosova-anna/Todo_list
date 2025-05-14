from controller import TodoController
from model import TodoList
from view import TodoView

def main() -> None:
    # выводит меню пользователю и вызывает соответствующие функции классов TodoList, TodoView и TodoController
    todo_list = TodoList()
    todo_view = TodoView(todo_list)
    controller = TodoController(todo_view)
    controller.run()

if __name__ == "__main__":
    main()
