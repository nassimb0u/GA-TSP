class Graph:
    def __init__(self, adj_mat):
        self.adj_mat = adj_mat

    @property
    def order(self):
        return len(self.adj_mat)
