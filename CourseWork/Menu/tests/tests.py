import unittest

from CourseWork.Menu.Levenstein import levenshtein


class LevensteinTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_LevensteinTest1(self):
        result = levenshtein('АбвгдключАБВ', 'rusLang')
        self.assertEqual(12.0, result)

    def test_LevensteinTest2(self):
        result = levenshtein('АбвгдключАБВ', 'enLang')
        self.assertEqual(12.0, result)

    def test_LevensteinTest3(self):
        result = levenshtein('А', 'Россия')
        self.assertEqual(6.0, result)

    def test_LevensteinTest4(self):
        result = levenshtein('А', 'United States')
        self.assertEqual(13.0, result)

    def test_LevensteinTest5(self):
        result = levenshtein('', 'United States')
        self.assertEqual(13, result)

    def test_LevensteinTest6(self):
        result = levenshtein('United States', '')
        self.assertEqual(13, result)

    def test_LevensteinTest7(self):
        result = levenshtein('', '')
        self.assertEqual(0, result)