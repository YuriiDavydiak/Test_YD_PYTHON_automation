from unittest import TestCase, main
from lesson_07.homework_07 import reverse_string, get_longest_word, find_substring
from lesson_11.homework_11 import sum_numbers


class TestHomeworks(TestCase):

    #  reverse_string
    def test_reverse_string_basic(self):
        test_input = "hello"

        actual_result = reverse_string(test_input)

        assert actual_result == "olleh"

    def test_reverse_string_empty(self):
        test_input = ""

        actual_result = reverse_string(test_input)

        assert actual_result == ""

    #  get_longest_word
    def test_get_longest_word_basic(self):
        test_input = ["a", "abc", "ab"]

        actual_result = get_longest_word(test_input)

        assert actual_result == "abc"

    def test_get_longest_word_empty(self):
        test_input = []

        actual_result = get_longest_word(test_input)

        assert actual_result == ""

    #  sum_numbers
    def test_sum_numbers_valid(self):
        test_input = "1,2,3"

        actual_result = sum_numbers(test_input)

        assert actual_result == 6

    def test_sum_numbers_invalid(self):
        test_input = "1,a,3"

        actual_result = sum_numbers(test_input)

        assert actual_result == "Не можу це зробити!"

    def test_sum_numbers_single(self):
        test_input = "5"

        actual_result = sum_numbers(test_input)

        assert actual_result == 5

    #  find_substring
    def test_find_substring_found(self):
        str1 = "hello world"
        str2 = "world"

        actual_result = find_substring(str1, str2)

        assert actual_result == 6

    def test_find_substring_not_found(self):
        str1 = "hello"
        str2 = "xyz"

        actual_result = find_substring(str1, str2)

        assert actual_result == -1

    def test_find_substring_empty(self):
        str1 = ""
        str2 = "a"

        actual_result = find_substring(str1, str2)

        assert actual_result == -1


if __name__ == "__main__":
    main()