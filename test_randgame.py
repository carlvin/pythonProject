import unittest
import randomgame


class TestMain(unittest.TestCase):
    def test_randgame(self):
        r=5
        guess = 5
        result = randomgame.run_guess(r,guess)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
