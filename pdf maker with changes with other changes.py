import cv2
from fpdf import FPDF
import os
url = "http://192.168.11.198:8080/video"
cap=cv2.VideoCapture(url)
ret = True
f1=0
i=1


while ret:
    ret, frame = cap.read()
    if f1 == 0:
        print("press 's' to scan the document ")
        print("press 'q' to quit ")
        f1 = f1 + 1



    cv2.imshow("camera feed", frame)
    k1 = cv2.waitKey(1)

    if k1 == ord('s'):
        cv2.destroyWindow("camera feed")
        cv2.imshow("scanned photo", frame)
        print("press u if its unreadable")
        print("press b to convert it to black and white form")
        k2 = cv2.waitKey(0)
        if k2 == ord('u'):
            cv2.destroyWindow('scanned photo')
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            new = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155, 1)
            cv2.imshow("result", new)
            k3 = cv2.waitKey(0)
            print("If you are satisfied with the photo press 'd' ,else press any other key ")
            if k3 == ord('d'):
                cv2.imwrite("E://pdf//scanned%d.jpg" % i, new)
                i = int(str(i) + str(1))

                print("press 's' to scan more document")
                print("press 'q' to quit")

            else:

                print("press 's' to scan more document")
                print("press 'q' to quit")

            continue

        elif k2 == ord('b'):
            cv2.destroyWindow('scanned photo')
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow("result", gray)
            k3 = cv2.waitKey(0)
            print("If you are satisfied with the photo press 'd' ,else press any other key ")
            if k3 == ord('d'):
                cv2.imwrite("E://pdf//scanned%d.jpg" % i, gray)
                i = int(str(i) + str(1))
                print("press 's' to scan more document")
                print("press 'q' to quit")

            else:

                print("press 's' to scan more document")
                print("press 'q' to quit")

            continue

    elif k1 == ord('q'):
        ret = False
        break



cv2.destroyAllWindows()
imagelist=os.listdir("E://pdf")
pdf = FPDF()
for image in imagelist:
    image ="E://pdf//"+image

    pdf.add_page()
    pdf.image(image)

    if len(image) >= len("E://pdf//scanned"+str(i)+".jp") :
        break


name_of_file=input("By what name do you want to save the PDF")
pdf.output("E://"+name_of_file+".pdf", "F")