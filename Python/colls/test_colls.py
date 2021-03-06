import unittest
from colls import Colls

class CollsTestCase(unittest.TestCase):

  def setUp(self):
    self.collections = Colls()

  def test_it_initializes_with_states(self):
    result = self.collections.states
    self.assertEqual(result, {"Oregon": "OR", "Alabama": "AL", "New Jersey": "NJ", "Colorado": "CO"})

  def test_it_intializes_with_capitals(self):
    result = self.collections.capitals
    self.assertEqual(result, {"OR": "Salem", "AL": "Montgomery", "NJ": "Trenton", "CO": "Denver"})
  
  def test_it_initializes_with_scrabble_board(self):
    result = self.collections.scrabble_board
    self.assertEqual(result, {"A":1, "B":3, "C":3, "D":2, "E":1, "F":4, "G":2, "H":4, "I":1, 
                             "J":8, "K":5, "L":1, "M":3, "N":1, "O":1, "P":3, "Q":10, "R":1, 
                             "S":1, "T":1, "U":1, "V":4, "W":4, "X":8, "Y":4, "Z":10})

  def test_it_returns_the_capital_when_given_a_state(self):
    state = "Colorado"
    result = self.collections.find_capital(state)
    self.assertEqual(result, "Denver")

  def test_it_returns_unknown_if_the_state_is_not_in_initial_hash(self):
    state = "Minnesota"
    result = self.collections.find_capital(state)
    self.assertEqual(result, "Unknown")

  def test_it_returns_the_state_when_given_the_capital(self):
    capital = 'Denver'
    result = self.collections.find_state(capital)
    self.assertEqual(result, 'Colorado')

  def test_it_can_score_one_letter_in_scrabble(self):
    letter = "H"
    result = self.collections.scrabble_score(letter)
    self.assertEqual(result, 4)

  def test_it_can_score_an_entire_word_in_scrabble(self):
    word = 'Hello'
    result = self.collections.scrabble_score(word)
    self.assertEqual(result, 8)

  def test_it_can_score_another_word_in_scrabble(self):
    word = 'Stephanie'
    result = self.collections.scrabble_score(word)
    self.assertEqual(result, 14)

unittest.main()