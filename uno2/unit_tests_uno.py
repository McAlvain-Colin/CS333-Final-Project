import unittest

from uno import UnoCard
from uno import UnoPlayer
from uno import UnoGame
from uno import ReversibleCycle
from uno import AIUnoGame

class TestUnoUnitTests(unittest.TestCase):
    def setUp(self):
        self.cardR0  = UnoCard("red", 0)
        self.cardR1  = UnoCard("red", 1)
        self.cardR2  = UnoCard("red", 2)
        self.cardR3  = UnoCard("red", 3)
        self.cardR4  = UnoCard("red", 4)
        self.cardR5  = UnoCard("red", 5)
        self.cardR6  = UnoCard("red", 6)
        self.cardR7  = UnoCard("red", 7)
        self.cardR8  = UnoCard("red", 8)
        self.cardR9  = UnoCard("red", 9)
        self.cardRSkip   = UnoCard("red", "skip")
        self.cardRReverse   = UnoCard("red", "reverse")
        self.cardRPlus2   = UnoCard("red", "+2")

        self.cardY0  = UnoCard("yellow", 0)
        self.cardY1  = UnoCard("yellow", 1)
        self.cardY2  = UnoCard("yellow", 2)
        self.cardY3  = UnoCard("yellow", 3)
        self.cardY4  = UnoCard("yellow", 4)
        self.cardY5  = UnoCard("yellow", 5)
        self.cardY6  = UnoCard("yellow", 6)
        self.cardY7  = UnoCard("yellow", 7)
        self.cardY8  = UnoCard("yellow", 8)
        self.cardY9  = UnoCard("yellow", 9)
        self.cardYSkip   = UnoCard("yellow", "skip")
        self.cardYReverse   = UnoCard("yellow", "reverse")
        self.cardYPlus2   = UnoCard("yellow","+2" )

        self.cardG0  = UnoCard("green", 0)
        self.cardG1  = UnoCard("green", 1)
        self.cardG2  = UnoCard("green", 2)
        self.cardG3  = UnoCard("green", 3)
        self.cardG4  = UnoCard("green", 4)
        self.cardG5  = UnoCard("green", 5)
        self.cardG6  = UnoCard("green", 6)
        self.cardG7  = UnoCard("green", 7)
        self.cardG8  = UnoCard("green", 8)
        self.cardG9  = UnoCard("green", 9)
        self.cardGSkip   = UnoCard("green", "skip")
        self.cardGReverse   = UnoCard("green", "reverse")
        self.cardGPlus2   = UnoCard("green", "+2")

        self.cardB0  = UnoCard("blue", 0)
        self.cardB1  = UnoCard("blue", 1)
        self.cardB2  = UnoCard("blue", 2)
        self.cardB3  = UnoCard("blue", 3)
        self.cardB4  = UnoCard("blue", 4)
        self.cardB5  = UnoCard("blue", 5)
        self.cardB6  = UnoCard("blue", 6)
        self.cardB7  = UnoCard("blue", 7)
        self.cardB8  = UnoCard("blue", 8)
        self.cardB9  = UnoCard("blue", 9)
        self.cardBSkip   = UnoCard("blue", "skip")
        self.cardBReverse   = UnoCard("blue", "reverse")
        self.cardBPlus2   = UnoCard("blue", "+2")

        self.cardW = UnoCard('black', 'wildcard')
        self.cardW4 = UnoCard("black", "+4")

        self.cards = [self.cardR0, self.cardB8, self.cardG3, self.cardGSkip, self.cardRPlus2, self.cardR5, self.cardBPlus2]
        self.wildcardCards =  [self.cardW, self.cardW, self.cardW, self.cardW4, self.cardW4, self.cardW4, self.cardW4]

        self.player1 = UnoPlayer(self.cards)

        self.game = UnoGame(15)
        self.cycle = ReversibleCycle(self.game.players)
        #self.AI = AIUnoGame(15)

