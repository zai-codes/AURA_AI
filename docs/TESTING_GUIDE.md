# Testing Guide for AURA-AI Accessibility Features

## **Quick Start Testing**

### **1. Test Sound Alert (Deaf User Feature)**

#### Manual Testing
```bash
# Run the app and select option 2 (Sound Alert)
python aura_main.py
# Choose: 2 - Sound Alert (Deaf)

# Test scenarios:
```

| Scenario | How to Test | Expected Result |
|----------|------------|-----------------|
| **Quiet Room** | Run sound alert, stay silent | No alert 🔇 |
| **Normal Speech** | Run sound alert, speak normally | No alert (speech ~70-80dB) |
| **Loud Clap** | Run sound alert, clap loudly | 🚨 LOUD SOUND DETECTED! |
| **Doorbell** | Play doorbell sound (~80dB) | Should trigger alert 🚨 |
| **Alarm/Siren** | Play alarm sound (~110dB) | Definitely triggers 🚨 |
| **Music** | Play loud music | Depends on volume, should alert if loud |

#### What Deaf Users Need:
- ❌ **Don't rely only on audio feedback**
- ✅ **Visual indicators**: Clear emoji alerts (🚨)
- ✅ **Text output**: "LOUD SOUND DETECTED! (Volume: XX.X)"
- ✅ **Vibration**: Add haptic feedback (optional enhancement)

---

### **2. Test Speech-to-Text (Deaf User Feature)**

```bash
python aura_main.py
# Choose: 1 - Speech to Text (Deaf)
```

**Testing Checklist:**
- [ ] Microphone works (app detects audio input)
- [ ] Transcription is accurate (say clear sentences)
- [ ] Text output is visible and readable
- [ ] Clear start/stop feedback

---

### **3. Test Object Detection (Blind User Feature)**

```bash
python aura_main.py
# Choose: 3 - Object Detection (Blind)
```

**For Blind Users Testing:**
- [ ] Objects are detected and described in text
- [ ] Audio feedback for detected objects (enhancement needed)
- [ ] Real-time feedback about what's being detected
- [ ] Easy exit with 'q' key

---

### **4. Test Voice Object Detection (Blind User Feature)**

```bash
python aura_main.py
# Choose: 4 - Voice Object Detection (Blind)
```

---

## **Automated Testing**

### **Run All Tests**
```bash
pip install pytest pytest-cov
pytest tests/ -v
pytest tests/test_accessibility.py -v
```

### **Run Specific Test Categories**
```bash
# Test only sound alert
pytest tests/test_accessibility.py::TestSoundAlert -v

# Test only accessibility features
pytest tests/test_accessibility.py::TestAccessibilityFeatures -v

# Real-world scenarios
pytest tests/test_accessibility.py::TestRealWorldScenarios -v
```

### **Test Coverage Report**
```bash
pytest tests/test_accessibility.py --cov=modules --cov-report=html
# Opens coverage report in htmlcov/index.html
```

---

## **Accessibility Testing Checklist**

### **For Deaf Users:**

#### Sound Alert (Option 2)
- [ ] Visual feedback is clear and obvious
- [ ] No reliance on audio-only alerts
- [ ] Emoji/text clearly indicates alert type (🚨 LOUD SOUND)
- [ ] Volume measurement is shown (dB level)
- [ ] Can run continuously without fatigue
- [ ] Easy to start/stop (Ctrl+C works smoothly)

#### Speech-to-Text (Option 1)
- [ ] Visual confirmation of recording start
- [ ] Text output is large and readable
- [ ] Transcription errors are visible to correct
- [ ] No audio-only feedback required to use feature

### **For Blind Users:**

#### Object Detection (Option 3)
- [ ] Audio description of detected objects ⚠️ **TODO**: Add voice output
- [ ] Text-based detection results
- [ ] Easy keyboard navigation (no mouse required)
- [ ] Clear feedback about what's happening

