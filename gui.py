import tkinter as tk
from tkinter import messagebox
from classes import Task, TaskManager


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Менеджер задач")
        self.root.geometry("480x440")
        self.manager = TaskManager()
        self.setup_ui()

    def setup_ui(self):
        # Название
        tk.Label(self.root, text="Название задачи:").grid(row=0, column=0, padx=8, pady=6, sticky="e")
        self.title_entry = tk.Entry(self.root, width=36)
        self.title_entry.grid(row=0, column=1, padx=8, pady=6)

        # Описание
        tk.Label(self.root, text="Описание:").grid(row=1, column=0, padx=8, pady=6, sticky="ne")
        self.desc_text = tk.Text(self.root, width=36, height=5)
        self.desc_text.grid(row=1, column=1, padx=8, pady=6)

        # Срок
        tk.Label(self.root, text="Срок (ГГГГ-ММ-ДД):").grid(row=2, column=0, padx=8, pady=6, sticky="e")
        self.date_entry = tk.Entry(self.root, width=36)
        self.date_entry.grid(row=2, column=1, padx=8, pady=6)

        # Кнопки
        btn_frame = tk.Frame(self.root)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=8)
        tk.Button(btn_frame, text="Добавить задачу", width=18, command=self.add_task).pack(side="left", padx=6)
        tk.Button(btn_frame, text="Удалить задачу", width=18, command=self.delete_task).pack(side="left", padx=6)

        # Список задач
        self.tasks_listbox = tk.Listbox(self.root, width=70, height=12)
        self.tasks_listbox.grid(row=4, column=0, columnspan=2, padx=8, pady=8)

        self.update_listbox()

    def add_task(self):
        title = self.title_entry.get().strip()
        description = self.desc_text.get("1.0", tk.END).strip()
        due_date = self.date_entry.get().strip()

        if not (title and description and due_date):
            messagebox.showwarning("Ошибка", "Заполните все поля!")
            return

        t = Task(title, description, due_date)
        self.manager.add_task(t)
        self.update_listbox()
        self.clear_inputs()

    def delete_task(self):
        sel = self.tasks_listbox.curselection()
        if not sel:
            messagebox.showinfo("Информация", "Выберите задачу для удаления.")
            return
        idx = sel[0]
        self.manager.delete_task(idx)
        self.update_listbox()

    def update_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.manager.tasks:
            self.tasks_listbox.insert(tk.END, f"{task.title} — до {task.due_date}")

    def clear_inputs(self):
        self.title_entry.delete(0, tk.END)
        self.desc_text.delete("1.0", tk.END)
        self.date_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()