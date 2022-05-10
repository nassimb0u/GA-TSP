import textwrap
from tkinter import CENTER, END, Tk, ttk


class DynamicMatrixFrame:
    class SizeFrame:
        def __init__(self, root, label, min_size, max_size, command):
            self.root = root
            self.label = ttk.Label(root, text=label)
            self.label.grid(row=0, column=0)
            self.input = ttk.Combobox(
                root,
                values=list(range(min_size, max_size + 1)),
                width=5,
                state="readonly",
            )
            self.input.current(0)
            self.input.grid(row=1, column=0, pady=5)
            self.button = ttk.Button(root, text="Ok", command=command)
            self.button.grid(row=2, column=0, pady=5)

        def get_size(self):
            print(self.input.get())
            return int(self.input.get())

    class MatrixFrame:
        def __init__(self, root, n, label):
            self.root = root
            label = textwrap.shorten(label, width=6 * n, placeholder="...")
            self.label = ttk.Label(root, text=label)
            self.label.grid(row=0, column=0, columnspan=n, pady=5)
            self.cells = [[None] * n for _ in range(n)]
            self.n = n
            for i in range(n):
                for j in range(n):
                    self.cells[i][j] = ttk.Entry(root, justify=CENTER, width=5)
                    self.cells[i][j].insert(END, 0)
                    self.cells[i][j].grid(row=i + 1, column=j)

        def delete(self):
            self.label.destroy()
            for i in range(self.n):
                for j in range(self.n):
                    self.cells[i][j].destroy()

    def __init__(self, root, matrix_label, size_label, min_size, max_size):
        self.size_wrapper = ttk.Frame(root)
        self.size_wrapper.grid(row=0, column=1, padx=5, pady=5)
        self.size_frame = DynamicMatrixFrame.SizeFrame(
            self.size_wrapper, size_label, min_size, max_size, self.reload
        )
        self.matrix_wrapper = ttk.Frame(root)
        self.matrix_wrapper.grid(row=0, column=0, padx=5, pady=5)
        self.matrix_label = matrix_label
        self.matrix = None

    def reload(self):
        if self.matrix:
            self.matrix.delete()
        self.matrix = DynamicMatrixFrame.MatrixFrame(
            self.matrix_wrapper, self.size_frame.get_size(), self.matrix_label
        )


root = Tk()
root.title("TSP avec AG")
dynamix_matrix_wrapper = ttk.Frame(root)
dynamix_matrix_wrapper.grid(row=0, column=0, padx=5, pady=5)
dynamix_matrix = DynamicMatrixFrame(
    dynamix_matrix_wrapper, "Matrice des distances", "Nombre de villes", 2, 15
)
root.mainloop()
