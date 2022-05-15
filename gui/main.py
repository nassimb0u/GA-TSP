from tkinter import Tk

from distances_matrix import DistancesMatrix, MatrixSizeFrame


def start(master, size):
    matrix = DistancesMatrix(master, size)
    matrix.grid(row=0, column=0, padx=5, pady=5)


root = Tk()
root.title("TSP avec AG")
matrix_size = MatrixSizeFrame(root, start)
matrix_size.grid(row=0, column=0, padx=5, pady=5)
root.mainloop()
