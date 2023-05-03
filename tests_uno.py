import unittest
import sys

from uno import UnoCard
from uno import UnoPlayer
from uno import UnoGame
from uno import ReversibleCycle


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

        self.cards = [self.cardR0, self.cardB8, self.cardG3,
                      self.cardGSkip, self.cardRPlus2, self.cardR5, self.cardBPlus2]
        self.wildcardCards =  [self.cardW, self.cardW, self.cardW, 
                               self.cardW4, self.cardW4, self.cardW4, self.cardW4]

        self.player1 = UnoPlayer(self.cards)

        self.game = UnoGame(15)
        self.cycle = ReversibleCycle(self.game.players)
        self.rc = ReversibleCycle(range(3))
        #self.AI = AIUnoGame(15)

#UnoCard Tests
#-----------------------------------------------------------------------------------------------------------------------------
    def test_uno_card_init_card_type_red_color(self):
        self.cardR0
        self.assertEqual(self.cardR0.color , "red")
    def test_uno_card_init_card_type_red_0(self):
        self.assertEqual(self.cardR0.card_type , 0)
    def test_uno_card_init_card_type_red_1(self):
        self.assertEqual(self.cardR1.card_type , 1)
    def test_uno_card_init_card_type_red_2(self):
        self.assertEqual(self.cardR2.card_type , 2)
    def test_uno_card_init_card_type_red_3(self):
        self.assertEqual(self.cardR3.card_type , 3)
    def test_uno_card_init_card_type_red_4(self):
        self.assertEqual(self.cardR4.card_type , 4)
    def test_uno_card_init_card_type_red_5(self):
        self.assertEqual(self.cardR5.card_type , 5)
    def test_uno_card_init_card_type_red_6(self):
        self.assertEqual(self.cardR6.card_type , 6)
    def test_uno_card_init_card_type_red_7(self):
        self.assertEqual(self.cardR7.card_type , 7)
    def test_uno_card_init_card_type_red_8(self):
        self.assertEqual(self.cardR8.card_type , 8)
    def test_uno_card_init_card_type_red_9(self):
        self.assertEqual(self.cardR9.card_type , 9)
    def test_uno_card_init_card_type_red_skip(self):
        self.assertEqual(self.cardRSkip.card_type , "skip")
    def test_uno_card_init_card_type_red_reverse(self):
        self.assertEqual(self.cardBReverse.card_type , "reverse")
    def test_uno_card_init_card_type_red_plus_2(self):
        self.assertEqual(self.cardRPlus2.card_type , "+2")

    def test_uno_card_init_card_type_yellow_color(self):
        self.assertEqual(self.cardY0.color , "yellow")
    def test_uno_card_init_card_type_yellow_0(self):
        self.assertEqual(self.cardY0.card_type , 0)
    def test_uno_card_init_card_type_yellow_1(self):
        self.assertEqual(self.cardY1.card_type , 1)
    def test_uno_card_init_card_type_yellow_2(self):
        self.assertEqual(self.cardY2.card_type , 2)
    def test_uno_card_init_card_type_yellow_3(self):
        self.assertEqual(self.cardY3.card_type , 3)
    def test_uno_card_init_card_type_yellow_4(self):
        self.assertEqual(self.cardY4.card_type , 4)
    def test_uno_card_init_card_type_yellow_5(self):
        self.assertEqual(self.cardY5.card_type , 5)
    def test_uno_card_init_card_type_yellow_6(self):
        self.assertEqual(self.cardY6.card_type , 6)
    def test_uno_card_init_card_type_yellow_7(self):
        self.assertEqual(self.cardY7.card_type , 7)
    def test_uno_card_init_card_type_yellow_8(self):
        self.assertEqual(self.cardY8.card_type , 8)
    def test_uno_card_init_card_type_yellow_9(self):
        self.assertEqual(self.cardY9.card_type , 9)
    def test_uno_card_init_card_type_yellow_skip(self):
        self.assertEqual(self.cardYSkip.card_type , "skip")
    def test_uno_card_init_card_type_yellow__reverse(self):
        self.assertEqual(self.cardYReverse.card_type , "reverse")
    def test_uno_card_init_card_type_yellow_plus_2(self):
        self.assertEqual(self.cardYPlus2.card_type , "+2")

    def test_uno_card_init_card_type_green_color(self):
        self.assertEqual(self.cardG0.color , "green")
    def test_uno_card_init_card_type_green_0(self):
        self.assertEqual(self.cardG0.card_type , 0)
    def test_uno_card_init_card_type_green_1(self):
        self.assertEqual(self.cardG1.card_type , 1)
    def test_uno_card_init_card_type_green_2(self):
        self.assertEqual(self.cardG2.card_type , 2)
    def test_uno_card_init_card_type_green_3(self):
        self.assertEqual(self.cardG3.card_type , 3)
    def test_uno_card_init_card_type_green_4(self):
        self.assertEqual(self.cardG4.card_type , 4)
    def test_uno_card_init_card_type_green_5(self):
        self.assertEqual(self.cardG5.card_type , 5)
    def test_uno_card_init_card_type_green_6(self):
        self.assertEqual(self.cardG6.card_type , 6)
    def test_uno_card_init_card_type_green_7(self):
        self.assertEqual(self.cardG7.card_type , 7)
    def test_uno_card_init_card_type_green_8(self):
        self.assertEqual(self.cardG8.card_type , 8)
    def test_uno_card_init_card_type_green_9(self):
        self.assertEqual(self.cardG9.card_type , 9)
    def test_uno_card_init_card_type_green_skip(self):
        self.assertEqual(self.cardGSkip.card_type , "skip")
    def test_uno_card_init_card_type_green_reverse(self):
        self.assertEqual(self.cardGReverse.card_type , "reverse")
    def test_uno_card_init_card_type_green_plus_2(self):
        self.assertEqual(self.cardGPlus2.card_type , "+2")

    def test_uno_card_init_card_type_blue_color(self):
        self.assertEqual(self.cardB0.color , "blue")
    def test_uno_card_init_card_type_blue_0(self):
        self.assertEqual(self.cardB0.card_type , 0)
    def test_uno_card_init_card_type_blue_1(self):
        self.assertEqual(self.cardB1.card_type , 1)
    def test_uno_card_init_card_type_blue_2(self):
        self.assertEqual(self.cardB2.card_type , 2)
    def test_uno_card_init_card_type_blue_3(self):
        self.assertEqual(self.cardB3.card_type , 3)
    def test_uno_card_init_card_type_blue_4(self):
        self.assertEqual(self.cardB4.card_type , 4)
    def test_uno_card_init_card_type_blue_5(self):
        self.assertEqual(self.cardB5.card_type , 5)
    def test_uno_card_init_card_type_blue_6(self):
        self.assertEqual(self.cardB6.card_type , 6)
    def test_uno_card_init_card_type_blue_7(self):
        self.assertEqual(self.cardB7.card_type , 7)
    def test_uno_card_init_card_type_blue_8(self):
        self.assertEqual(self.cardB8.card_type , 8)
    def test_uno_card_init_card_type_blue_9(self):
        self.assertEqual(self.cardB9.card_type , 9)
    def test_uno_card_init_card_type_blue_skip(self):
        self.assertEqual(self.cardBSkip.card_type , "skip")
    def test_uno_card_init_card_type_blue_reverse(self):
        self.assertEqual(self.cardBReverse.card_type , "reverse")
    def test_uno_card_init_card_type_blue_plus_2(self):
        self.assertEqual(self.cardBPlus2.card_type , "+2")

    def test_uno_card_init_card_type_wild_color(self):
        self.assertEqual(self.cardW.color , "black")
    def test_uno_card_init_card_type_wild_type(self):
        self.assertEqual(self.cardW.card_type , "wildcard")

    def test_uno_card_init_card_type_wild_draw_4_color(self):
        self.assertEqual(self.cardW4.color , "black")
    def test_uno_card_init_card_type_wild_draw_4_type(self):
        self.assertEqual(self.cardW4.card_type , "+4")

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
    def test_color_not_black_and_card_type_not_in_black_card_type_false(self):
        self.assertIsNone(self.cardGSkip._validate('green', 'skip'))

