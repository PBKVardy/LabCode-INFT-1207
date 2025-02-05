import csv
import unittest
from reading_list import add_book, list_books, search_book

class TestReadingList(unittest.TestCase):
    def test_add_book(self):
        # Test adding a book.
        add_book("Test Book", "Author Name", "2022")
        with open("books.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
        self.assertIn(["Test Book", "Author Name", "2022"], rows)

        # Test cases where there should be an error
        no_author = add_book("Test Book 2", "", "2031")
        self.assertEqual(no_author, "Error: Author cannot be empty.")

        no_title = add_book("", "Author Name 3", "2023")
        self.assertEqual(no_title, "Error: Title cannot be empty.")

        no_year = add_book("Test Book 4", " Author Name 4", "")
        self.assertEqual(no_year, "Error: Year cannot be empty.")

        invalid_year = add_book("Test Book 5", "Author Name 5", "abc")
        self.assertEqual(invalid_year, "Error: Year must be a number.")




    def test_search_book(self):
        # Test searching for an existing book.
        output_result = search_book("Test Book")  # Now it returns a value
        expected_output = "Found: Title: Test Book, Author: Author Name, Year: 2022"
        self.assertEqual(output_result, expected_output, "search_book did not return the expected output.")


if __name__ == '__main__':
    unittest.main()