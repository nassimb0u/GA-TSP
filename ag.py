from numpy.random import default_rng

from individual import Individual
from population import Population
from tsp import TSP, timer


class AG(TSP):
    def __init__(
        self,
        graph,
        population_size,
        crossover_rate=0.8,
        mutation_rate=1e-3,
        stagnation_metric=5,
    ):
        super().__init__(graph)
        self.pop_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.stagnation_metric = stagnation_metric
        self.rng = default_rng()
        self.init_pop = Population.create_rand(self)

    def crossover_prob(self):
        return self.rng.random() < self.crossover_rate

    def mutation_prob(self):
        return self.rng.random() < self.mutation_rate

    def is_stag(self, gen, new_gen, counter):
        if counter is None:
            counter = self.stagnation_metric
        if new_gen.total_fitness <= gen.total_fitness:
            return counter - 1
        return self.stagnation_metric

    @timer
    def solve(self):
        gen = self.init_pop
        counter = None
        gen_count = 0
        while True:
            gen_count += 1
            gen.setup_probas()
            new_gen = Population(self)
            while len(new_gen) < len(gen):
                p1, p2 = gen.select_pair()
                if self.crossover_prob():
                    o1, o2 = Individual.crossover(p1, p2)
                    if self.mutation_prob():
                        o1.mutate()
                        o2.mutate()
                    new_gen.insert(o1)
                    new_gen.insert(o2)
                else:
                    new_gen.insert(p1)
                    new_gen.insert(p2)
            counter = self.is_stag(gen, new_gen, counter)
            if counter == 0:
                break
            gen = new_gen
        return gen_count, gen
