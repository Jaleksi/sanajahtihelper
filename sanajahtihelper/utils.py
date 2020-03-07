from .widgets import FoundWord


class GridFinder:
    def __init__(self):
        self.words = self.load_words()

    def load_words(self):
        '''
        Loads almost 100 000 Finnish words to self.words from a text file.
        '''
        with open('./sanajahtihelper/data/finnish_words.txt', 'r', encoding='utf-8') as f:
            data = f.read()
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
        if letter_index + 1 == len(word):
            return True
        x, y = index
        for i in range(-1, 2):
            for j in range(-1, 2):
                if x+i in [0, 1, 2, 3] and y+j in [0, 1, 2, 3]:
                    found_in_neighbour = self.grid[x+i][y+j] == word[letter_index + 1]
                    not_the_same_index = abs(i) + abs(j) != 0
                    already_found = (x+i, y+j) in self.found_indexes
                    if found_in_neighbour and not_the_same_index and not already_found:
                        self.found_indexes.append((x+i, y+j))
                        if self.index_neighbours((x+i, y+j), word, letter_index + 1):
                            return True
        del self.found_indexes[-1]
        return False
