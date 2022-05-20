from functools import total_ordering
from random import randint


@total_ordering
class Individual:
    def __init__(self, ga):
        self.ga = ga
        self.genes = [None] * ga.order
        self.distance = None
        self.fitness = None

    @staticmethod
    def create_rand(ga):
        individ = Individual(ga)
        individ.genes = list(ga.rng.permutation(ga.order))
        individ.calc_fitness()
        return individ

    def calc_fitness(self):
        tmp = 0
        for i in range(self.ga.order - 1):
            tmp += self.ga.adj_mat[self.genes[i]][self.genes[i + 1]]
        tmp += self.ga.adj_mat[self.genes[-1]][self.genes[0]]
        self.distance = tmp
        self.fitness = 1 / tmp

    @staticmethod
    def crossover(p1, p2):
        # Order Crossover Operator
        assert p1.ga == p2.ga
        ga = p1.ga
        o1, o2 = Individual(ga), Individual(ga)
        cp1, cp2 = sorted([randint(0, ga.order - 1), randint(0, ga.order - 1)])
        so1, so2 = set(), set()
        for i in range(cp1, cp2 + 1):
            o1.genes[i] = p1.genes[i]
            so1.add(o1.genes[i])
            o2.genes[i] = p2.genes[i]
            so2.add(o2.genes[i])
        ip1 = ip2 = (cp2 + 1) % ga.order
        for i in range(cp2 + 1, cp2 + 1 + ga.order - (cp2 - cp1 + 1)):
            while p2.genes[ip2] in so1:
                ip2 = (ip2 + 1) % ga.order
            o1.genes[i % ga.order] = p2.genes[ip2]
            ip2 = (ip2 + 1) % ga.order
            while p1.genes[ip1] in so2:
                ip1 = (ip1 + 1) % ga.order
            o2.genes[i % ga.order] = p1.genes[ip1]
            ip1 = (ip1 + 1) % ga.order
        o1.calc_fitness()
        o2.calc_fitness()
        return o1, o2

    def mutate(self):
        i1, i2 = randint(0, self.ga.order - 1), randint(0, self.ga.order - 1)
        self.genes[i1], self.genes[i2] = self.genes[i2], self.genes[i1]
        self.calc_fitness()

    def __eq__(self, __o):
        return self.fitness == __o.fitness

    def __lt__(self, __o):
        return self.fitness < __o.fitness

    def __str__(self):
        return f"{self.genes} distance: {self.distance} fitness: {self.fitness}"
