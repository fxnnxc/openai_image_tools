from openai import OpenAI
import requests
import datetime 
from PIL import Image  # Add this import
import os 

# Initialize the OpenAI client
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)
def convert_mask_to_binary(mask_path):
    with Image.open(mask_path) as mask:
        # Convert to grayscale
        mask = mask.convert("L")
        # Convert to binary (black and white)
        binary_mask = mask.point(lambda p: 255 if p > 128 else 0)
        return binary_mask

def edit_and_save_image(image_path, mask_path, prompt, filename, n=1):
    # Determine the size of the input image
    with Image.open(image_path) as img:
        size = (img.width, img.height)

    # Convert and resize the mask to match the input image size
    binary_mask = convert_mask_to_binary(mask_path)
    binary_mask = binary_mask.resize(size)

    # Save the resized binary mask temporarily
    os.makedirs("temp", exist_ok=True)
    resized_mask_path = 'temp/resized_binary_mask.png'
    binary_mask.save(resized_mask_path)

    # Make a request to the DALL-E API for editing
    print("Editing image...")
    response = client.images.edit(
        image=open(image_path, "rb"),
        mask=open(resized_mask_path, "rb"),
        prompt=prompt,
        n=n,
        size=f"{size[0]}x{size[1]}"
    )

    # Iterate over each edited image variation
    for index, image_data in enumerate(response.data):
        # Get the URL of the edited image
        image_url = image_data.url
        print(image_url)

        # Download the image and save it in the same directory
        image_content = requests.get(image_url).content
        edited_filename = f"{filename.split('.')[0]}_edit_{index}.png"
        with open(edited_filename, 'wb') as image_file:
            image_file.write(image_content)

# Example usage
import os 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--n", type=int, default=1)
parser.add_argument("--model", type=str, default="dall-e-2")
parser.add_argument("--image-path", type=str, default="generated_images/cute_dog.png")
parser.add_argument("--mask-path", type=str, default="mask.png")
parser.add_argument("--prompt", type=str, default="A cute baby sea otter wearing a beret")
args = parser.parse_args()


save_dir="edited_images"
os.makedirs(save_dir, exist_ok=True)

prompt = args.prompt
image_path = args.image_path
mask_path = args.mask_path
n=args.n

fetched_name = image_path.split("/")[-1].split(".")[0]
save_path = f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}_edited_{fetched_name}.png"
save_path = os.path.join(save_dir, save_path)
edit_and_save_image(image_path, mask_path, prompt, save_path, n)