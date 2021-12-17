import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):        
        self.card_game = CardGame()
        self.hearts_1 = Card("Hearts", 1)
        self.hearts_4 = Card("Hearts", 4)
        self.hearts_6 = Card("Hearts", 6)

    def test_check_for_ace__true(self):
        actual = self.card_game.check_for_ace( self.hearts_1 )
        self.assertEqual(actual, True)

    def test_check_for_ace__false(self):
        actual = self.card_game.check_for_ace(self.hearts_4)
        self.assertEqual(actual, False)

    def test_highest_card__return_card_1(self):       
        actual = self.card_game.highest_card(self.hearts_6, self.hearts_4)
        self.assertEqual(actual, self.hearts_6)
    
    def test_highest_card__return_card_2(self):        
        actual = self.card_game.highest_card(self.hearts_4, self.hearts_6)
        self.assertEqual(actual, self.hearts_6)
    
    def test_cards_total(self):
        actual = self.card_game.cards_total([self.hearts_4,self.hearts_6])
        self.assertEqual(actual, "You have a total of10")