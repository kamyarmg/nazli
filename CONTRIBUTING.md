Here's a professional and comprehensive `CONTRIBUTING.md` file for your repository:

---

# Contributing to Nazli

Thank you for your interest in contributing to **Nazli**! 🎉 We welcome contributions of all kinds—whether you're fixing bugs, improving documentation, adding new features, or expanding the character set.

This document outlines the guidelines for contributing to the project to ensure smooth collaboration.

## Table of Contents
- [Contributing to Nazli](#contributing-to-nazli)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
  - [Code of Conduct](#code-of-conduct)
  - [How to Contribute](#how-to-contribute)
    - [Reporting Issues](#reporting-issues)
    - [Submitting Pull Requests](#submitting-pull-requests)
    - [Adding New Fonts or Characters](#adding-new-fonts-or-characters)
    - [Improving Documentation](#improving-documentation)
  - [Development Workflow](#development-workflow)
  - [License](#license)

---

## Getting Started

1. **Fork the repository:**
   Start by forking the repository to your GitHub account.

2. **Clone your fork:**
   ```bash
   git clone https://github.com/kamyarmg/nazli.git
   cd nazli
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements-dev.txt
   ```

4. **Run tests (if applicable):**
   Verify that everything is working before making changes:
   ```bash
   tox
   ```
5. **Install pre-commit:**
   Install pre-commit to lint code and etc.
   ```bash
   pre-commit install
   ```

---

## Code of Conduct

We follow a [Code of Conduct](CODE_OF_CONDUCT.md) to ensure that this project remains a welcoming and inclusive space for everyone. Please take a moment to review it before contributing.

---

## How to Contribute

### Reporting Issues
If you find a bug or have a feature request, please [open an issue](https://github.com/kamyarmg/nazli/issues). When reporting:
- Provide clear steps to reproduce the problem (if applicable).
- Include details about your environment, such as Python version and operating system.
- Be specific and concise about your suggestion or issue.

### Submitting Pull Requests
We welcome pull requests for bug fixes, new features, or any other improvements. Here's how to submit one:

1. **Create a new branch:**
   ```bash
   git checkout -b feature-name
   ```

2. **Make your changes.**
3. **Run tests:**
   Ensure your changes don’t break existing functionality:
   ```bash
   pytest
   ```

4. **Commit your changes:**
   Use clear and concise commit messages:
   ```bash
   git commit -m "Add feature: description of the feature"
   ```

5. **Push to your fork:**
   ```bash
   git push origin feature-name
   ```

6. **Submit a pull request:**
   Go to the original repository, click on "New Pull Request," and describe your changes in detail.

---

### Adding New Fonts or Characters
We’re thrilled to see contributions that expand the versatility of the project!

- **Adding Characters:**
  1. Locate the `PIXEL_MAP` in `pixel_art.py`.
  2. Add a new character by defining its pixel grid as a list of strings. For example:
     ```python
     PIXEL_MAP["B"] = [
         "XXXXX",
         "X   X",
         "XXXXX",
         "X   X",
         "XXXXX",
     ]
     ```
  3. Verify your new character with test cases.

- **Adding New Fonts:**
  If you'd like to add a new pixel font style:
  1. Create a new dictionary with the character mappings.
  2. Include it in a way that users can switch between fonts easily.
  3. Ensure all characters in the font set are aligned and visually consistent.

We’re happy to guide you through the process—feel free to ask questions by [opening an issue](https://github.com/kamyarmg/nazli/issues)!

### Improving Documentation
Documentation is just as important as the code itself! You can contribute by:
- Fixing typos or grammatical errors.
- Adding examples or explanations to make the project easier to understand.
- Updating the `README.md` or any other project documentation.

---

## Development Workflow

1. **Set up the development environment:**
   Ensure you have Python installed and all dependencies are configured using `pip install -r requirements-dev.txt`.

2. **Test your changes:**
   Add unit tests for new features or modified code. We aim for high test coverage to maintain reliability.

3. **Lint your code:**
   Follow the PEP 8 style guide for Python. Use tools like `ruff` to check for style violations:
   ```bash
   ruff
   ```

4. **Submit a pull request:**
   Include a clear description of your changes and reference any related issues.

---


---

## License

By contributing to this project, you agree that your contributions will be licensed under the [MIT License](LICENSE).

---

We’re excited to have you on board and can’t wait to see your contributions! 😊