#UnoPlayer Tests
#-----------------------------------------------------------------------------------------------------------------------------
    def test_UnoPlayer_init_player_id(self):
        player1 = UnoPlayer(self.cards, 1)
        self.assertEqual(player1.player_id, 1)
    def test_UnoPlayer_init_player_hand(self):
        player1 = UnoPlayer(self.cards, 1)
        self.assertEqual(len(player1.hand), 7)
    def test_UnoPlayer_can_play_return_true(self):
        player1 = UnoPlayer(self.cards, 1)
        self.currentCard = self.cardR3 
        self.assertTrue(player1.can_play(self.currentCard))
    def test_UnoPlayer_can_play_return_false(self):
        player1 = UnoPlayer(self.cards, 1)
        self.currentCard = self.cardY7 
        self.assertFalse(player1.can_play(self.currentCard))
    def test_UnoPlayer_init_player_hand_error_not_triggered(self):
        with self.assertRaises(ValueError):
            player3 = UnoPlayer('player3', self.cards)
            player3
    def test_UnoPlayer_init_player_hand_error_triggered_invalid_color(self):
        with self.assertRaises(ValueError):
            player4 = UnoPlayer(4, [UnoCard('purple', 1), UnoCard('blue', 'skip')])
            player4
    def test_invalid_player(self):
        game = self.game
        invalid_player = "invalid_player"
        with self.assertRaises(ValueError):
            game.play(invalid_player)
    def test_player_index_out_of_range(self):
        game = self.game
        player_index = len(game.players)
        with self.assertRaises(ValueError):
            game.play(player_index)
    def test_draw_card(self):
        game = self.game
        player_index = 0
        initial_hand_size = len(game.players[player_index].hand)
        game.play(player_index, card=None, new_color=None)
        expected_hand_size = initial_hand_size + 1
        actual_hand_size = len(game.players[player_index].hand)
        self.assertEqual(expected_hand_size, actual_hand_size)
    


