import unittest


def sort_algorithm(list):
    list.sort()
    return list


def is_not_in_descending_order(list):
    """
    Check if the list a is not descending (means "rather ascending")
    """
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True


class TestSort(unittest.TestCase):
    def setUp(self):
        self.cases = ([1], [], [1, 2], [1, 2, 3, 4, 5],
                      [4, 2, 5, 0, 3], [5, 4, 4, 5, 5],
                      list(range(1, 10)), list(range(9, 0, -1)))

    def test_simple_cases(self):
        for case in self.cases:
            with self.subTest(case=case):
                self.assertTrue(is_not_in_descending_order(case),
                                msg="List not sorted in ascending order. List = " + str(case))

    def tearDown(self):
        self.cases = None


unittest.main()
