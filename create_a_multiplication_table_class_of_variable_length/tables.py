class MultiplicationTable:
    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
        their calculations (form of caching)"""
        self.length = length
        self._table = [
            [str(num * num2) for num2 in range(1, self.length + 1)]
            for num in range(1, self.length + 1)
        ]

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return len(self._table)*len(self._table)

    def __str__(self):
        """Returns a string representation of the table"""
        return '\n'.join([' | '.join(row) for row in self._table])


    def calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""
        return int(self._table[x-1][y-1])
