import PIL
from PIL import Image

# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(file_path):

    #hints: look through the pillow documentation
    img = Image.open(file_path)

    return img

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(img):
    img.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(img, file_name):
    #HINT: look at the pillow documentation! See Image.save
    img.save(file_name, "PNG")

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
# def obamicon():
