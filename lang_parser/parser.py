class GenericParser:
    "A generic parsing interface."
    def __init__(self, filename, mode = 'r'):
        self.filename = filename
        self.raw_content = None
        with open(filename, mode) as f:
            self.raw_content = f.read()
    
    def parse(self):
        raise NotImplementedError("This is a generic interface. Please implement a Parser object.")