from PIL import Image
from tkinter.filedialog import askopenfilename
from AppKit import NSScreen
from Quartz import CGDisplayScreenSize

for screen in NSScreen.screens():
    description = screen.deviceDescription()
    print(CGDisplayScreenSize(description["NSScreenNumber"]))

filename = askopenfilename()
print(filename)
if filename is '':
    print("Filename cannot be empty")
    exit()

imLeft = Image.open(filename)
imMiddle = imLeft
imRight = imLeft
width, height = imLeft.size
widthByThree = int(width / 3)

imLeft.crop((0, 0, widthByThree - 1, height)).show()
imMiddle.crop((widthByThree, 0, widthByThree * 2 - 1, height)).show()
imRight.crop((widthByThree * 2, 0, widthByThree * 3 - 1, height)).show()
