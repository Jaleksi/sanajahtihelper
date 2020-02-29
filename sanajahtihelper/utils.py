from .word_widget import FoundWord


class GridFinder:
    def __init__(self):
        self.words = self.load_words()

    def load_words(self):
        with open('./sanajahtihelper/data/finnish_words.txt', 'r',
        encoding='utf-8') as _file:
            data = _file.read()
        return data.replace(',', '').replace('\ufeff', '').split()

    def search(self, grid):
        found_words = []
        self.grid = grid
        for word in self.words:
            if self.word_in_grid(word):
                found_words.append(FoundWord(word, self.found_indexes))
        return found_words

    def word_in_grid(self, word):
        if not self.lazy_check(word):
            return False
        first_letter_indexes = self.letter_indexes_in_grid(word[0])

        for index in first_letter_indexes:
            self.found_indexes = [index]
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
                if self.grid[x][y] == letter:
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
        '''
        Recursively checks if given grid-index' neighbours include next letter.

        IN: index in grid (x, y), word string, current letters' index in word
        OUT: boolean, is the word in grid
        '''
        if letter_index+1 == len(word):
            return True
        x, y = index
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if (self.grid[x+i][y+j] == word[letter_index + 1] and
                        abs(i) + abs(j) != 0):
                        self.found_indexes.append((x+i, y+j))
                        if self.index_neighbours((x+i, y+j), word, letter_index + 1):
                            return True
                # IndexError happens when trying to go out of bounds in grid
                except IndexError:
                    continue
        return False
