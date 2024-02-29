import unittest


def func_equal(a, b):
    if a == b:
        return True
    else:
        return False


def func_not_equal(a, b):
    if a != b:
        return True
    else:
        return False


def func_true(x):
    return x % 2 == 0


def func_false(x):
    return x % 2 == 0


def func_is(x):
    if x == 0:
        return None
    else:
        return x


def func_is_not():
    return []


def func_is_none(x):
    if x == 1:
        return None
    else:
        return x


def func_is_not_none(x):
    if x == 1:
        return None
    else:
        return x


def func_in():
    list1 = [1, 2, 3]
    return list1


def func_not_in():
    list12 = [1, 2, 3]
    return list12


class TheOne:
    pass


class TheTwo(TheOne):
    pass


class TheThree:
    pass


def func_is_instance():
    return TheTwo()


def func_not_is_instance():
    return TheTwo()


class TestFunc(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(func_equal(1, 1), True,  'Right')
        self.assertEqual(func_equal(1, 2), False,  'Wrong')

    def test_not_equal(self):
        self.assertNotEqual(func_not_equal(1, 2), False, 'Right')
        self.assertNotEqual(func_not_equal(1, 1), True,  'Wrong')

    def test_true(self):
        self.assertTrue(func_true(2), 'True')

    def test_false(self):
        self.assertTrue(func_true(2), 'Passed')

    def test_is(self):
        result = func_is(0)
        self.assertIs(result, None, 'Result None when x == 0')

    def test_is_not(self):
        list1 = func_is_not()
        list2 = func_is_not()
        self.assertIsNot(list1, list2, 'list1 and list2 are not same objects')

    def test_is_none(self):
        self.assertIsNone(func_is_none(1), 'the None is come')

    def test_is_not_none(self):
        self.assertIsNotNone(func_is_not_none(2), 'the None not come')

    def test_in(self):
        list2 = func_in()
        self.assertIn(1, list2, 'there no element')

    def test_not_in(self):
        list2 = func_not_in()
        self.assertNotIn(4, list2, 'there element')

    def test_is_instance(self):
        check = func_is_instance()
        self.assertIsInstance(check, TheOne, 'there no object')

    def test_not_is_instance(self):
        check = func_not_is_instance()
        self.assertNotIsInstance(check, TheThree, 'there object')


if __name__ == '__main__':
    unittest.main()
