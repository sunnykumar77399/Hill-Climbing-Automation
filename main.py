import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
import time
import sys


pyautogui.FAILSAFE = False


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam. Please check if your camera is connected.")
    sys.exit(1)


detector = HandDetector(detectionCon=0.8, maxHands=1)

print("Hill Climb Racing Gesture Control")
print("Controls:")
print("- Open palm (all fingers up) -> Right Arrow (Accelerate)")
print("- Closed palm (fist) -> Left Arrow (Brake)")
print("- Other gestures -> Release keys")
print("- Press 'q' to quit")
print("\nStarting in 3 seconds...")
time.sleep(3)

try:
    while True:
        success, img = cap.read()
        if not success:
            print("Error: Could not read from webcam")
            break

       
        img = cv2.flip(img, 1)

        
        hands, img = detector.findHands(img, draw=True)  

        if hands:
            hand = hands[0]
            fingers = detector.fingersUp(hand)

            
            print(f"Fingers: {fingers}") 

         
            if fingers == [1, 1, 1, 1, 1] or fingers == [0,1,1,0,0]:  
                pyautogui.keyDown('right')  
                pyautogui.keyUp('left')
                cv2.putText(img, "ACCELERATE (RIGHT)", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            elif fingers == [0, 0, 0, 0, 0] or fingers == [0,1,0,0,0]:  
                pyautogui.keyDown('left')  
                pyautogui.keyUp('right')
                cv2.putText(img, "BRAKE (LEFT)", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            else:
                pyautogui.keyUp('right')
                pyautogui.keyUp('left')
                cv2.putText(img, "NEUTRAL", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        else:
            
            pyautogui.keyUp('right')
            pyautogui.keyUp('left')
            cv2.putText(img, "NO HAND DETECTED", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (128, 128, 128), 2)

        cv2.imshow("Hill Climb Gesture Control", img)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("\nProgram interrupted by user")
except Exception as e:
    print(f"An error occurred: {e}")
finally:

    pyautogui.keyUp('right')
    pyautogui.keyUp('left')
    cap.release()
    cv2.destroyAllWindows()
    print("Program ended. All keys released.")
