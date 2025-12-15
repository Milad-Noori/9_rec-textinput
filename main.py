import pandas as pd
import numpy as np
import cv2
from matplotlib.font_manager import font_scalings

img = cv2.imread("images/exersize.jpg")
img = cv2.resize(img, (800, 800))
pt1=(40,18)
pt2=(240,220)
color = (0,255,0)
thickness = 1
text = "cow"
font = cv2.FONT_HERSHEY_DUPLEX
cv2.rectangle(img,pt1,pt2,color,thickness)
cv2.putText(img,text,(40,18),font,1,color=(0,255,0),thickness=1)

pt3=(280,18)
pt4=(480,220)
color1 = (255,0,0)
thickness1 = 1
text1 = "sheep"
font1 = cv2.FONT_HERSHEY_DUPLEX
cv2.rectangle(img,pt3,pt4,color1,thickness1)
cv2.putText(img,text1,(280,18),font1,1,color=(255,0,0),thickness=1)


pt5=(530,18)
pt6=(750,220)
color2 = (50,100,15)
thickness2 = 1
text2 = "Frog"
font2 = cv2.FONT_HERSHEY_DUPLEX
font_scale = 0.2
cv2.rectangle(img,pt5,pt6,color2,thickness2)
cv2.putText(img,text2,(530,18),font2,1,color=(255,180,130),thickness=1)




pt7=(40,500)
pt8=(240,300)
color3= (240,20,15)
thickness3 = 1
text3= "cat"
font3 = cv2.FONT_HERSHEY_DUPLEX
cv2.rectangle(img,pt7,pt8,color3,thickness3)
cv2.putText(img,text3,(40,300),font3,1,color=(125,125,125),thickness=1)




pt9=(280,500)
pt10=(485,300)
color4= (100,200,150)
thickness4 = 1
text4= "Dog"
font4 = cv2.FONT_HERSHEY_DUPLEX
cv2.rectangle(img,pt9,pt10,color4,thickness4)
cv2.putText(img,text4,(280,300),font4,1,color=(180,100,180),thickness=1)



pt11=(530,500)
pt12=(750,300)
color5 = (50,100,15)
thickness5 = 1
text5 = "Roster"
font5 = cv2.FONT_HERSHEY_DUPLEX
cv2.rectangle(img,pt11,pt12,color5,thickness5)
cv2.putText(img,text5,(530,300),font5,1,color=(255,180,130),thickness=1)



pt13=(40,580)
pt14=(240,790)
color6= (217,190,150)
thickness6 = 1
text6= "chikhen"
font6 = cv2.FONT_HERSHEY_DUPLEX
cv2.rectangle(img,pt13,pt14,color6,thickness6)
cv2.putText(img,text6,(40,580),font6,1,color=(130,100,120),thickness=1)





cv2.imshow("exersize.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
