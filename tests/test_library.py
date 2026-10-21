import unittest
import pas2_unit_converter as api


class Tests(unittest.TestCase):
    def test_length(self):
        self.assertAlmostEqual(api.convert(1, "ft", "cm"), 30.48)

    def test_temperature(self):
        self.assertAlmostEqual(api.convert(32, "F", "C"), 0.0, places=9)
        self.assertAlmostEqual(api.convert(100, "C", "F"), 212.0)

    def test_invalid(self):
        for args in [(1, "kg", "m"), (-1, "K", "C"), (float("nan"), "m", "km")]:
            with self.assertRaises(ValueError):
                api.convert(*args)


if __name__ == "__main__":
    unittest.main()
