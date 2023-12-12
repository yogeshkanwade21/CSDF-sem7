# import the captcha package
# pip install captcha
from captcha.image import ImageCaptcha

# Store it in 'image' and define image dimensions
image = ImageCaptcha(width = 280, height = 90)

# Input CAPTCHA text to be generated
captcha_text = input("Enter CAPTCHA text to be generated")

# Generate CAPTCHA image of given text
data = image.generate(captcha_text)

# Write the image on a file and save it
image.write(captcha_text, 'CAPTCHA.png')

# Verification text
X = input("Enter text from image captcha below:\n")

# Check if both text match
if X == captcha_text:
    print("Verified")
else:
    print("Verification Failed")