from unittest import TestCase

from nazli import word_to_pixel_emoji


class NazliTestCase(TestCase):
    def test_present_A(self) -> None:
        expected_result = (
            "    🌸      \n  🌸  🌸    \n🌸🌸🌸🌸🌸  \n🌸      🌸  \n🌸      🌸  "
        )

        result = word_to_pixel_emoji("A")

        self.assertEqual(expected_result, result)

    def test_present_B(self) -> None:
        expected_result = (
            "🌸🌸🌸🌸    \n🌸      🌸  \n🌸🌸🌸🌸    \n🌸      🌸  \n🌸🌸🌸🌸    "
        )

        result = word_to_pixel_emoji("B")

        self.assertEqual(expected_result, result)

    def test_present_C(self) -> None:
        expected_result = (
            "  🌸🌸🌸    \n🌸      🌸  \n🌸          \n🌸      🌸  \n  🌸🌸🌸    "
        )

        result = word_to_pixel_emoji("C")

        self.assertEqual(expected_result, result)
