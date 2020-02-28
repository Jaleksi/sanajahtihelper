grid = [['a', 'b', 'p', 'r'],
        ['x', 'a', 'e', 'o'],
        ['x', 's', 'm', 'i'],
        ['i', 'm', 's', 'v']]

words = ['aasi', 'jalkapallo']

class GridFinder:
    def __init__(self, words, grid):
        self.words = words
        self.grid = grid
    
    def word_in_grid(self, word):
        if not self.lazy_check(word):
            return False

        first_letter_indexes = self.letter_indexes_in_grid(word[0])

        for index in first_letter_indexes:
            print('*', index, self.grid[index[0]][index[1]])
            if self.index_neighbours(index, word, 0):
                return True
        return False

    def letter_indexes_in_grid(self, letter):
        '''
        Loops through grid and finds all indexes where
        given letter appears.

        IN: letter, string
        OUT: list of indexes
        '''
        indexes = []
        for x in range(4):
            for y in range(4):
                if grid[x][y] == letter:
                    indexes.append((x, y))
        return indexes

    def lazy_check(self, word):
        '''
        Quick check to see if doing bigger search is worth it.
        Checks if all letters in given word appear in grid.

        IN: word, string
        OUT: boolean
        '''
        unpacked_grid = [letter for row in self.grid for letter in row]
        for letter in word:
            if letter not in unpacked_grid:
                return False
        return True

    def index_neighbours(self, index, word, letter_index):
        if letter_index+1 == len(word):
            return True
        x, y = index
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if (self.grid[x+i][y+j] == word[letter_index + 1] and
                        abs(i) + abs(j) != 0):
                        print(f'({x+i}, {y+j}), {word[letter_index+1]}')
                        if self.index_neighbours((x+i, y+j), word, letter_index + 1):
                            return True

                except IndexError:
                    continue
        return False
grid_finder = GridFinder(words, grid)

print(grid_finder.word_in_grid("resep"))
