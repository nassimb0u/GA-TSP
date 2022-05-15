from collections import deque

from individual import Individual


class Population:
    def __init__(self, ag):
        self.ag = ag
        self.individuals = deque(maxlen=ag.pop_size)
        self.total_fitness = 0
        self.probas = None

    @staticmethod
    def create_rand(ag):
        rand_pop = Population(ag)
        for _ in range(ag.pop_size):
            rand_pop.insert(Individual.create_rand(ag))
        return rand_pop

    def __len__(self):
        return len(self.individuals)

    def insert(self, individ):
        if len(self.individuals) == self.individuals.maxlen and len(self.individuals):
            self.total_fitness -= self.individuals.popleft().fitness
        self.individuals.append(individ)
        self.total_fitness += individ.fitness

    def setup_probas(self):
        self.probas = [e.fitness / self.total_fitness for e in self.individuals]

    def roulette_selection(self):
        return self.ag.rng.choice(self.individuals, p=self.probas)

    def select_pair(self):
        return self.roulette_selection(), self.roulette_selection()

    def elitism(self):
        return sorted(self.individuals, reverse=True)

    def __str__(self):
        return "\n".join(
            [f"total_fitness: {self.total_fitness}"]
            + [str(individ) for individ in self.individuals]
        )
