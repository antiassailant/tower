from PIL import Image, ImageDraw, ImageFont

def get_text_dimensions(text_string, font):
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width, text_height)

def text_to_image(input_text, font_path, output_path):
    # Set the image dimensions and background mode
    width, height = 6000, 500  # You can adjust these values based on your needs
    background_color = (255, 255, 255, 0)  # RGBA format with 0 alpha for transparent background

    # Create a new image with a transparent background
    image = Image.new("RGBA", (width, height), background_color)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Load the font
    try:
        font = ImageFont.truetype(font_path, size=24)  # Adjust the font size as needed
    except IOError:
        return

    # Calculate text position to center it in the image
    text_width, text_height = get_text_dimensions(input_text, font)
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # Draw text on the image
    draw.text((x, y), input_text, font=font, fill=(255, 255, 255, 255))  # Use RGBA format for text color

    # Save the image
    image.save(output_path, "PNG")  # You can change the format if needed

def crop_outer_transparent(image):
    # Convert the image to RGBA if it's not already
    image = image.convert("RGBA")

    # Get the bounding box of the non-transparent region
    bbox = image.getbbox()

    # Crop the image using the bounding box
    cropped_image = image.crop(bbox)

    return cropped_image

def generate(textinput):
    user_input = textinput
    font_file_path = "eva.ttf"  # Replace with the path to your font file
    output_image_path = "output_image.png"  # You can change the output filename and format
    text_to_image(user_input, font_file_path, output_image_path)
    input_image_path = "output_image.png"
    image = Image.open(input_image_path)
    cropped_image = crop_outer_transparent(image)
    output_image_path = "final.png"
    cropped_image.save(output_image_path)