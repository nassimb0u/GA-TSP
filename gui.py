import textwrap
from tkinter import CENTER, END, Tk, ttk
import tkinter as tk


class DynamicMatrixFrame(ttk.Frame):
    class SizeFrame(ttk.Frame):
        def __init__(self, master, label, min_size, max_size, command):
            super().__init__(master)
            self.label = ttk.Label(self, text=label)
            self.label.grid(row=0, column=0)
            self.input = ttk.Combobox(
                self,
                values=list(range(min_size, max_size + 1)),
                width=5,
                state="readonly",
            )
            self.input.current(0)
            self.input.grid(row=1, column=0, pady=5)
            self.button = ttk.Button(self, text="Ok", command=command)
            self.button.grid(row=2, column=0, pady=5)

        def get_size(self):
            return int(self.input.get())

    class MatrixFrame(ttk.Frame):
        def __init__(
            self,
            master,
            n,
            label,
            default_value=None,
            validator=lambda v: True,
            error_message="",
        ):
            super().__init__(master)
            label = textwrap.shorten(label, width=6 * n, placeholder="...")
            error_message = textwrap.shorten(
                error_message, width=6 * n, placeholder="..."
            )
            self.label = ttk.Label(self, text=label)
            self.label.grid(row=0, column=0, columnspan=n, pady=5)
            self.cells = [[None] * n for _ in range(n)]
            self.n = n
            self.error_label = ttk.Label(self, foreground="red")
            self.error_label.grid(row=n + 1, column=0, columnspan=n, pady=5)

            def validator_wrapper(v):
                if validator(v):
                    self._clear_error()
                    return True
                self._show_error(error_message)
                return False

            vcmd = (self.register(validator_wrapper), "%P")
            for i in range(n):
                for j in range(n):
                    self.cells[i][j] = ttk.Entry(
                        self,
                        justify=CENTER,
                        width=5,
                        validate="key",
                        validatecommand=vcmd,
                    )
                    if default_value:
                        self.cells[i][j].insert(END, default_value)
                    self.cells[i][j].grid(row=i + 1, column=j)

        def delete(self):
            self.label.destroy()
            self.error_label.destroy()
            for i in range(self.n):
                for j in range(self.n):
                    self.cells[i][j].destroy()

        def _show_error(self, message):
            self.error_label["text"] = message

        def _clear_error(self):
            self._show_error("")

    def __init__(
        self,
        master,
        matrix_label,
        size_label,
        min_size,
        max_size,
        default_value=None,
        validator=lambda v: True,
        error_message="",
    ):
        super().__init__(master)
        self.size_frame = DynamicMatrixFrame.SizeFrame(
            self, size_label, min_size, max_size, self.reload
        )
        self.size_frame.grid(row=0, column=1, padx=5, pady=5)
        self.matrix_label = matrix_label
        self.default_value = default_value
        self.validator = validator
        self.error_message = error_message
        self.matrix = None

    def reload(self):
        if self.matrix:
            self.matrix.delete()
        self.matrix = DynamicMatrixFrame.MatrixFrame(
            self,
            self.size_frame.get_size(),
            self.matrix_label,
            self.default_value,
            self.validator,
            self.error_message,
        )
        self.matrix.grid(row=0, column=0, padx=5, pady=5)

    @staticmethod
    def is_float(v):
        if v == "" or v == "-":
            return True
        try:
            float(v)
        except ValueError:
            return False
        return True


root = Tk()
root.title("TSP avec AG")
dynamix_matrix = DynamicMatrixFrame(
    root,
    "Matrice des distances",
    "Nombre de villes",
    2,
    15,
    "0",
    DynamicMatrixFrame.is_float,
    "Veuillez entrer un nombre réel",
)
dynamix_matrix.grid(row=0, column=0, padx=5, pady=5)
root.mainloop()
