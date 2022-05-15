from tkinter import Tk

from ag_parameters_frame import AGParametersFrame
from distances_matrix import DistancesMatrix, MatrixSizeFrame


def start(master, size):
    matrix = DistancesMatrix(master, size)
    matrix.grid(row=0, column=0, padx=10, pady=10)
    ag_parameters = AGParametersFrame(master)
    ag_parameters.grid(row=0, column=1, padx=10, pady=10)


root = Tk()
root.title("TSP avec AG")
matrix_size = MatrixSizeFrame(root, start)
matrix_size.grid(row=0, column=0, padx=5, pady=5)
root.mainloop()
