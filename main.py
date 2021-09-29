import cv2
import pyautogui
import mediapipe as mp

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

green = (0, 255, 0)
white = (255, 255, 255)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    multiLandMarks = results.multi_hand_landmarks

    cv2.line(img, (640, 0), (640, 720), white, 10)
    cv2.rectangle(img, (600,260), (680,460), green, cv2.FILLED)

    if multiLandMarks:
        handPoints = []
        for handLms in multiLandMarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            for idx, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                handPoints.append((cx,cy))


            if handPoints[8][1] < 260:
                print("UP")
                pyautogui.keyDown("space")
                pyautogui.keyUp("space")
            elif handPoints[8][1] > 460:
                print("Down")
                pyautogui.keyDown("down")
                pyautogui.keyUp("down")
            else:
                print("CENTER")





    cv2.imshow("Dino Game", img)
    cv2.waitKey(1)
