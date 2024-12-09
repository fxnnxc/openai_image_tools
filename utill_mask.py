from PIL import Image, ImageDraw

def create_mask(width, height):
    # Create a new image with a black background (fully opaque)
    mask = Image.new("RGBA", (width, height), (0, 0, 0, 255))
    
    # Draw a white rectangle in the center of the image
    draw = ImageDraw.Draw(mask)
    rect_start = (width // 4, height // 4)
    rect_end = (3 * width // 4, 3 * height // 4)
    draw.rectangle([rect_start, rect_end], fill=(255, 255, 255, 255))  # White rectangle
    
    # Save the mask
    mask.save("mask.png")

# Create a 1024x1024 mask
create_mask(1024, 1024)