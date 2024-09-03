import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    
    if hands:
        hand = hands[0]
        landmarks = hand['lmList']  # Get the landmarks for the detected hand
        
        for lm in landmarks:
            x = lm[0]  # x-coordinate of the landmark
            y = lm[1]  # y-coordinate of the landmark
            cv2.circle(img, (x, y), 8, (255, 0, 0), cv2.FILLED)  # Draw a circle at each landmark point
            #print(f"Landmark Point - X: {x}, Y: {y}")
        x, y, w, h = hand['bbox']
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
