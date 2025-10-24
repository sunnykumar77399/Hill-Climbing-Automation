# #!/usr/bin/env python3
# """
# Setup script for Hill Climb Racing Gesture Control
# """

# import subprocess
# import sys
# import os

# def install_requirements():
#     """Install required packages"""
#     print("Installing required packages...")
#     try:
#         subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
#         print("✅ All packages installed successfully!")
#         return True
#     except subprocess.CalledProcessError as e:
#         print(f"❌ Error installing packages: {e}")
#         return False

# def check_camera():
#     """Check if camera is available"""
#     print("Checking camera availability...")
#     try:
#         import cv2
#         cap = cv2.VideoCapture(0)
#         if cap.isOpened():
#             print("✅ Camera is available!")
#             cap.release()
#             return True
#         else:
#             print("❌ Camera not found. Please check your camera connection.")
#             return False
#     except ImportError:
#         print("❌ OpenCV not installed. Please run: pip install -r requirements.txt")
#         return False

# def main():
#     print("Hill Climb Racing Gesture Control - Setup")
#     print("=" * 50)
    
#     # Install requirements
#     if not install_requirements():
#         print("Setup failed. Please check the error messages above.")
#         return
    
#     # Check camera
#     if not check_camera():
#         print("Setup completed with warnings. Camera may not work properly.")
#         return
    
#     print("\n🎉 Setup completed successfully!")
#     print("\nTo run the game:")
#     print("  python main.py")
#     print("\nControls:")
#     print("  - All fingers up (open palm) → Brake")
#     print("  - Only index finger up → Accelerate")
#     print("  - Press 'q' to quit")

# if __name__ == "__main__":
#     main()
