import sys
from pathlib import Path

# Ensure project root is on sys.path so `modules` package can be imported
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from modules import speech_to_text, sound_alert, object_detection, voice_object_detection

def main():
    print("=== AURA-AI Assistive System ===")
    print("1 - Speech to Text (Deaf)")
    print("2 - Sound Alert (Deaf)")
    print("3 - Object Detection (Blind)")
    print("4 - Voice Object Detection (Blind)")
    choice = input("Choose mode: ")

    if choice == "1":
        speech_to_text.run()
    elif choice == "2":
        sound_alert.run()
    elif choice == "3":
        object_detection.run()
    elif choice == "4":
        voice_object_detection.run()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

