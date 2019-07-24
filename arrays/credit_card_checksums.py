# no link available

import unittest


def check_sum(card):
    card = str(card)

    # step 1 - reverse ordering of digits
    card = card[::-1]

    # step 2
    #   extract all elements at an odd position
    #   sum them up and assign it to A
    card_odd_positions = card[0::2]
    A = get_sum_of_digits(card_odd_positions)

    # step 3
    #   extract all elements at an even position
    #   multiply each of them by 2
    #       if you obtain a 2 digit number, replace it with the sum of its digits
    #   sum them up and assign it to B
    card_even_positions = card[1::2]
    B = 0
    for number in card_even_positions:
        number = int(number)
        number *= 2
        if number > 9:
            number = str(number)
            number = get_sum_of_digits(number)
        B += number

    # step 4
    #   find sum of A and B
    #   if sum is divisible by 10, pass!
    if (A + B) % 10:
        result = "No"
    else:
        result = "Yes"
    return(result)


def get_sum_of_digits(number_string):
    # just for better readability
    return sum([int(number) for number in number_string])


class MyTest(unittest.TestCase):
    def test_1(self):
        card = 9795526789839145
        received = check_sum(card)
        expected = "No"
        self.assertEqual(received, expected)

    def test_2(self):
        card = 2861747566959730
        received = check_sum(card)
        expected = "Yes"
        self.assertEqual(received, expected)

    def test_3(self):
        card = 99447398617
        received = check_sum(card)
        expected = "No"
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
