# https://platform.openai.com/docs/api-reference/images/createVariation
from openai import OpenAI
import requests
import datetime 
import argparse
import os 

# Initialize the OpenAI client
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_and_save_image(image_path, filename, model, n=1, size="1024x1024"):
    # Create a variation of an existing image
    print("Creating image variation...")
    response = client.images.create_variation(
        image=open(image_path, "rb"),
        n=n,
        size=size,
        model=model,
    )

    # Iterate over each generated image variation
    for index, image_data in enumerate(response.data):
        # Get the URL of the generated image
        image_url = image_data.url
        print(image_url)

        # Download the image and save it in the same directory
        image_content = requests.get(image_url).content
        variation_filename = f"{filename.split('.')[0]}_variation_{index}.png"
        with open(variation_filename, 'wb') as image_file:
            image_file.write(image_content)

# Example usage
save_dir = "variation_images"
os.makedirs(save_dir, exist_ok=True)

parser = argparse.ArgumentParser()
parser.add_argument("--n", type=int, default=1)
parser.add_argument("--model", type=str, default="dall-e-2")
parser.add_argument("--image-path", type=str, default="generated_images/cute_dog.png")
parser.add_argument("--size", type=str, default="1024x1024")
args = parser.parse_args()

n = args.n
model = args.model
image_path = args.image_path
size = args.size

models = [ args.model]   # "dall-e-3" not available for variations 
for model in models:
    fetched_name = image_path.split("/")[-1].split(".")[0]
    save_path = f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}_{model}_{fetched_name}.png"
    save_path = os.path.join(save_dir, save_path)
    generate_and_save_image(image_path, save_path, model, n=n, size=size)