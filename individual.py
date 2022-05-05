from functools import total_ordering
from random import randint


@total_ordering
class Individual:
    def __init__(self, ag):
        self.ag = ag
        self.genes = [None] * ag.order
        self.distance = None
        self.fitness = None

    @staticmethod
    def create_rand(ag):
        individ = Individual(ag)
        individ.genes = list(ag.rng.permutation(ag.order))
        individ.calc_fitness()
        return individ

    def calc_fitness(self):
        tmp = 0
        for i in range(self.ag.order - 1):
            tmp += self.ag.adj_mat[self.genes[i]][self.genes[i + 1]]
        tmp += self.ag.adj_mat[self.genes[-1]][self.genes[0]]
        self.distance = tmp
        self.fitness = 1 / tmp

    @staticmethod
    def crossover(p1, p2):
        # Order Crossover Operator
        assert p1.ag == p2.ag
        ag = p1.ag
        o1, o2 = Individual(ag), Individual(ag)
        cp1, cp2 = sorted([randint(0, ag.order - 1), randint(0, ag.order - 1)])
        so1, so2 = set(), set()
        for i in range(cp1, cp2 + 1):
            o1.genes[i] = p1.genes[i]
            so1.add(o1.genes[i])
            o2.genes[i] = p2.genes[i]
            so2.add(o2.genes[i])
        ip1 = ip2 = (cp2 + 1) % ag.order
        for i in range(cp2 + 1, cp2 + 1 + ag.order - (cp2 - cp1 + 1)):
            while p2.genes[ip2] in so1:
                ip2 = (ip2 + 1) % ag.order
            o1.genes[i % ag.order] = p2.genes[ip2]
            ip2 = (ip2 + 1) % ag.order
            while p1.genes[ip1] in so2:
                ip1 = (ip1 + 1) % ag.order
            o2.genes[i % ag.order] = p1.genes[ip1]
            ip1 = (ip1 + 1) % ag.order
        o1.calc_fitness()
        o2.calc_fitness()
        return o1, o2

    def mutate(self):
        i1, i2 = randint(0, self.ag.order - 1), randint(0, self.ag.order - 1)
        self.genes[i1], self.genes[i2] = self.genes[i2], self.genes[i1]
        self.calc_fitness()

    def __eq__(self, __o):
        return self.fitness == __o.fitness

    def __lt__(self, __o):
        return self.fitness < __o.fitness

    def __str__(self):
        return f"{self.genes} distance: {self.distance} fitness: {self.fitness}"
