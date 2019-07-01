# This is importing the functions we made in the filters.py file!
import filters


def main():

    # how to represent a file name?
    # need the image path
    # https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/file---image-file-path
    # example: /Users/brookeryan/Downloads/giphy-4.gif
    img = filters.load_img("/Users/brookeryan/giphy-2.gif")
    filters.show_img(img)
    filters.save_img(img, "cool")

# Don't forget to call your main function!
main()
