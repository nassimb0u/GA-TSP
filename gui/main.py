from tkinter import Tk

from conf_matrix_frame import ConfMatrixFrame

root = Tk()
root.title("TSP avec AG")
dynamix_matrix = ConfMatrixFrame(
    root,
    "Matrice des distances",
    "Nombre de villes",
    2,
    15,
    "0",
    ConfMatrixFrame.is_float,
    "Veuillez entrer un nombre réel",
)
dynamix_matrix.grid(row=0, column=0, padx=5, pady=5)
root.mainloop()
