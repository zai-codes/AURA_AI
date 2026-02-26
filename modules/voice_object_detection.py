"""Voice + Object Detection module for blind users"""

try:
    from ultralytics import YOLO  # type: ignore
    import cv2  # type: ignore
    import pyttsx3  # type: ignore
    HAS_VOICE_VISION = True
except ImportError:
    HAS_VOICE_VISION = False

def run():
    """Run combined voice and object detection"""
    if not HAS_VOICE_VISION:
        print("⚠️  Voice Object Detection requires: pip install ultralytics opencv-python pyttsx3")
        print("Demo mode: Would detect objects and announce them")
        return
    
    try:
        engine = pyttsx3.init()
        model = YOLO("yolov8n.pt")
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("❌ Error: Camera not available")
            return
        
        print("📹🔊 Voice Object Detection started (Press 'q' to quit)")
        while True:
            ret, frame = cap.read()
            if not ret:
                print("❌ Error: Failed to read from camera")
                break
            
            results = model(frame)
            names = results[0].names
            boxes = results[0].boxes
            
            for box in boxes:
                cls = int(box.cls[0])
                label = names[cls]
                print(f"🎯 Detected: {label}")
                engine.say(label)
                engine.runAndWait()
            
            annotated_frame = results[0].plot()
            cv2.imshow("AURA AI", annotated_frame)
            
            if cv2.waitKey(1) == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"❌ Error: {e}")
        if 'cap' in locals():
            cap.release()
        if 'cv2' in locals():
            cv2.destroyAllWindows()
