from graph import Graph
from ag import AG

m = [
    [0, 2, 4, 12, 5],
    [2, 0, 4, 8, 7],
    [4, 4, 0, 3, 3],
    [12, 8, 3, 0, 10],
    [5, 7, 3, 10, 0],
]
g = Graph(m)
ag = AG(g, population_size=50)
gen_count, gen = ag.solve()
print("gen_count", gen_count)
print(gen)
print("best")
print(gen.elitism()[-1])
