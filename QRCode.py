# Import the QRCode Library:
import qrcode


# Create the QRCode with the chosen data inside of it:
def qr_code_generator() -> None:
	myQRCode = qrcode.QRCode(
		version=1,
		error_correction=qrcode.constants.ERROR_CORRECT_L,
		box_size=30,
		border=1,
	)

	# Storing the HTTPS URL inside of a string:
	contentsOfQRCode = "https://drive.google.com/file/d/1fxyvc8HvMwpxci_orip8clTa1AC4E0d9/view?usp=sharing"

	# Adding the data with error handling:
	try:
		myQRCode.add_data(contentsOfQRCode)
		myQRCode.make(fit=True)

		# Generating/creating the image:
		generatedImage = myQRCode.make_image(fill_color="black", back_color="white")

		# Saving the image as a "PNG" to whatever path you specify, shown below:
		generatedImage.save(r'C:\Users\ronit\PycharmProjects\QRCodeProject\secure_QRCode.png')
		print("Your QR Code has been generated!")
	except Exception as error:
		print("An error occurred while generating the QR code!")
		print(error)

    # DEBUGGER: Check if the image was saved successfully:
    '''
    try:
        with open('qr_code.png', 'rb'):
            print("DEBUGGER: Works!")
    except FileNotFoundError:
        print("DEBUGGER: Does not work!")
    '''


# Functional-based calling:
if __name__ == "__main__":
	qr_code_generator()
