import cv2 as cv

cap = cv.VideoCapture(1)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("can't receive frame (stream end?), Exiting...")
        break
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # 显示结果
    cv.imshow("frame", gray)
    if cv.waitKey(1) == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()