from tkinter import Tk, Toplevel, ttk

from ag import AG
from graph import Graph
from gui.ag_parameters_frame import AGParametersFrame
from gui.distances_matrix import DistancesMatrix, MatrixSizeFrame
from gui.solutions_frame import SolutionsFrame


def start(master, size):
    matrix = DistancesMatrix(master, size)
    matrix.grid(row=0, column=0, padx=10, pady=10)
    ag_parameters = AGParametersFrame(master)
    ag_parameters.grid(row=0, column=1, padx=10, pady=10)

    def run():
        solution_window = Toplevel(master)
        m = matrix.get_distances_matrix()
        g = Graph(m)
        ag = AG(
            g,
            ag_parameters.get_population_size(),
            ag_parameters.get_crossover_rate(),
            ag_parameters.get_mutation_rate(),
        )
        gen_count, population = ag.solve()
        solutions_frame = SolutionsFrame.from_population(solution_window, population)
        solutions_frame.grid(row=0, column=0, padx=10, pady=10)

    run = ttk.button = ttk.Button(master, text="Exécuter", command=run)
    run.grid(row=1, column=1, padx=10, pady=10)


root = Tk()
root.title("TSP avec AG")
matrix_size = MatrixSizeFrame(root, start)
matrix_size.grid(row=0, column=0, padx=5, pady=5)
root.mainloop()
