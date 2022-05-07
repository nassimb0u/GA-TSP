from tkinter import CENTER, Tk
from tkinter import ttk


class DynamicMatrixFrame:
    class SizeFrame:
        def __init__(self, root, label, max_size, command):
            self.root = root
            self.label = ttk.Label(root, text=label)
            self.label.grid(row=0, column=0)
            self.input = ttk.Combobox(
                root, values=list(range(1, max_size + 1)), width=5
            )
            self.input.grid(row=1, column=0, pady=5)
            self.button = ttk.Button(root, text="Ok", command=command)
            self.button.grid(row=2, column=0, pady=5)

        def get_size(self):
            return int(self.input.get())

    class MatrixFrame:
        def __init__(self, root, n):
            self.root = root
            self.cells = [[None] * n for _ in range(n)]
            self.n = n
            for i in range(n):
                for j in range(n):
                    self.cells[i][j] = ttk.Entry(self.root, justify=CENTER, width=5)
                    self.cells[i][j].grid(row=i, column=j)

        def delete(self):
            for i in range(self.n):
                for j in range(self.n):
                    self.cells[i][j].destroy()

    def __init__(self, root, label, max_size):
        self.size_wrapper = ttk.Frame(root)
        self.size_wrapper.grid(row=0, column=1, padx=5, pady=5)
        self.size_frame = DynamicMatrixFrame.SizeFrame(
            self.size_wrapper, label, max_size, self.reload
        )
        self.matrix_wrapper = ttk.Frame(root)
        self.matrix_wrapper.grid(row=0, column=0, padx=5, pady=5)
        self.matrix = None

    def reload(self):
        if self.matrix:
            self.matrix.delete()
        self.matrix = DynamicMatrixFrame.MatrixFrame(
            self.matrix_wrapper, self.size_frame.get_size()
        )


root = Tk()
root.title("TSP avec AG")
dynamix_matrix = DynamicMatrixFrame(root, "Nombre de villes", 10)
root.mainloop()
