import pytest

from app.yahtzee import *


class TestHand:

    def test_hand_number_of_dice(self):
        hand = Hand(15, 6)
        assert len(hand.hand) == 15

    def test_hand_sides_per_die(self):
        hand = Hand(5, 18)
        for i in hand.hand:
            assert i.sides == 18


class TestRules:

    def test_aces(self):
        hand = Hand()
        for i in range(5):
            hand.hand[i]._Die__face = 1
        assert Rules().aces(hand) == 5
        hand.hand[4]._Die__face = 4
        assert Rules().aces(hand) == 4

    def test_twos(self):
        hand = Hand()
        for i in range(5):
            hand.hand[i]._Die__face = 2
        assert Rules().twos(hand) == 10
        hand.hand[4]._Die__face = 4
        assert Rules().twos(hand) == 8
        hand.hand[3]._Die__face = 3
        assert Rules().twos(hand) == 6
        hand.hand[2]._Die__face = 1
        hand.hand[1]._Die__face = 5
        hand.hand[0]._Die__face = 6
        assert Rules().twos(hand) == 0

    def test_threes(self):
        hand = Hand()
        for i in range(5):
            hand.hand[i]._Die__face = 3
        assert Rules().threes(hand) == 15
        hand.hand[4]._Die__face = 4
        assert Rules().threes(hand) == 12
        hand.hand[3]._Die__face = 2
        assert Rules().threes(hand) == 9
        hand.hand[2]._Die__face = 1
        hand.hand[1]._Die__face = 5
        hand.hand[0]._Die__face = 6
        assert Rules().threes(hand) == 0

    def test_fours(self):
        hand = Hand()
        for i in range(5):
            hand.hand[i]._Die__face = 4
        assert Rules().fours(hand) == 20
        hand.hand[4]._Die__face = 3
        assert Rules().fours(hand) == 16
        hand.hand[3]._Die__face = 3
        assert Rules().fours(hand) == 12
        hand.hand[2]._Die__face = 1
        hand.hand[1]._Die__face = 5
        hand.hand[0]._Die__face = 5
        assert Rules().fours(hand) == 0

    def test_fives(self):
        hand = Hand()
        for i in range(5):
            hand.hand[i]._Die__face = 5
        assert Rules().fives(hand) == 25
        hand.hand[4]._Die__face = 3
        assert Rules().fives(hand) == 20
        hand.hand[3]._Die__face = 3
        assert Rules().fives(hand) == 15
        hand.hand[2]._Die__face = 1
        hand.hand[1]._Die__face = 2
        hand.hand[0]._Die__face = 4
        assert Rules().fives(hand) == 0

    def test_sixes(self):
        hand = Hand()
        for i in range(5):
            hand.hand[i]._Die__face = 6
        assert Rules().sixes(hand) == 30
        hand.hand[4]._Die__face = 4
        assert Rules().sixes(hand) == 24
        hand.hand[3]._Die__face = 3
        assert Rules().sixes(hand) == 18
        hand.hand[2]._Die__face = 1
        hand.hand[1]._Die__face = 5
        hand.hand[0]._Die__face = 5
        assert Rules().sixes(hand) == 0

    def test_pair(self):
        hand = Hand()
        hand.hand[0]._Die__face = 3
        hand.hand[1]._Die__face = 3
        hand.hand[2]._Die__face = 3
        hand.hand[3]._Die__face = 1
        hand.hand[4]._Die__face = 1
        assert Rules().pair(hand) == 2
        hand.hand[2]._Die__face = 4
        assert Rules().pair(hand) == 6   # 3,3,4,1,2

        hand.hand[3]._Die__face = 3
        assert Rules().pair(hand) == 0   # 3,3,4,3,2
        hand.hand[4]._Die__face = 5
        assert Rules().pair(hand) == 0   # 3,3,4,3,5

    def test_two_pairs(self):
        hand = Hand()
        hand.hand[0]._Die__face = 3
        hand.hand[1]._Die__face = 3
        hand.hand[2]._Die__face = 5
        hand.hand[3]._Die__face = 1
        hand.hand[4]._Die__face = 1
        assert Rules().two_pairs(hand) == 8

        hand.hand[2]._Die__face = 3
        assert Rules().two_pairs(hand) == 0    # 3, 3, 3, 1, 1
        hand.hand[2]._Die__face = 4
        hand.hand[3]._Die__face = 5
        assert Rules().two_pairs(hand) == 0    # 3, 3, 4, 5, 1

    def test_three_of_a_kind(self):
        hand = Hand()
        hand.hand[0]._Die__face = 3
        hand.hand[1]._Die__face = 3
        hand.hand[2]._Die__face = 3
        hand.hand[3]._Die__face = 1
        hand.hand[4]._Die__face = 1
        assert Rules().three_of_a_kind(hand) == 9

        hand.hand[3]._Die__face = 3
        assert Rules().three_of_a_kind(hand) == 0
        hand.hand[2]._Die__face = 4
        hand.hand[3]._Die__face = 5
        assert Rules().three_of_a_kind(hand) == 0

    def test_four_of_a_kind(self):
        hand = Hand()
        hand.hand[0]._Die__face = 2
        hand.hand[1]._Die__face = 2
        hand.hand[2]._Die__face = 2
        hand.hand[3]._Die__face = 2
        hand.hand[4]._Die__face = 5
        assert Rules().four_of_a_kind(hand) == 8
        hand.hand[3]._Die__face = 5
        hand.hand[4]._Die__face = 5
        assert Rules().four_of_a_kind(hand) == 0
        hand.hand[3]._Die__face = 2
        hand.hand[4]._Die__face = 2
        assert Rules().four_of_a_kind(hand) == 0

    def test_full_house(self):
        hand = Hand()
        hand.hand[0]._Die__face = 2
        hand.hand[1]._Die__face = 2
        hand.hand[2]._Die__face = 2
        hand.hand[3]._Die__face = 1
        hand.hand[4]._Die__face = 1
        assert Rules().full_house(hand) == 8
        hand.hand[2]._Die__face = 3
        hand.hand[3]._Die__face = 3
        hand.hand[4]._Die__face = 3
        assert Rules().full_house(hand) == 13
        hand.hand[1]._Die__face = 3
        assert Rules().full_house(hand) == 0

    def test_small_straight(self):
        hand = Hand()
        hand.hand[0]._Die__face = 4
        hand.hand[1]._Die__face = 3
        hand.hand[2]._Die__face = 5
        hand.hand[3]._Die__face = 2
        hand.hand[4]._Die__face = 1
        assert Rules().small_straight(hand) == 15
        hand.hand[4]._Die__face = 6
        assert Rules().small_straight(hand) == 0
        hand.hand[0]._Die__face = 1
        assert Rules().small_straight(hand) == 0
        hand.hand[1]._Die__face = 1
        assert Rules().small_straight(hand) == 0

    def test_large_straight(self):
        hand = Hand()
        hand.hand[0]._Die__face = 4
        hand.hand[1]._Die__face = 3
        hand.hand[2]._Die__face = 5
        hand.hand[3]._Die__face = 2
        hand.hand[4]._Die__face = 6
        assert Rules().large_straight(hand) == 20
        hand.hand[4]._Die__face = 1
        assert Rules().large_straight(hand) == 0
        hand.hand[3]._Die__face = 3
        assert Rules().large_straight(hand) == 0

    def test_yahtzee(self):
        hand = Hand()
        hand.hand[0]._Die__face = 3
        hand.hand[1]._Die__face = 3
        hand.hand[2]._Die__face = 3
        hand.hand[3]._Die__face = 3
        hand.hand[4]._Die__face = 3
        assert Rules().yahtzee(hand) == 50

    def test_chance(self):
        hand = Hand()
        for i in range(5):
            hand.hand[i]._Die__face = i + 1
        assert Rules().chance(hand) == 15


print(list(range(1, 5)))
if __name__ == '__main__':
    pytest.main()
