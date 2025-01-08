from unittest import TestCase

from nazli import word_to_pixel_emoji


class NazliTestCase(TestCase):
    def test_not_supported_character(self) -> None:
        expected_result = "\n\n\n\n"

        result = word_to_pixel_emoji("$")

        self.assertEqual(expected_result, result)

    def test_combine_supported_and_not_supported_characters(self) -> None:
        expected_result = "    🌸      🌸🌸🌸🌸    \n  🌸  🌸    🌸      🌸  \n🌸🌸🌸🌸🌸  🌸🌸🌸🌸    \n🌸      🌸  🌸      🌸  \n🌸      🌸  🌸🌸🌸🌸    "

        uppercase_letter_result = word_to_pixel_emoji("A$B")
        lowercase_letter_result = word_to_pixel_emoji("a$b")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_A(self) -> None:
        expected_result = (
            "    🌸      \n  🌸  🌸    \n🌸🌸🌸🌸🌸  \n🌸      🌸  \n🌸      🌸  "
        )

        uppercase_letter_result = word_to_pixel_emoji("A")
        lowercase_letter_result = word_to_pixel_emoji("a")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_B(self) -> None:
        expected_result = (
            "🌸🌸🌸🌸    \n🌸      🌸  \n🌸🌸🌸🌸    \n🌸      🌸  \n🌸🌸🌸🌸    "
        )

        uppercase_letter_result = word_to_pixel_emoji("B")
        lowercase_letter_result = word_to_pixel_emoji("b")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_C(self) -> None:
        expected_result = (
            "  🌸🌸🌸    \n🌸      🌸  \n🌸          \n🌸      🌸  \n  🌸🌸🌸    "
        )

        uppercase_letter_result = word_to_pixel_emoji("C")
        lowercase_letter_result = word_to_pixel_emoji("c")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_D(self) -> None:
        expected_result = (
            "🌸🌸🌸🌸    \n🌸      🌸  \n🌸      🌸  \n🌸      🌸  \n🌸🌸🌸🌸    "
        )

        uppercase_letter_result = word_to_pixel_emoji("D")
        lowercase_letter_result = word_to_pixel_emoji("d")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_E(self) -> None:
        expected_result = (
            "🌸🌸🌸🌸🌸  \n🌸          \n🌸🌸🌸🌸    \n🌸          \n🌸🌸🌸🌸🌸  "
        )

        uppercase_letter_result = word_to_pixel_emoji("E")
        lowercase_letter_result = word_to_pixel_emoji("e")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_F(self) -> None:
        expected_result = (
            "🌸🌸🌸🌸🌸  \n🌸          \n🌸🌸🌸🌸    \n🌸          \n🌸          "
        )

        uppercase_letter_result = word_to_pixel_emoji("F")
        lowercase_letter_result = word_to_pixel_emoji("f")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_G(self) -> None:
        expected_result = (
            "  🌸🌸🌸    \n🌸          \n🌸    🌸🌸  \n🌸      🌸  \n  🌸🌸🌸    "
        )

        uppercase_letter_result = word_to_pixel_emoji("G")
        lowercase_letter_result = word_to_pixel_emoji("g")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_H(self) -> None:
        expected_result = (
            "🌸      🌸  \n🌸      🌸  \n🌸🌸🌸🌸🌸  \n🌸      🌸  \n🌸      🌸  "
        )

        uppercase_letter_result = word_to_pixel_emoji("H")
        lowercase_letter_result = word_to_pixel_emoji("h")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_I(self) -> None:
        expected_result = (
            "  🌸🌸🌸    \n    🌸      \n    🌸      \n    🌸      \n  🌸🌸🌸    "
        )

        uppercase_letter_result = word_to_pixel_emoji("I")
        lowercase_letter_result = word_to_pixel_emoji("i")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_J(self) -> None:
        expected_result = (
            "    🌸🌸🌸  \n      🌸    \n      🌸    \n🌸    🌸    \n  🌸🌸🌸    "
        )

        uppercase_letter_result = word_to_pixel_emoji("J")
        lowercase_letter_result = word_to_pixel_emoji("j")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_K(self) -> None:
        expected_result = (
            "🌸      🌸  \n🌸    🌸    \n🌸🌸🌸      \n🌸    🌸    \n🌸      🌸  "
        )

        uppercase_letter_result = word_to_pixel_emoji("K")
        lowercase_letter_result = word_to_pixel_emoji("k")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_L(self) -> None:
        expected_result = (
            "🌸          \n🌸          \n🌸          \n🌸          \n🌸🌸🌸🌸🌸  "
        )

        uppercase_letter_result = word_to_pixel_emoji("L")
        lowercase_letter_result = word_to_pixel_emoji("l")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_M(self) -> None:
        expected_result = (
            "🌸      🌸  \n🌸🌸  🌸🌸  \n🌸  🌸  🌸  \n🌸      🌸  \n🌸      🌸  "
        )

        uppercase_letter_result = word_to_pixel_emoji("M")
        lowercase_letter_result = word_to_pixel_emoji("m")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_N(self) -> None:
        expected_result = (
            "🌸      🌸  \n🌸🌸    🌸  \n🌸  🌸  🌸  \n🌸    🌸🌸  \n🌸      🌸  "
        )

        uppercase_letter_result = word_to_pixel_emoji("N")
        lowercase_letter_result = word_to_pixel_emoji("n")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_O(self) -> None:
        expected_result = (
            "  🌸🌸🌸    \n🌸      🌸  \n🌸      🌸  \n🌸      🌸  \n  🌸🌸🌸    "
        )

        uppercase_letter_result = word_to_pixel_emoji("O")
        lowercase_letter_result = word_to_pixel_emoji("o")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_P(self) -> None:
        expected_result = (
            "🌸🌸🌸🌸    \n🌸      🌸  \n🌸🌸🌸🌸    \n🌸          \n🌸          "
        )

        uppercase_letter_result = word_to_pixel_emoji("P")
        lowercase_letter_result = word_to_pixel_emoji("p")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_Q(self) -> None:
        expected_result = (
            "  🌸🌸🌸    \n🌸      🌸  \n🌸      🌸  \n🌸    🌸🌸  \n  🌸🌸🌸🌸  "
        )

        uppercase_letter_result = word_to_pixel_emoji("Q")
        lowercase_letter_result = word_to_pixel_emoji("q")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_R(self) -> None:
        expected_result = (
            "🌸🌸🌸🌸    \n🌸      🌸  \n🌸🌸🌸🌸    \n🌸    🌸    \n🌸      🌸  "
        )

        uppercase_letter_result = word_to_pixel_emoji("R")
        lowercase_letter_result = word_to_pixel_emoji("r")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_S(self) -> None:
        expected_result = (
            "  🌸🌸🌸🌸  \n🌸          \n  🌸🌸🌸    \n        🌸  \n🌸🌸🌸🌸    "
        )

        uppercase_letter_result = word_to_pixel_emoji("S")
        lowercase_letter_result = word_to_pixel_emoji("s")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_T(self) -> None:
        expected_result = (
            "🌸🌸🌸🌸🌸  \n    🌸      \n    🌸      \n    🌸      \n    🌸      "
        )

        uppercase_letter_result = word_to_pixel_emoji("T")
        lowercase_letter_result = word_to_pixel_emoji("t")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_U(self) -> None:
        expected_result = (
            "🌸      🌸  \n🌸      🌸  \n🌸      🌸  \n🌸      🌸  \n  🌸🌸🌸    "
        )

        uppercase_letter_result = word_to_pixel_emoji("U")
        lowercase_letter_result = word_to_pixel_emoji("u")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_V(self) -> None:
        expected_result = (
            "🌸      🌸  \n🌸      🌸  \n🌸      🌸  \n  🌸  🌸    \n    🌸      "
        )

        uppercase_letter_result = word_to_pixel_emoji("V")
        lowercase_letter_result = word_to_pixel_emoji("v")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_W(self) -> None:
        expected_result = (
            "🌸      🌸  \n🌸      🌸  \n🌸  🌸  🌸  \n🌸🌸  🌸🌸  \n🌸      🌸  "
        )

        uppercase_letter_result = word_to_pixel_emoji("W")
        lowercase_letter_result = word_to_pixel_emoji("w")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_X(self) -> None:
        expected_result = (
            "🌸      🌸  \n  🌸  🌸    \n    🌸      \n  🌸  🌸    \n🌸      🌸  "
        )

        uppercase_letter_result = word_to_pixel_emoji("X")
        lowercase_letter_result = word_to_pixel_emoji("x")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_Y(self) -> None:
        expected_result = (
            "🌸      🌸  \n  🌸  🌸    \n    🌸      \n    🌸      \n    🌸      "
        )

        uppercase_letter_result = word_to_pixel_emoji("Y")
        lowercase_letter_result = word_to_pixel_emoji("y")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_Z(self) -> None:
        expected_result = (
            "🌸🌸🌸🌸🌸  \n      🌸    \n    🌸      \n  🌸        \n🌸🌸🌸🌸🌸  "
        )

        uppercase_letter_result = word_to_pixel_emoji("Z")
        lowercase_letter_result = word_to_pixel_emoji("z")

        self.assertEqual(expected_result, uppercase_letter_result)
        self.assertEqual(expected_result, lowercase_letter_result)

    def test_comma(self) -> None:
        expected_result = (
            "            \n    🌸      \n  🌸🌸🌸    \n      🌸    \n  🌸🌸      "
        )

        result = word_to_pixel_emoji(",")

        self.assertEqual(expected_result, result)

    def test_open_brace(self) -> None:
        expected_result = (
            "  🌸🌸🌸    \n  🌸        \n  🌸        \n  🌸        \n  🌸🌸🌸    "
        )

        result = word_to_pixel_emoji("[")

        self.assertEqual(expected_result, result)

    def test_close_braces(self) -> None:
        expected_result = (
            "  🌸🌸🌸    \n      🌸    \n      🌸    \n      🌸    \n  🌸🌸🌸    "
        )

        result = word_to_pixel_emoji("]")

        self.assertEqual(expected_result, result)

    def test_open_parenthesis(self) -> None:
        expected_result = (
            "    🌸🌸    \n  🌸        \n🌸          \n  🌸        \n    🌸🌸    "
        )

        result = word_to_pixel_emoji("(")

        self.assertEqual(expected_result, result)

    def test_open_curly_brace(self) -> None:
        expected_result = (
            "  🌸🌸      \n  🌸        \n🌸          \n  🌸        \n  🌸🌸      "
        )

        result = word_to_pixel_emoji("{")

        self.assertEqual(expected_result, result)

    def test_close_curly_brace(self) -> None:
        expected_result = (
            "    🌸🌸    \n      🌸    \n        🌸    \n      🌸    \n    🌸🌸    "
        )

        result = word_to_pixel_emoji("}")

        self.assertEqual(expected_result, result)

    def test_plus(self) -> None:
        expected_result = (
            "            \n    🌸      \n  🌸🌸🌸    \n    🌸      \n            "
        )

        result = word_to_pixel_emoji("+")

        self.assertEqual(expected_result, result)

    def test_minus(self) -> None:
        expected_result = (
            "            \n            \n  🌸🌸🌸    \n            \n            "
        )

        result = word_to_pixel_emoji("-")

        self.assertEqual(expected_result, result)

    def test_point(self) -> None:
        expected_result = (
            "            \n            \n            \n            \n    🌸      "
        )

        result = word_to_pixel_emoji(".")

        self.assertEqual(expected_result, result)

    def test_start(self) -> None:
        expected_result = (
            "    🌸      \n🌸  🌸  🌸  \n  🌸🌸🌸    \n🌸  🌸  🌸  \n    🌸    "
        )

        result = word_to_pixel_emoji("*")

        self.assertEqual(expected_result, result)

    def test_divide(self) -> None:
        expected_result = (
            "        🌸  \n      🌸    \n    🌸      \n  🌸        \n🌸          "
        )

        result = word_to_pixel_emoji("/")

        self.assertEqual(expected_result, result)

    def test_colon(self) -> None:
        expected_result = (
            "            \n    🌸      \n            \n    🌸      \n            "
        )

        result = word_to_pixel_emoji(":")

        self.assertEqual(expected_result, result)

    def test_equals(self) -> None:
        expected_result = (
            "            \n🌸🌸🌸🌸🌸  \n            \n🌸🌸🌸🌸🌸  \n            "
        )

        result = word_to_pixel_emoji("=")

        self.assertEqual(expected_result, result)

    def test_less_than(self) -> None:
        expected_result = (
            "      🌸    \n    🌸      \n  🌸        \n    🌸      \n      🌸    "
        )

        result = word_to_pixel_emoji("<")

        self.assertEqual(expected_result, result)

    def test_greater_than(self) -> None:
        expected_result = (
            "  🌸        \n    🌸      \n      🌸    \n    🌸      \n  🌸        "
        )

        result = word_to_pixel_emoji(">")

        self.assertEqual(expected_result, result)

    def test_percent(self) -> None:
        expected_result = "🌸🌸      🌸  \n🌸🌸    🌸    \n      🌸      \n    🌸  🌸🌸  \n  🌸    🌸🌸  "

        result = word_to_pixel_emoji("%")

        self.assertEqual(expected_result, result)

    def test_hat(self) -> None:
        expected_result = (
            "    🌸      \n  🌸  🌸    \n🌸      🌸  \n            \n            "
        )

        result = word_to_pixel_emoji("^")

        self.assertEqual(expected_result, result)

    def test_exclamation(self) -> None:
        expected_result = (
            "    🌸      \n    🌸      \n    🌸      \n            \n    🌸      "
        )

        result = word_to_pixel_emoji("!")

        self.assertEqual(expected_result, result)

    def test_question_mark(self) -> None:
        expected_result = (
            "  🌸🌸🌸    \n🌸      🌸  \n    🌸🌸    \n    🌸      \n    🌸      "
        )

        result = word_to_pixel_emoji("?")

        self.assertEqual(expected_result, result)

    def test_zero(self) -> None:
        expected_result = (
            "  🌸🌸🌸    \n🌸      🌸  \n🌸      🌸  \n🌸      🌸  \n  🌸🌸🌸    "
        )

        result = word_to_pixel_emoji("0")

        self.assertEqual(expected_result, result)

    def test_one(self) -> None:
        expected_result = (
            "    🌸      \n  🌸🌸      \n    🌸      \n    🌸      \n  🌸🌸🌸    "
        )

        result = word_to_pixel_emoji("1")

        self.assertEqual(expected_result, result)

    def test_two(self) -> None:
        expected_result = (
            "🌸🌸🌸🌸🌸  \n        🌸  \n🌸🌸🌸🌸🌸  \n🌸          \n🌸🌸🌸🌸🌸  "
        )

        result = word_to_pixel_emoji("2")

        self.assertEqual(expected_result, result)

    def test_three(self) -> None:
        expected_result = (
            "🌸🌸🌸🌸🌸  \n        🌸  \n    🌸🌸🌸  \n        🌸  \n🌸🌸🌸🌸🌸  "
        )

        result = word_to_pixel_emoji("3")

        self.assertEqual(expected_result, result)

    def test_four(self) -> None:
        expected_result = (
            "🌸      🌸  \n🌸      🌸  \n🌸🌸🌸🌸🌸  \n        🌸  \n        🌸  "
        )

        result = word_to_pixel_emoji("4")

        self.assertEqual(expected_result, result)

    def test_five(self) -> None:
        expected_result = (
            "🌸🌸🌸🌸🌸  \n🌸          \n🌸🌸🌸🌸🌸  \n        🌸  \n🌸🌸🌸🌸🌸  "
        )

        result = word_to_pixel_emoji("5")

        self.assertEqual(expected_result, result)

    def test_six(self) -> None:
        expected_result = (
            "🌸🌸🌸🌸🌸  \n🌸          \n🌸🌸🌸🌸🌸  \n🌸      🌸  \n🌸🌸🌸🌸🌸  "
        )

        result = word_to_pixel_emoji("6")

        self.assertEqual(expected_result, result)

    def test_seven(self) -> None:
        expected_result = (
            "🌸🌸🌸🌸🌸  \n        🌸  \n      🌸    \n    🌸      \n  🌸        "
        )

        result = word_to_pixel_emoji("7")

        self.assertEqual(expected_result, result)

    def test_eight(self) -> None:
        expected_result = (
            "🌸🌸🌸🌸🌸  \n🌸      🌸  \n🌸🌸🌸🌸🌸  \n🌸      🌸  \n🌸🌸🌸🌸🌸  "
        )

        result = word_to_pixel_emoji("8")

        self.assertEqual(expected_result, result)

    def test_nine(self) -> None:
        expected_result = (
            "🌸🌸🌸🌸🌸  \n🌸      🌸  \n🌸🌸🌸🌸🌸  \n        🌸  \n🌸🌸🌸🌸🌸  "
        )

        result = word_to_pixel_emoji("9")

        self.assertEqual(expected_result, result)

    def test_space(self) -> None:
        expected_result = "      \n      \n      \n      \n      "

        result = word_to_pixel_emoji(" ")

        self.assertEqual(expected_result, result)
