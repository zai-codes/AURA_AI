# AURA_AI

AURA_AI is an assistive application designed to help people with visual and hearing impairments interact with their environment using computer vision, speech-to-text, and audio alerts.

> **GitHub repository:** `https://github.com/<zai-codes>/AURA_AI`  

> After you push a release with a compiled executable, you can also share a one‑click download link such as `https://github.com/<zai-codes>/AURA_AI/releases/latest/download/AURA_AI.exe` which directly delivers the program file.


Contents
- Features
- Accessibility guidance (for deaf and blind users)
- Quickstart
- Creating a distributable & sharing
- Publishing to GitHub
- Contributing & License

## Features
- Real-time object detection and voice-enabled interaction
- Speech-to-text capture and visual transcripts for spoken information
- Visual and audio alerts for important events

## Accessibility guidance

### For deaf users
- Captions & transcripts: Use the `speech_to_text.py` output to display live captions or to save transcripts for later review.
- Visual alerts: Ensure the UI displays clear high-contrast visual cues and large icons when sound alerts are emitted.
- Silent operation: Provide an option to disable audio and rely solely on visual indicators.

### For blind users
- Text-to-speech (TTS): Use the `sound_alert.py` module or an OS-level TTS engine to read transcripts, detections, and menu options aloud.
- Keyboard-first operation: Ensure any UI is fully navigable via keyboard and that command-line mode (`aura_main.py`) exposes all functionality via textual commands.
- Screen reader compatibility: If a GUI is added, use semantic elements and ARIA labels so screen readers can interpret the interface.

## Quickstart

### Prerequisites
- Python 3.8+
- Install dependencies:

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python aura_main.py
```

### Testing

Run the project tests with:

```bash
pytest -q
```

## Creating a distributable (shareable executable)

To create a Windows executable you can share with users who don't run Python, use PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile aura_main.py
```

Distribute the generated executable from the `dist/` folder via GitHub Releases or your preferred hosting.

## Publishing to GitHub and creating a shareable link

1. Initialize a local git repository (if not already):

```bash
git init
git add .
git commit -m "Initial commit"
```

2. Create a GitHub repository (https://github.com/new) named `AURA_AI` and copy the remote URL.

```bash
# example commands once the repo exists:
git remote add origin https://github.com/<your-username>/AURA_AI.git
git branch -M main
git push -u origin main
```

3. Create a Release on GitHub and upload the distributable executable for easy download. The Release page gives you a permanent shareable link.

4. If you add a small web UI, you can host it with GitHub Pages and share a friendlier URL.

### Accessibility-first sharing tips
- For deaf users: include a short README section or a README asset with usage screenshots and a sample transcript file so recipients can preview features visually.
- For blind users: include an audio walkthrough file (MP3) that explains how to run the app and what each option does, and include instructions for enabling TTS on their OS.

## Contributing

Contributions are welcome. Please add a `CONTRIBUTING.md` describing how to open issues and submit pull requests. Include accessibility test cases when possible.

## License

This repository does not include a license file yet. For broad reuse, consider the MIT License. Add a `LICENSE` file in the repository root.

## Contact & support

Open an issue on GitHub for bugs or accessibility requests. Include platform (Windows/macOS/Linux), Python version, and a short description of the problem.

## Notes on privacy

If the app records or transmits speech or images, explicitly document where data is stored and how it is used. Add an option to disable any network uploads and to keep transcripts local.

## Acknowledgements

This project was created to improve accessibility and assistive technology for people with sensory impairments.
