import textwrap
from tkinter import CENTER, END, ttk


class MatrixFrame(ttk.Frame):
    def __init__(
        self,
        master,
        sizex,
        sizey,
        label,
        default_value="",
        validator=lambda v: True,
        error_message="",
    ):
        super().__init__(master)
        label = textwrap.shorten(label, width=6 * sizex, placeholder="...")
        error_message = textwrap.shorten(
            error_message, width=6 * sizex, placeholder="..."
        )
        self.label = ttk.Label(self, text=label)
        self.label.grid(row=0, column=0, columnspan=sizex, pady=5)
        self.cells = [[None] * sizex for _ in range(sizey)]
        self.error_label = ttk.Label(self, foreground="red")
        self.error_label.grid(row=sizey + 1, column=0, columnspan=sizex, pady=5)

        def validator_wrapper(v):
            if validator(v):
                self._clear_error()
                return True
            self._show_error(error_message)
            return False

        vcmd = (self.register(validator_wrapper), "%P")
        for i in range(sizex):
            for j in range(sizey):
                self.cells[i][j] = ttk.Entry(
                    self,
                    justify=CENTER,
                    width=5,
                    validate="key",
                    validatecommand=vcmd,
                )
                self.cells[i][j].insert(END, default_value)
                self.cells[i][j].grid(row=i + 1, column=j)

    def _show_error(self, message):
        self.error_label["text"] = message

    def _clear_error(self):
        self._show_error("")


class DistancesMatrix(MatrixFrame):
    def __init__(self, master, size) -> None:
        super().__init__(
            master,
            size,
            size,
            "Matrice des distances",
            "0",
            DistancesMatrix.is_distance,
            "Veuillez entrer une distance valide",
        )

    @staticmethod
    def is_distance(v):
        if v == "":
            return True
        try:
            assert float(v) >= 0
        except (AssertionError, ValueError):
            return False
        return True


class ComboboxFrame(ttk.Frame):
    def __init__(self, master, label, min_size, max_size, on_validate):
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
        self.button = ttk.Button(
            self, text="Ok", command=lambda: on_validate(master, self.get())
        )
        self.button.grid(row=2, column=0, pady=5)

    def get(self):
        return int(self.input.get())


class MatrixSizeFrame(ComboboxFrame):
    def __init__(self, master, on_validate):
        super().__init__(master, "Nombre de villes", 1, 15, on_validate)
