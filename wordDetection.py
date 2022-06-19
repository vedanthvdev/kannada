import cv2
import pytesseract as pyt


def imagToCharecter(img, hImg):
    boxes = pyt.image_to_boxes(img, config="-l kan")
    for b in boxes.splitlines():
        print(b)
        b = b.split(' ')
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x,hImg-y), (w,hImg-h), (0,0,255), 3)  

def imageToWords(img):
    data = pyt.image_to_data(img, config="-l kan")
    for x,b in enumerate(data.splitlines()):
        if x != 0:
            b = b.split()
            if len(b)==12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x,y), (w+x,h+y), (0,0,255), 3)
                print(b[11])


image = 'meenu.png'
img = cv2.imread(image)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
hImg, wImg,_ = img.shape
imageToWords(img)
