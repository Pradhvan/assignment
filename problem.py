"""
Write a function that takes an array of integers given a string
as an argument and returns the second max value from the input array.
If there is no second max return -1.

1. For array ["3", "-2"] should return "-2"
2. For array ["5", "5", "4", "2"] should return "4"
3. For array ["4", "4", "4"] should return “-1”
(duplicates are not considered as the second max)
4. For [] (empty array) should return “-1”.
"""
import sys
import unittest


def secondMaxValue(numbers):
    """
    Function that returns the secondMaxValue from the array list of strings.
    """
    if len(numbers) == 0:
        return "-1"
    else:
        size = len(numbers)

    # Setting the placeholders to the min value and index to zero.
    largest, secondLargest, index = -sys.maxsize - 1, -sys.maxsize - 1, 0

    # Iterating over the array list to check the secondMaxValue
    while index < size:
        # Adding initial largest and second largest value
        if int(numbers[index]) > largest:
            secondLargest = largest
            largest = int(numbers[index])

        # Comparing the cuurent index number
        elif int(numbers[index]) > secondLargest and \
                int(numbers[index]) != largest:

            secondLargest = int(numbers[index])

        index += 1

    if largest == int(numbers[index - 1]):
        return "-1"
    else:
        return str(secondLargest)


class Test(unittest.TestCase):

    array1 = ["4", "4", "4"]
    array2 = ["5", "5", "4", "2"]
    array3 = ["4", "4", "4"]
    array4 = []

    def test_secondMaxValue(self):
        """
        Class to test the secondMaxValue function
        """
        result = secondMaxValue(self.array1)
        self.assertEqual("-1", result)
        result = secondMaxValue(self.array2)
        self.assertEqual("4", result)
        result = secondMaxValue(self.array3)
        self.assertEqual("-1", result)
        result = secondMaxValue(self.array4)
        self.assertEqual("-1", result)


if __name__ == '__main__':
    unittest.main()
