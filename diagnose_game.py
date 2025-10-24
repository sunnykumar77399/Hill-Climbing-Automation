# #!/usr/bin/env python3
# """
# Diagnostic script to test game compatibility
# """

# import pyautogui
# import time
# import sys

# def test_key_press():
#     """Test key press with different methods"""
#     print("Testing different key press methods...")
    
#     # Method 1: pyautogui.press
#     print("Method 1: pyautogui.press('right')")
#     pyautogui.press('right')
#     time.sleep(0.5)
    
#     # Method 2: pyautogui.keyDown/keyUp
#     print("Method 2: keyDown/keyUp")
#     pyautogui.keyDown('right')
#     time.sleep(0.1)
#     pyautogui.keyUp('right')
#     time.sleep(0.5)
    
#     # Method 3: pyautogui.hotkey
#     print("Method 3: pyautogui.hotkey")
#     pyautogui.hotkey('right')
#     time.sleep(0.5)
    
#     print("Test completed!")

# def check_active_window():
#     """Check which window is currently active"""
#     try:
#         import pygetwindow as gw
#         active_window = gw.getActiveWindow()
#         if active_window:
#             print(f"Active window: {active_window.title}")
#             return active_window.title
#         else:
#             print("No active window detected")
#             return None
#     except ImportError:
#         print("pygetwindow not available for window detection")
#         return None

# def main():
#     print("Game Compatibility Diagnostic Tool")
#     print("=" * 40)
    
#     print("\n1. Make sure Hill Climb Racing is open and active")
#     print("2. Click on the game window to make it the active window")
#     print("3. This script will test different key press methods")
    
#     input("\nPress Enter when ready...")
    
   
#     active_window = check_active_window()
    
#     print(f"\nTesting with active window: {active_window}")
#     print("Watch the game for any movement...")
    
  
#     for i in range(3, 0, -1):
#         print(f"Starting test in {i}...")
#         time.sleep(1)
    

#     test_key_press()
    
#     print("\nDiagnostic completed!")
#     print("If the car didn't move, try these solutions:")
#     print("1. Make sure the game window is truly active (click on it)")
#     print("2. Try running the gesture control as administrator")
#     print("3. Check if the game has different key bindings")
#     print("4. Try a different Hill Climb Racing version")

# if __name__ == "__main__":
#     main()
