
# Nazli - Word to Pixel Emoji

This Python project converts text into pixel-art-style emojis, transforming each character into a creative and visually appealing grid of emojis.

## Features

- **Pixel Art Transformation:** Converts words into pixel-art-style emoji grids.
- **Customizable Emojis:** Choose your own emojis for the "filled" and "empty" parts of the pixel art.
- **Flexible Input:** Handles multi-character words and adjusts spacing based on emoji width.
- **Simple Integration:** Designed for easy integration into larger projects or standalone use.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/kamyarmg/nazli.git
   cd nazli
   ```

2. Import the module into your project:
   ```python
   from nazli import word_to_pixel_emoji

   print(word_to_pixel_emoji("I", filled_emoji="🌺"))
   print(word_to_pixel_emoji("Wish", filled_emoji="🌸"))
   print(word_to_pixel_emoji("You", filled_emoji="🧊"))
   print(word_to_pixel_emoji("The", filled_emoji="🍀"))
   print(word_to_pixel_emoji("Best.", filled_emoji="🌟"))
   ```

#### Output Example:
```
  🌺🌺🌺
    🌺
    🌺
    🌺
  🌺🌺🌺

🌸      🌸    🌸🌸🌸      🌸🌸🌸🌸  🌸      🌸
🌸      🌸      🌸      🌸          🌸      🌸
🌸  🌸  🌸      🌸        🌸🌸🌸    🌸🌸🌸🌸🌸
🌸🌸  🌸🌸      🌸              🌸  🌸      🌸
🌸      🌸    🌸🌸🌸    🌸🌸🌸🌸    🌸      🌸

🧊      🧊    🧊🧊🧊    🧊      🧊
  🧊  🧊    🧊      🧊  🧊      🧊
    🧊      🧊      🧊  🧊      🧊
    🧊      🧊      🧊  🧊      🧊
    🧊        🧊🧊🧊      🧊🧊🧊

🍀🍀🍀🍀🍀  🍀      🍀  🍀🍀🍀🍀🍀
    🍀      🍀      🍀  🍀
    🍀      🍀🍀🍀🍀🍀  🍀🍀🍀🍀
    🍀      🍀      🍀  🍀
    🍀      🍀      🍀  🍀🍀🍀🍀🍀

🌟🌟🌟🌟    🌟🌟🌟🌟🌟    🌟🌟🌟🌟  🌟🌟🌟🌟🌟
🌟      🌟  🌟          🌟              ‌ 🌟
🌟🌟🌟🌟    🌟🌟🌟🌟      🌟🌟🌟        🌟
🌟      🌟  🌟                  🌟       🌟
🌟🌟🌟🌟    🌟🌟🌟🌟🌟  🌟🌟🌟🌟        🌟          🌟



```

### Key Functions

1. **`word_to_pixel_emoji(word: str, filled_emoji: str = "🌸") -> str`**
   - Converts a word into a grid of pixel emoji art.
   - Parameters:
     - `word`: The text to convert.
     - `filled_emoji`: The emoji to use for the filled portions of the grid (default: 🌸).

   - Returns:
     - A string containing the pixel-art emoji representation of the word.

2. **`char_to_pixel_emoji(char: str, filled_emoji: str, empty_emoji: str) -> list[str] | None`**
   - Converts a single character to a pixel-art representation.
   - Returns `None` if the character is not in the pixel map.

3. **`emoji_length(emoji: str) -> int`**
   - Calculates the visual width of an emoji based on its Unicode properties.

## Pixel Map

The pixel map for each character is stored in `PIXEL_MAP` and defines how each letter is visualized. You can customize this mapping by updating the `pixel_art.py` module.

### Example Mapping
```python
PIXEL_MAP = {
    "A": [
        "  X  ",
        " X X ",
        "XXXXX",
        "X   X",
        "X   X",
    ],
    # Add more characters...
}
```

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to enhance the functionality or add support for additional features. For more information, please see the [CONTRIBUTING.md](CONTRIBUTING.md)
