class Counter:
    def __init__(self):
        self.counter = 0

    def incr(self):
        self.counter += 1

    def curr(self):
        return self.counter

    def __str__(self):
        return str(self.counter)