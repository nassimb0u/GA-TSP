import textwrap
from tkinter import CENTER, ttk, NO


class SolutionsFrame(ttk.Frame):
    def __init__(self, master, solution_width):
        super().__init__(master)
        self.solutions_table = ttk.Treeview(
            self, columns=("solution", "distance_totale", "fitness")
        )
        self.solutions_table.column("#0", width=0, stretch=NO)
        print(solution_width)
        self.solutions_table.column(
            "solution", anchor=CENTER, width=solution_width * 2 * 12
        )
        self.solutions_table.column("distance_totale", anchor=CENTER, width=180)
        self.solutions_table.column("fitness", anchor=CENTER, width=120)
        self.solutions_table.heading("#0", text="", anchor=CENTER)
        self.solutions_table.heading("solution", text="Solution", anchor=CENTER)
        self.solutions_table.heading(
            "distance_totale", text="Distance Totale", anchor=CENTER
        )
        self.solutions_table.heading("fitness", text="Fitness", anchor=CENTER)
        self.table_scroll = ttk.Scrollbar(
            self, orient="vertical", command=self.solutions_table.yview
        )
        self.table_scroll.pack(side="right", fill="y")
        self.solutions_table.configure(yscrollcommand=self.table_scroll.set)
        self.solutions_table.pack()

    @staticmethod
    def from_population(master, population):
        solutions_frame = SolutionsFrame(master, population.ag.order)
        i = 0
        for solution in population.elitism():
            genes = "-".join(map(str, solution.genes))
            solutions_frame.solutions_table.insert(
                parent="",
                index=i,
                iid=i,
                text="",
                values=(
                    genes,
                    str(solution.distance),
                    "{:.4f}".format(solution.fitness),
                ),
            )
            i += 1
        return solutions_frame
