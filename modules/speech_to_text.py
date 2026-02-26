"""Speech to Text module for deaf users"""

try:
    import whisper
    import sounddevice as sd
    import numpy as np
    HAS_WHISPER = True
except ImportError:
    HAS_WHISPER = False

def run():
    """Run speech-to-text transcription"""
    if not HAS_WHISPER:
        print("⚠️  Speech-to-Text requires: pip install openai-whisper sounddevice numpy")
        print("Demo mode: Would transcribe audio input")
        return
    
    try:
        model = whisper.load_model("base")
        print("🎤 Listening... Speak now (5 seconds)")
        
        audio = sd.rec(int(5 * 16000), samplerate=16000, channels=1)
        sd.wait()
        audio = np.squeeze(audio)
        
        result = model.transcribe(audio)
        print(f"📝 Transcribed: {result['text']}")
    except Exception as e:
        print(f"❌ Error: {e}")
