# test_components.py
import components
import unittest
from components import fetch_data, process_data, display_data

class TestComponents(unittest.TestCase):
    
    def test_fetch_data(self):
        # Test Component A
        self.assertEqual(fetch_data("http://example.com"), {"data": [1, 2, 3]})
        with self.assertRaises(ValueError):
            fetch_data("invalid_url")

    def test_process_data(self):
        # Test Component B
        self.assertEqual(process_data({"data": [1, 2, 3]}), [2, 4, 6])
        with self.assertRaises(ValueError):
            process_data({"invalid_key": [1, 2, 3]})

    def test_display_data(self):
        # Test Component C
        self.assertEqual(display_data([2, 4, 6]), "Processed Data: 2, 4, 6")
        self.assertEqual(display_data([]), "No data to display")

if __name__ == '__main__':
    unittest.main()
