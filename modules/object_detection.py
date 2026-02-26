"""Object Detection module for blind users"""

try:
    from ultralytics import YOLO  # type: ignore
    import cv2  # type: ignore
    HAS_VISION = True
except ImportError:
    HAS_VISION = False

def run():
    """Run real-time object detection"""
    if not HAS_VISION:
        print("⚠️  Object Detection requires: pip install ultralytics opencv-python")
        print("Demo mode: Would detect objects from camera")
        return
    
    try:
        model = YOLO("yolov8n.pt")
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("❌ Error: Camera not available")
            return
        
        print("📹 Object Detection started (Press 'q' to quit)")
        while True:
            ret, frame = cap.read()
            if not ret:
                print("❌ Error: Failed to read from camera")
                break
            
            results = model(frame)
            annotated_frame = results[0].plot()
            
            cv2.imshow("Object Detection", annotated_frame)
            
            if cv2.waitKey(1) == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"❌ Error: {e}")
        if 'cap' in locals():
            cap.release()
        cv2.destroyAllWindows()
