from tkinter import CENTER, END, ttk


class AGParametersFrame(ttk.Frame):
    size_error_message = "Veuillez entrer une taille valide"
    rate_error_message = "Veuillez entrer une probabilité"

    class Entry(ttk.Frame):
        def __init__(
            self,
            master,
            label,
            default_value="",
            validator=lambda v: True,
            error_message="",
        ):
            super().__init__(master)
            self.label = ttk.Label(self, text=label)
            self.label.grid(row=0, column=0)
            self.error_label = ttk.Label(self, foreground="red")
            self.error_label.grid(row=2, column=0)

            def validator_wrapper(v):
                if validator(v):
                    self._clear_error()
                    return True
                self._show_error(error_message)
                return False

            vcmd = (self.register(validator_wrapper), "%P")
            self.input = ttk.Entry(
                self, justify=CENTER, width=5, validate="key", validatecommand=vcmd
            )
            self.input.insert(END, default_value)
            self.input.grid(row=1, column=0)

        def get(self):
            return self.info.get()

        def _show_error(self, message):
            self.error_label["text"] = message

        def _clear_error(self):
            self._show_error("")

    def __init__(self, master):
        super().__init__(master)
        self.crossover_rate = AGParametersFrame.Entry(
            self,
            "Taux de croisement",
            "0.8",
            AGParametersFrame.is_rate,
            AGParametersFrame.rate_error_message,
        )
        self.crossover_rate.grid(row=0, column=1)
        self.mutation_rate = AGParametersFrame.Entry(
            self,
            "Taux de mutation",
            "0.001",
            AGParametersFrame.is_rate,
            AGParametersFrame.rate_error_message,
        )
        self.mutation_rate.grid(row=2, column=1)
        self.pop_size = AGParametersFrame.Entry(
            self,
            "Taille de la population",
            "20",
            AGParametersFrame.is_size,
            AGParametersFrame.rate_error_message,
        )
        self.pop_size.grid(row=3, column=1)

    @staticmethod
    def is_rate(v):
        if v == "":
            return True
        try:
            rate = float(v)
            assert rate >= 0 and rate <= 1
        except (ValueError, AssertionError):
            return False
        return True

    @staticmethod
    def is_size(v):
        if v == "":
            return True
        try:
            assert int(v) > 0
        except (ValueError, AssertionError):
            return False
        return True
