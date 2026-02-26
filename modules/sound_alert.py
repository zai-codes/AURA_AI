"""Sound Alert module for deaf users - detects loud sounds"""

try:
    import sounddevice as sd
    import numpy as np
    HAS_AUDIO = True
except ImportError:
    HAS_AUDIO = False

def run():
    """Run sound detection alert"""
    if not HAS_AUDIO:
        print("⚠️  Sound Alert requires: pip install sounddevice numpy")
        print("Demo mode: Would monitor for loud sounds")
        return
    
    try:
        print("🔊 Listening for loud sounds... (Press Ctrl+C to stop)")
        while True:
            audio = sd.rec(int(1 * 16000), samplerate=16000, channels=1)
            sd.wait()
            volume = np.linalg.norm(audio)
            
            if volume > 10:
                print(f"🚨 LOUD SOUND DETECTED! (Volume: {volume:.1f})")
    except KeyboardInterrupt:
        print("\n✓ Sound detection stopped")
    except Exception as e:
        print(f"❌ Error: {e}")
