# tests/test_game.py
from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
            # setup
            new_game = Game()

            # exercise
            grid = new_game.grid

            # verify
            assert isinstance(grid, list)
            assert len(grid) == 9
            for letter in grid:
                assert letter in string.ascii_uppercase

    def test_empty_word_is_invalid(self):
        new_game = Game()
        assert new_game.is_valid('') is False

    def test_word_with_unavailable_letters_is_invalid(self):
        new_game = Game()
        new_game.grid = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']  # Fixe la grille pour le test
        assert new_game.is_valid('XYZ') is False  # X, Y et Z ne sont pas dans la grille

    def test_word_using_letters_too_many_times_is_invalid(self):
        new_game = Game()
        new_game.grid = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        assert new_game.is_valid('AA') is False  # Il n'y a qu'un seul 'A' dans la grille

    def test_valid_word(self):
        new_game = Game()
        new_game.grid = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        assert new_game.is_valid('CAB') is True  # C, A, et B sont bien dans la grille

    def test_is_invalid(self):
        # setup
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'SANDWICH'
        # exercise
        new_game.grid = list(test_grid) # Force the grid to a test case
        # verify
        assert new_game.is_valid(test_word) is False
        # teardown
        assert new_game.grid == list(test_grid) # Make sure the grid remained untouched