#UnoGame Tests
#-----------------------------------------------------------------------------------------------------------------------------
    def test_init_game_is_created(self):
        game = UnoGame(4)
        self.assertIsInstance(game, UnoGame)
    def test_init_game_num_players(self):
        game = UnoGame(4)
        self.assertEqual(len(game.players), 4)
    def test_init_game_deck_correct(self):
        game = UnoGame(4)
        self.assertEqual(len(game.deck), 80)
    def test_init_game_deck_is_unoCard_objects(self):
        game = UnoGame(4)
        self.assertIsInstance(game.deck[0], UnoCard)
    def test_init_game_winner(self):
        game = UnoGame(4)
        self.assertIsNone(game._winner)
    def test_deal_hand_is_list(self):
        game = UnoGame(3)
        hand1 = game._deal_hand()
        self.assertIsInstance(hand1, list)
    def test_deal_hand_is_UnoCard(self):
        game = UnoGame(3)
        hand1 = game._deal_hand()
        self.assertIsInstance(hand1[0], UnoCard)
    def test_deal_hand_is_7_cards(self):
        game = UnoGame(3)
        hand1 = game._deal_hand()
        self.assertEqual(len(hand1), 7)
    def test_deal_hand_not_equal_to_second_hand_1(self):
        game = UnoGame(3)
        hand1 = game._deal_hand()
        hand2 = game._deal_hand()
        self.assertNotEqual(hand1, hand2)
    def test_deal_hand_not_equal_to_second_hand_2(self):
        game = UnoGame(3)
        hand2 = game._deal_hand()
        hand3 = game._deal_hand()
        self.assertNotEqual(hand2, hand3)
    def test_deal_hand_not_equal_to_second_hand_3(self):
        game = UnoGame(3)
        hand1 = game._deal_hand()
        hand3 = game._deal_hand()
        self.assertNotEqual(hand1, hand3)
    def test_next_player(self):
        #This test breaks conventions to use multiple 
        # asserts to show we are changing players
        game = UnoGame(2)
        self.assertEqual(game._current_player, game.players[0])
        next(game)
        self.assertEqual(game._current_player, game.players[1])
        next(game)
        self.assertEqual(game._current_player, game.players[0])

    def test_playing_a_card_that_is_playable_current_hand_size(self):
        game = UnoGame(2)
        game._current_player.hand = [
            UnoCard('red', 5),
            UnoCard('blue', 7),
            UnoCard('yellow', 2),
            UnoCard('green', 'skip'),
            UnoCard('black', 'wildcard'),
        ]
        game._current_card = self.cardB4

        self.assertEqual(len(game._current_player.hand), 5)
    def test_playing_a_card_that_is_playable_UnoCard(self):
        game = UnoGame(2)
        game._current_player.hand = [
            UnoCard('red', 5),
            UnoCard('blue', 7),
            UnoCard('yellow', 2),
            UnoCard('green', 'skip'),
            UnoCard('black', 'wildcard'),
        ]
        game._current_card = self.cardB7

        self.assertEqual(game._current_card, self.cardB7)

    def test_play_invalid_player(self):
        with self.assertRaises(ValueError):
            self.game.play('not an int')

    def test_play_invalid_player_index(self):
        with self.assertRaises(ValueError):
            self.game.play(10)

    def test_play_not_players_turn(self):
        with self.assertRaises(ValueError):
            self.game.play(1)

    def test_play_invalid_player_type(self):
        with self.assertRaises(ValueError):
            self.game.play('1')

    def test_play_invalid_card(self):
        player = self.game.current_player
        with self.assertRaises(ValueError):
            self.game.play(player, 0)

    def test_play_invalid_new_color(self):
        player = self.game.current_player
        with self.assertRaises(ValueError):
            self.game.play(player, 0, 'purple')

    def test_play_game_over(self):
        player = self.game.current_player
        with self.assertRaises(ValueError):
            self.game.play(player, 0)

