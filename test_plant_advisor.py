import unittest

from plant_advisor import recommend_watering


class PlantAdvisorTests(unittest.TestCase):
    def test_dry_bright_conditions_need_high_watering(self):
        self.assertEqual(recommend_watering(15, 32, 9), "high")

    def test_invalid_moisture_is_rejected(self):
        with self.assertRaises(ValueError):
            recommend_watering(120, 24, 6)


if __name__ == "__main__":
    unittest.main()