#UnoCard Tests
#-----------------------------------------------------------------------------------------------------------------------------
    def test_uno_card_init_card_type_red_color(self):
        self.cardR0
        self.assertEqual(self.cardR0.color , "red")
    def test_uno_card_init_card_type_red_0(self):
        self.cardR0
        self.assertEqual(self.cardR0.card_type , 0)
    def test_uno_card_init_card_type_red_1(self):
        self.cardR1
        self.assertEqual(self.cardR1.card_type , 1)
    def test_uno_card_init_card_type_red_2(self):
        self.cardR2
        self.assertEqual(self.cardR2.card_type , 2)
    def test_uno_card_init_card_type_red_3(self):
        self.cardR3
        self.assertEqual(self.cardR3.card_type , 3)
    def test_uno_card_init_card_type_red_4(self):
        self.cardR4
        self.assertEqual(self.cardR4.card_type , 4)
    def test_uno_card_init_card_type_red_5(self):
        self.cardR5
        self.assertEqual(self.cardR5.card_type , 5)
    def test_uno_card_init_card_type_red_6(self):
        self.cardR6
        self.assertEqual(self.cardR6.card_type , 6)
    def test_uno_card_init_card_type_red_7(self):
        self.cardR7
        self.assertEqual(self.cardR7.card_type , 7)
    def test_uno_card_init_card_type_red_8(self):
        self.cardR8
        self.assertEqual(self.cardR8.card_type , 8)
    def test_uno_card_init_card_type_red_9(self):
        self.cardR9
        self.assertEqual(self.cardR9.card_type , 9)
    def test_uno_card_init_card_type_red_skip(self):
        self.cardR0
        self.assertEqual(self.cardRSkip.card_type , "skip")
    def test_uno_card_init_card_type_red_reverse(self):
        self.cardR0
        self.assertEqual(self.cardBReverse.card_type , "reverse")
    def test_uno_card_init_card_type_red_plus_2(self):
        self.cardR0
        self.assertEqual(self.cardRPlus2.card_type , "+2")

    def test_uno_card_init_card_type_yellow_color(self):
        self.cardY0
        self.assertEqual(self.cardY0.color , "yellow")
    def test_uno_card_init_card_type_yellow_0(self):
        self.cardY0
        self.assertEqual(self.cardY0.card_type , 0)
    def test_uno_card_init_card_type_yellow_1(self):
        self.cardY1
        self.assertEqual(self.cardY1.card_type , 1)
    def test_uno_card_init_card_type_yellow_2(self):
        self.cardY2
        self.assertEqual(self.cardY2.card_type , 2)
    def test_uno_card_init_card_type_yellow_3(self):
        self.cardY3
        self.assertEqual(self.cardY3.card_type , 3)
    def test_uno_card_init_card_type_yellow_4(self):
        self.cardY4
        self.assertEqual(self.cardY4.card_type , 4)
    def test_uno_card_init_card_type_yellow_5(self):
        self.cardY5
        self.assertEqual(self.cardY5.card_type , 5)
    def test_uno_card_init_card_type_yellow_6(self):
        self.cardY6
        self.assertEqual(self.cardY6.card_type , 6)
    def test_uno_card_init_card_type_yellow_7(self):
        self.cardY7
        self.assertEqual(self.cardY7.card_type , 7)
    def test_uno_card_init_card_type_yellow_8(self):
        self.cardY8
        self.assertEqual(self.cardY8.card_type , 8)
    def test_uno_card_init_card_type_yellow_9(self):
        self.cardY9
        self.assertEqual(self.cardY9.card_type , 9)
    def test_uno_card_init_card_type_yellow_skip(self):
        self.cardY0
        self.assertEqual(self.cardYSkip.card_type , "skip")
    def test_uno_card_init_card_type_yellow__reverse(self):
        self.cardY0
        self.assertEqual(self.cardYReverse.card_type , "reverse")
    def test_uno_card_init_card_type_yellow_plus_2(self):
        self.cardY0
        self.assertEqual(self.cardYPlus2.card_type , "+2")

    def test_uno_card_init_card_type_green_color(self):
        self.cardG0
        self.assertEqual(self.cardG0.color , "green")
    def test_uno_card_init_card_type_green_0(self):
        self.cardG0
        self.assertEqual(self.cardG0.card_type , 0)
    def test_uno_card_init_card_type_green_1(self):
        self.cardG1
        self.assertEqual(self.cardG1.card_type , 1)
    def test_uno_card_init_card_type_green_2(self):
        self.cardG2
        self.assertEqual(self.cardG2.card_type , 2)
    def test_uno_card_init_card_type_green_3(self):
        self.cardG3
        self.assertEqual(self.cardG3.card_type , 3)
    def test_uno_card_init_card_type_green_4(self):
        self.cardG4
        self.assertEqual(self.cardG4.card_type , 4)
    def test_uno_card_init_card_type_green_5(self):
        self.cardG5
        self.assertEqual(self.cardG5.card_type , 5)
    def test_uno_card_init_card_type_green_6(self):
        self.cardG6
        self.assertEqual(self.cardG6.card_type , 6)
    def test_uno_card_init_card_type_green_7(self):
        self.cardG7
        self.assertEqual(self.cardG7.card_type , 7)
    def test_uno_card_init_card_type_green_8(self):
        self.cardG8
        self.assertEqual(self.cardG8.card_type , 8)
    def test_uno_card_init_card_type_green_9(self):
        self.cardG9
        self.assertEqual(self.cardG9.card_type , 9)
    def test_uno_card_init_card_type_green_skip(self):
        self.cardG0
        self.assertEqual(self.cardGSkip.card_type , "skip")
    def test_uno_card_init_card_type_green_reverse(self):
        self.cardG0
        self.assertEqual(self.cardGReverse.card_type , "reverse")
    def test_uno_card_init_card_type_green_plus_2(self):
        self.cardG0
        self.assertEqual(self.cardGPlus2.card_type , "+2")

    def test_uno_card_init_card_type_blue_color(self):
        self.cardB0
        self.assertEqual(self.cardB0.color , "blue")
    def test_uno_card_init_card_type_blue_0(self):
        self.cardB0
        self.assertEqual(self.cardB0.card_type , 0)
    def test_uno_card_init_card_type_blue_1(self):
        self.cardB1
        self.assertEqual(self.cardB1.card_type , 1)
    def test_uno_card_init_card_type_blue_2(self):
        self.cardB2
        self.assertEqual(self.cardB2.card_type , 2)
    def test_uno_card_init_card_type_blue_3(self):
        self.cardB3
        self.assertEqual(self.cardB3.card_type , 3)
    def test_uno_card_init_card_type_blue_4(self):
        self.cardB4
        self.assertEqual(self.cardB4.card_type , 4)
    def test_uno_card_init_card_type_blue_5(self):
        self.cardB5
        self.assertEqual(self.cardB5.card_type , 5)
    def test_uno_card_init_card_type_blue_6(self):
        self.cardB6
        self.assertEqual(self.cardB6.card_type , 6)
    def test_uno_card_init_card_type_blue_7(self):
        self.cardB7
        self.assertEqual(self.cardB7.card_type , 7)
    def test_uno_card_init_card_type_blue_8(self):
        self.cardB8
        self.assertEqual(self.cardB8.card_type , 8)
    def test_uno_card_init_card_type_blue_9(self):
        self.cardB9
        self.assertEqual(self.cardB9.card_type , 9)
    def test_uno_card_init_card_type_blue_skip(self):
        self.cardB0
        self.assertEqual(self.cardBSkip.card_type , "skip")
    def test_uno_card_init_card_type_blue_reverse(self):
        self.cardB0
        self.assertEqual(self.cardBReverse.card_type , "reverse")
    def test_uno_card_init_card_type_blue_plus_2(self):
        self.cardB0
        self.assertEqual(self.cardRPlus2.card_type , "+2")

    def test_uno_card_init_card_type_wild_color(self):
        self.cardW
        self.assertEqual(self.cardR0.color , "black")
    def test_uno_card_init_card_type_wild_type(self):
        self.cardB0
        self.assertEqual(self.cardBReverse.card_type , "reverse")
    def test_uno_card_init_card_type_wild_color(self):
        self.cardB0
        self.assertEqual(self.cardRPlus2.card_type , "+2")

    def test_uno_card_init_card_type_wild_draw_4_color(self):
        self.cardW4
        self.assertEqual(self.cardW4.color , "black")
    def test_uno_card_init_card_type_wild_draw_4_type(self):
        self.cardB0
        self.assertEqual(self.cardBReverse.card_type , "reverse")
    def test_uno_card_init_card_type_wild_draw_4_color(self):
        self.cardB0
        self.assertEqual(self.cardRPlus2.card_type , "+2")

    def test_str_string_return_test_1(self):
        self.assertEqual(str(self.cardR1), 'R1')
    def test_str_string_return_test_2(self):
        self.assertEqual(str(self.cardG2), 'G2')

    def test_eq_return_test_true(self):
        self.assertTrue(self.cardR1 == self.cardR1)
    def test_eq_return_test_false(self):
        self.assertFalse(self.cardR1 == self.cardG3)

    def test_validate_not_in_all_color_return_false(self):
        self.assertIsNone(self.cardR2._validate('red', 2))
    def test_validate_color_is_black_and_card_type_not_in_black_card_type_false(self):
        self.assertIsNone(self.cardR1._validate('black', '+4'))
    def test_validate_color_is_black_and_card_type_not_in_black_card_type_true(self):
        with self.assertRaises(ValueError):
            self.cardR1._validate('black', '2')
    def test_validate_color_is_not_black_and_card_type_not_in_black_card_type_false(self):
        self.assertIsNone(self.cardGSkip._validate('green', 'skip'))

#UnoPlayer Tests
#-----------------------------------------------------------------------------------------------------------------------------
    def test_UnoPlayer_init_player_id(self):
        player1 = UnoPlayer(self.cards, 1)
        self.assertEqual(player1.player_id, 1)
    def test_UnoPlayer_init_player_hand(self):
        player1 = UnoPlayer(self.cards, 1)
        self.assertEqual(len(player1.hand), 7)
    def test_UnoPlayer_init_player_hand_error_not_triggered(self):
        with self.assertRaises(ValueError):
            player3 = UnoPlayer('player3', self.cards)
    def test_UnoPlayer_init_player_hand_error_triggered_invalid_color(self):
        with self.assertRaises(ValueError):
            player4 = UnoPlayer(4, [UnoCard('purple', 1), UnoCard('blue', 'skip')])

#UnoGame Tests
#-----------------------------------------------------------------------------------------------------------------------------
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):
    #     pass
    # def test(self):

#integreation Test
#-----------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()