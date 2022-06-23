# Importing Libraries
from PIL import Image, ImageDraw, ImageFont
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

# Function to create default text watermarked image

def text_watermark():
    global input_filename
    # Opening Image & Creating New Text Layer
    img = Image.open(input_filename).convert("RGBA")
    txt = Image.new('RGBA', img.size, (255, 255, 255, 0))

    # Creating Text
    text = "https://github.com/giovanni-vc"
    font = ImageFont.truetype("arial.ttf", 82)

    # Creating Draw Object
    d = ImageDraw.Draw(txt)

    # Positioning Text
    width, height = img.size
    textwidth, textheight = d.textsize(text, font)
    x = width / 2 - textwidth / 2
    y = height - textheight - 300

    # Applying Text
    d.text((x, y), text, fill=(255, 255, 255, 125), font=font)

    # Combining Original Image with Text and Saving
    watermarked = Image.alpha_composite(img, txt)
    watermarked_rgb = watermarked.convert('RGB')
    savefile(watermarked_rgb)

#Function to create watermarked logo image

def watermark_with_transparency(input_image_path,
                                watermark_image_path,
                                ):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    width, height = base_image.size
    transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    transparent.paste(base_image, (0, 0))
    position = (int(width/2), int(height/2))
    transparent.paste(watermark, position, mask=watermark)
    transparent_rgb = transparent.convert('RGB')
    transparent_rgb.show()
    savefile(transparent_rgb)

# Function to show image in tkinter

def open_img():
    global input_filename
    # Select the Imagename from a folder
    # x = openfilename()

    # opens the image
    img = Image.open(input_filename)

    # resize the image and apply a high-quality down sampling filter
    img = img.resize((250, 250), Image.Resampling.LANCZOS)

    # PhotoImage class is used to add image to widgets, icons etc
    img = ImageTk.PhotoImage(img)

    # create a label,

    panel = Label(root, image=img)

    # set the image as img
    panel.image = img
    panel.grid(row=5)

# Function to open image filename

def openfilename():
    global input_filename
    # open file dialog box to select image
    # The dialogue box has a title "Open"
    input_filename = filedialog.askopenfilename(title='Select image')
    open_img()
    return input_filename

# Function to save image

def savefile(output_img):
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not filename:
        return
    output_img.save(filename)

# Function to activate the logo watermark function

def create_img_watermark():
    watermark_with_transparency(input_image_path=input_filename,
                                watermark_image_path=openfilename(),
                                )

#Create a global input image filename

global input_filename

# Create a window
root = Tk()

# Set Title as Image Loader
root.title("Simple Image Watermarking")

# Set the resolution of window
root.geometry("550x300+300+150")

# Allow Window to be resizable
root.resizable(width=True, height=True)

# Create a button and place it into the window using grid layout
btn = Button(root, text='open image', command=openfilename).grid(
    row=1, columnspan=4)

# Create a button to create a logo watermark

btn_place_watermark = Button(root, text='Logo watermark image', command=create_img_watermark).grid(
    row=3, columnspan=4)

# Create a button to create a text watermark

btn_place_text_watermark = Button(root, text='Text watermark image', command=text_watermark).grid(
    row=4, columnspan=4)

root.mainloop()
