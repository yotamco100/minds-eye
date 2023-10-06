# A generic Grapher interface

class Grapher:
    def __init__(self, filename, tree):
        self.filename = filename
        self.tree = tree
    
    def generate_graph(self):
        raise NotImplementedError("This is a generic interface. Please implement a Grapher object.")

    def save_graph(self):
        raise NotImplementedError("This is a generic interface. Please implement a Grapher object.")
