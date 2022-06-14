# Importing all important library

import cv2
import pandas as pd

# Reading the txt file Present in the current director
# And converting into a DataFrame
# Since our txt has no header , so Header = None

index = ['names_', 'names', 'hex_code', 'R', 'G', 'B']
df = pd.read_csv('clo.txt', delimiter=',', header=None, names=index)

# To print the DataFrame use the below Commend by removing the Hashtag
# print(df)

# Now reading the image file present in the same director
# To Change the image for the project , please place the file in the same director as the program file
# And replace the file name and the associated file type

imge = cv2.imread('bright_river.jpg')
imge = cv2.resize(imge, (640, 640))


# This function is used to Get the colour Name from the Txt / DataFrame that we got Using Pandas
# The Params are :- R value of the image , G value of the image , B value of the image
# The Return type is a String that is the name of the colour
def getColorName(R, G, B):
    minimum = 10000
    cname = 0
    for i in range(len(df)):
        d = abs(R - int(df["R"][i])) + abs(G - int(df["G"][i])) + abs(B - int(df["B"][i]))
        if d <= minimum:
            minimum = d
            cname = df["names"][i]
    return cname


def Mouse_event(event, x, y, flag, params):
    if event == cv2.EVENT_MOUSEMOVE:
        print('Position :- ', x, y)
        b, g, r = imge[y][x]
        print('BGR_value :- ', b, g, r)
        b = int(b)
        g = int(g)
        r = int(r)
        cv2.rectangle(imge, (20, 20), (620, 60), (b, g, r), -1)

        text = getColorName(r, g, b) + '->' + " R: " + str(r) + " G: " + str(g) + " B: " + str(b)
        print(text)

        cv2.putText(imge, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)

        if int(r) + int(g) + int(b) >= 550:
            cv2.putText(imge, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow('img', imge)


# Now We show the image for the first time we use the below codes
cv2.imshow('img', imge)
cv2.setWindowTitle('img', 'Colour Detection using Pandas & OpenCV - by Srivatsa Cool')
# For setting our mouse Events we use cv2.setMouseCallback
cv2.setMouseCallback("img", Mouse_event)
# For the Waiting time we use cv2.WaitKey
# it can have any particular values which denotes milliseconds
cv2.waitKey()
cv2.destroyAllWindows()
