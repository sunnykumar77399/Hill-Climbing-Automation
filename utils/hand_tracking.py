import cv2
from cvzone.HandTrackingModule import HandDetector
from utils.config import DETECTION_CONFIDENCE, MAX_HANDS

class HandTracker:
    def __init__(self):
        self.detector = HandDetector(detectionCon=DETECTION_CONFIDENCE, maxHands=MAX_HANDS)

    def process(self, frame):
        hands, frame = self.detector.findHands(frame)  # Draw landmarks
        return hands, frame

    def fingers_up(self, hand):
        return self.detector.fingersUp(hand)
