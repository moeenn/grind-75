from unittest import TestCase

from .valid_parentheses import valid_parentheses


class ValidParenthesesTest(TestCase):
    def test_valid_cases(self) -> None:
        valid_cases = ["()", "()[]{}", "([])"]

        for tc in valid_cases:
            actual = valid_parentheses(tc)
            self.assertTrue(actual)

    def test_invalid_cases(self) -> None:
        invalid_cases = ["(]", "([)]"]

        for tc in invalid_cases:
            actual = valid_parentheses(tc)
            self.assertFalse(actual)
