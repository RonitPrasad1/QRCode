Simple and fun QR code project done in Python that essentially allows you to store whatever you desire in the URL link and then generates a QR code as a png in the specified pathing, shown here:
      
    generatedImage.save(r'C:\Users\ronit\PycharmProjects\QRCodeProject\secure_QRCode.png')

Saves the QR code called "secure_QRCode" in the directory where you created your QR code project to begin with. In my case, I have my Resume stored in the QR code, so as soon as you scan it, it'll open up a Google Drive with my 1-page Software Engineering Resume.

The code has error handling built-in using a try-catch block as well as a debugger portion that can check if the image is being saved to begin with.
