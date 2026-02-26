# Contributing to AURA_AI

Thank you for your interest in improving AURA_AI! We welcome contributions of
all kinds, especially those that enhance accessibility.

## How to contribute

1. **Fork the repository** on GitHub.
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/<zai-codes>/AURA_AI.git
   cd AURA_AI
   ```
3. **Create a new branch** for your work:
   ```bash
   git checkout -b feature/your-descriptive-name
   ```
4. **Make your changes** – add tests for new behaviour or edge cases.
5. **Run the test suite** before submitting:
   ```bash
   pytest -q
   ```
6. **Commit your changes** with a clear message:
   ```bash
   git add .
   git commit -m "Describe your change"
   ```
7. **Push your branch** and open a pull request on GitHub.

## Accessibility considerations

- Ensure any new UI elements are screen-reader friendly.
- When adding audio or visual output, provide alternatives (captions, TTS).
- Update documentation with usage examples and screenshots or audio guides.

## Code style

- Follow PEP 8 for Python code. Use `flake8` or `black` to format.

## Reporting bugs

File an issue with a detailed description, steps to reproduce, and platform
information (OS, Python version, hardware if relevant).

## License

By contributing, you agree that your contributions will be licensed under
the [MIT License](./LICENSE).
