def gemiddelde(cijfers):
    return str(sum(cijfers)/len(cijfers))
import unittest
class TestsGemiddelde(unittest.TestCase):
    """Tests voor de functie ''gemiddelde''."""
    def test_functie_gemiddelde_met_niet_lege_lijst(self):
        """Werkt de functie met een cijferlijst?"""
        print("Het gemiddelde is: " + gemiddelde([5,6,7,8,9]))
    def test_function_gem_met_lege_lijst(self):
        """Werpt de functie een fout op met een lege lijst"""
        with self.assertRaises(ZeroDivisionError):
            gemiddelde([])
        if __name__ == '__main__':
            unittest.main()


if __name__ == '__main__':
    unittest.main()

