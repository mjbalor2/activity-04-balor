import cv2
filepath ="justine.jpg"
image = cv2.imread(filepath,1)
cv2.imshow("baby",image)
cv2.waitKey(0)
cv2.destroyAllWindows()