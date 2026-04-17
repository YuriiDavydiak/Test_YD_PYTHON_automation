from unittest import TestCase, main
from lesson_07.homework_07 import reverse_string, get_longest_word, find_substring
from lesson_11.homework_11 import sum_numbers


# reverse_string
class TestReverseString(TestCase):

    def test_reverse_string_basic(self):
        actual_result = reverse_string("hello")
        assert actual_result == "olleh"

    def test_reverse_string_empty(self):
        actual_result = reverse_string("")
        assert actual_result == ""

    def test_reverse_string_with_numbers(self):
        actual_result = reverse_string("12345")
        assert actual_result == "54321"

    def test_reverse_string_invalid_type(self):  # негативний
        with self.assertRaises(Exception):
            reverse_string(123)


# get_longest_word
class TestGetLongestWord(TestCase):

    def test_get_longest_word_basic(self):
        actual_result = get_longest_word(["a", "abc", "ab"])
        assert actual_result == "abc"

    def test_get_longest_word_empty(self):
        with self.assertRaises(IndexError):
            get_longest_word([])

    def test_get_longest_word_same_length(self):
        actual_result = get_longest_word(["aa", "bb", "cc"])
        assert actual_result in ["aa", "bb", "cc"]

    def test_get_longest_word_invalid_type(self): # негативний
        actual_result = get_longest_word("not a list")
        assert actual_result in "not a list"

    def test_get_longest_word_none(self): # негативний
        with self.assertRaises(Exception):
            get_longest_word(None)



# sum_numbers
class TestSumNumbers(TestCase):

    def test_sum_numbers_valid(self):
        actual_result = sum_numbers("1,2,3")
        assert actual_result == 6

    def test_sum_numbers_invalid_data(self):
        actual_result = sum_numbers("1,a,3")
        assert actual_result == "Не можу це зробити!"

    def test_sum_numbers_single(self):
        actual_result = sum_numbers("5")
        assert actual_result == 5

    def test_sum_numbers_empty_string(self): # негативний
        actual_result = sum_numbers("")
        assert actual_result == "Не можу це зробити!"

    def test_sum_numbers_none(self): # негативний
        with self.assertRaises(Exception):
            sum_numbers(None)



# find_substring
class TestFindSubstring(TestCase):

    def test_find_substring_found(self):
        actual_result = find_substring("hello world", "world")
        assert actual_result == 6

    def test_find_substring_not_found(self):
        actual_result = find_substring("hello", "xyz")
        assert actual_result == -1

    def test_find_substring_empty(self):
        actual_result = find_substring("", "a")
        assert actual_result == -1

    def test_find_substring_invalid_type(self): # негативний
        with self.assertRaises(Exception):
            find_substring(123, "a")

    def test_find_substring_none(self): # негативний
        with self.assertRaises(Exception):
            find_substring(None, "a")


if __name__ == "__main__":
    main()