# THIS ONE
    def test_play_black_card_plus_four(self):
        sys.stdout = open('nul', 'w')
        player = self.game.current_player
        card = self.cardW4
        player.hand = [card]
        self.game.play(0, 0, 'green')
        self.assertEqual(len(player.hand), 0)

#ReversibleCycle Tests
#-----------------------------------------------------
    def test_init_items(self):
        self.assertEqual(self.rc._items, [0, 1, 2])    
    def test_init_pos(self):
        self.assertIsNone(self.rc._pos)
    def test_init_reverse(self):
        self.assertFalse(self.rc._reverse)

    def test_next_forward(self):
        # Test forward cycle
        # multiple asserts to make sure the cycle is working
        self.assertEqual(next(self.rc), 0)
        self.assertEqual(next(self.rc), 1)
        self.assertEqual(next(self.rc), 2)
        self.assertEqual(next(self.rc), 0)
        self.assertEqual(next(self.rc), 1)
    
    def test_next_reverse(self):
        # Test reverse cycle
        # multiple asserts to make sure the cycle is working
        self.rc.reverse()
        self.assertEqual(next(self.rc), 2)
        self.assertEqual(next(self.rc), 1)
        self.assertEqual(next(self.rc), 0)
        self.assertEqual(next(self.rc), 2)
        self.assertEqual(next(self.rc), 1)

    def test_reverse(self):
        self.assertFalse(self.rc._reverse)
        self.rc.reverse()
        self.assertTrue(self.rc._reverse)
        self.rc.reverse()
        self.assertFalse(self.rc._reverse)

    def test_pos_forward(self):
        # Test forward cycle
        self.rc.pos = 1
        self.assertEqual(self.rc.pos, 1)

    def test_pos_reverse(self):
        # Test reverse cycle
        self.rc.reverse()
        self.rc.pos = 1
        self.assertEqual(self.rc.pos, 1)

#integreation Test
#----------------------------------------------------
    def test_create_uno_card(self):
        # Test that a valid UnoCard can be created
        card = UnoCard('red', 5)
        self.assertEqual(card.color, 'red')
        self.assertEqual(card.card_type, 5)

    def test_create_uno_player(self):
        # Test that a valid UnoPlayer can be created
        cards = [UnoCard('red', n) for n in range(7)]
        player = UnoPlayer(cards)
        self.assertEqual(len(player.hand), 7)

    def test_create_uno_game(self):
        # Test that a valid UnoGame can be created
        game = UnoGame(5)
        self.assertEqual(len(game.players), 5)
        self.assertIsInstance(game.deck[0], UnoCard)

    def test_play_uno_game(self):
        # Test that a game can be played and completed
        game = UnoGame(2)
        game.deck = [UnoCard('red', n) for n in range(1, 9)]
        game.players[0].hand = [UnoCard('red', n) for n in range(3)]
        game.players[1].hand = [UnoCard('green', n) for n in range(3)]
        current_card = UnoCard('red', 8)
        while game._winner is None:
            player = game._current_player
            if player.can_play(current_card):
                card_to_play = player.hand[0]
                for card in player.hand:
                    if card.playable(current_card):
                        card_to_play = card
                        break
                player.hand.remove(card_to_play)
                current_card = card_to_play
                if len(player.hand) == 0:
                    game._winner = player
                    break
                elif len(player.hand) == 1:
                    player.called_uno = True
            else:
                player.draw_card(game.deck.pop())
            next(game)
        self.assertEqual(game._winner, game.players[0])

#-----------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main(verbosity=0, exit=False)