from entities.Todo import Todo
from repositories.TodoRepository import TodoRepository

class TodoService():
    def __init__(self, todo_repository: TodoRepository):
        self.todo_repository = todo_repository

    def show_todos(self):
        todos = self.todo_repository.get_all_todos()
        print("Daftar Todo:")
        if not todos:
            print("- Data todo belum tersedia!")
            return

        for counter, todo in enumerate(todos, start=1):
            print(todo)

    def add_todo(self, title: str):
        new_todo = Todo(title=title)
        self.todo_repository.add_todo(new_todo)

    def remove_todo(self, id: int):
        success = self.todo_repository.remove_todo(id)
        if not success:
            print(f"[!] Gagal menghapus todo dengan ID: {id}.")

    def update_todo(self, id: int, title: str):
        todos = self.todo_repository.get_all_todos()
        for todo in todos:
            if todo.id == id:
                todo.title = title
                return
        print(f"[!] Gagal mengubah todo dengan ID: {id}.")

    def search_todo(self, keyword: str):
        todos = self.todo_repository.get_all_todos()
        print("Hasil Pencarian:")
        found = False
        for todo in todos:
            if keyword.lower() in todo.title.lower():
                print(todo)
                found = True
        if not found:
            print("- Data todo tidak ditemukan!")

    def sort_todo(self):
        todos = self.todo_repository.get_all_todos()
        todos.sort(key=lambda todo: todo.title.lower())
