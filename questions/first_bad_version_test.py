from unittest import TestCase

from .first_bad_version import first_bad_version


class TestFirstBadVersion(TestCase):
    def test_simple(self) -> None:
        def is_bad_version(n: int) -> bool:
            versions = [False, False, False, True, True]
            return versions[n - 1]

        actual = first_bad_version(5, is_bad_version)
        self.assertEqual(4, actual)

    def test_one_version(self) -> None:
        def test_simple(self) -> None:
            def is_bad_version(n: int) -> bool:
                versions = [True]
                return versions[n - 1]

            actual = first_bad_version(1, is_bad_version)
            self.assertEqual(1, actual)
