import time
from abc import abstractmethod


def timer(func):
    def wrapper_timer(*args, **kwargs):
        tic = time.process_time()
        value = func(*args, **kwargs)
        toc = time.process_time()
        return value, toc - tic

    return wrapper_timer


class TSP:
    def __init__(self, graph):
        self.g = graph
        self.solution = None, [None] * graph.order

    @property
    def adj_mat(self):
        return self.g.adj_mat

    @property
    def order(self):
        return self.g.order

    @abstractmethod
    def solve(self):
        pass