#### Voice Object Detection (Option 4)
- [ ] Audio feedback for commands
- [ ] Voice recognition is clear
- [ ] Audio announcements of detected objects

### **For All Users:**

- [ ] Clear error messages (text-based, not icon-only)
- [ ] Keyboard-only navigation possible
- [ ] No flashing/strobe effects (seizure risk)
- [ ] Font sizes readable without zoom
- [ ] High contrast between text and background

---

## **Volume Detection Testing**

### **Understand the Volume Scale**

```python
# Current threshold: > 10 (needs calibration)

Sound Level Examples:
- Silence: 0-1
- Whisper: 1-3
- Normal conversation: 3-8
- Raised voice: 8-15
- Loud music: 15-30
- Alarm/siren: 30-50+
```

### **Calibration Test**
```bash
# Edit modules/sound_alert.py 
# Change threshold from 10 to test different levels:
if volume > 10:  # Adjust this number
    print(f"Alert! Volume: {volume:.1f}")
```

**Recommended thresholds:**
- 8: Very sensitive (detects speech)
- 10: Balanced (detects loud sounds)
- 15: Less sensitive (only loud alerts)

---

## **Problem Scenarios to Test**

### **Scenario 1: Background Noise**
```bash
# Test in different environments:
# - Quiet room
# - Office with fans
# - Street with traffic
# - Coffee shop

# Expected: Should not give false alarms
```

### **Scenario 2: Hearing Aid Feedback**
- Test with hearing aids enabled (high-frequency buzzing)
- Should detect as loud sound

### **Scenario 3: Emergency Situations**
- Smoke alarm: ~85dB ✅
- Car horn: ~110dB ✅
- Baby crying: ~100dB ✅
- Phone notification: ~60dB ✅ (depends on threshold)

### **Scenario 4: Battery Low / Device Disabled**
- Test graceful failure
- Show clear warning message
- Offer demo mode

---

## **Enhancements Needed (For Better Accessibility)**

### **For Deaf Users:**
1. ✅ Visual alerts (already done)
2. 🔲 **Haptic feedback** (phone vibration)
3. 🔲 **Customizable volume threshold**
4. 🔲 **Recording of alerts** (history logs)
5. 🔲 **Different alert types** (different emoji/patterns for different sounds)

### **For Blind Users:**
1. 🔲 **Audio descriptions** of detected objects
2. 🔲 **Text-to-speech** for all output
3. 🔲 **Screen reader** compatibility testing

### **For Everyone:**
1. 🔲 **Settings menu** to customize sensitivity
2. 🔲 **Help system** (accessible to all abilities)
3. 🔲 **Logging** of events for review

---

## **Running Tests in CI/CD**

```yaml
# .github/workflows/test.yml (if using GitHub)
name: Accessibility Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install -r requirements.txt pytest numpy
      - run: pytest tests/ -v
```

---

## **Testing Tools Recommended**

| Tool | Purpose |
|------|---------|
| `pytest` | Unit testing (automation) |
| `pylint` | Code quality |
| `screen-reader` | Test with NVDA/JAWS |
| `wave` | Web accessibility evaluation |
| Microphone calibrator | Test sound levels |
| Video analysis | Record and analyze alert triggers |

---

## **Questions to Ask Test Users:**

1. **For Deaf Users**: "Can you understand what the app is alerting you to without any sound?"
2. **For Blind Users**: "Can you use all features using keyboard only?"
3. **For Both**: "Are error messages clear when something goes wrong?"
4. **General**: "Is the app easy to understand and use?"

---

## **Success Criteria**

✅ Sound alert triggers on loud sounds (>80dB+)
✅ Deaf user can see all alerts without audio
✅ Blind user can use all features without vision
✅ App fails gracefully with clear messages
✅ No dependencies block basic functionality
✅ All keyboard navigation works
✅ Error messages are visible and helpful
