import unicodedata

from nazli.pixel_art import PIXEL_MAP


def word_to_pixel_emoji(word: str, filled_emoji: str = "🌸") -> str:
    lines = ["" for _ in range(5)]
    for char in word:
        p_art = pixel_art(filled_emoji, char)
        if p_art is not None:
            for i in range(5):
                lines[i] += p_art[i] + " " * emoji_length(filled_emoji)
    return "\n".join(lines)


def pixel_art(filled_emoji: str, char: str) -> None | list[str]:
    return char_to_pixel_emoji(
        char.upper(),
        filled_emoji,
        " " * emoji_length(filled_emoji),
    )


def char_to_pixel_emoji(
    char: str, filled_emoji: str, empty_emoji: str
) -> None | list[str]:
    return (
        [
            line.replace("X", filled_emoji).replace(" ", empty_emoji)
            for line in PIXEL_MAP[char]
        ]
        if char in PIXEL_MAP
        else None
    )


def emoji_length(emoji: str) -> int:
    width = 0
    for e in emoji:
        ch_type = unicodedata.east_asian_width(e)
        if ch_type == "W":
            width += 2
        if ch_type == "N":
            width += 1
    return width
