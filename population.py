from collections import deque

from individual import Individual


class Population:
    def __init__(self, ag):
        self.ag = ag
        self.population = deque(maxlen=ag.pop_size)
        self.total_fitness = 0
        self.probas = None

    @staticmethod
    def create_rand(ag):
        rand_pop = Population(ag)
        for _ in range(ag.pop_size):
            rand_pop.insert(Individual.create_rand(ag))
        return rand_pop

    def __len__(self):
        return len(self.population)

    def insert(self, individ):
        if len(self.population) == self.population.maxlen and len(self.population):
            self.total_fitness -= self.population.popleft().fitness
        self.population.append(individ)
        self.total_fitness += individ.fitness

    def setup_probas(self):
        self.probas = [e.fitness / self.total_fitness for e in self.population]

    def roulette_selection(self):
        return self.ag.rng.choice(self.population, p=self.probas)

    def select_pair(self):
        return self.roulette_selection(), self.roulette_selection()

    def elitism(self):
        return sorted(self.population)

    def __str__(self):
        return "\n".join(
            [f"total_fitness: {self.total_fitness}"]
            + [str(individ) for individ in self.population]
        )
