from openai import OpenAI
import requests
import datetime 
import os 
# Initialize the OpenAI client with a specific version if needed
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)
def generate_and_save_image(prompt, filename, model, num_samples, size="1024x1024"):
    # Make a request to the DALL-E 2 API
    print("Generating image...")
    response = client.images.generate(
        prompt=prompt,
        n=num_samples,
        size=size,
        model=model
    )

    # Iterate over each generated image variation
    for index, image_data in enumerate(response.data):
        # Get the URL of the generated image
        image_url = image_data.url
        print(image_url)

        # Download the image and save it in the same directory
        image_content = requests.get(image_url).content
        generation_filename = f"{filename.split('.')[0]}_generation_{index}.png"
        with open(generation_filename, 'wb') as image_file:
            image_file.write(image_content)


import os 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--n", type=int, default=1)
parser.add_argument("--model", type=str, default="dall-e-2")
parser.add_argument("--size", type=str, default="1024x1024")
parser.add_argument("--prompt", type=str, default="A cute dog")
args = parser.parse_args()


# Example usage
save_dir="generated_images"
os.makedirs(save_dir, exist_ok=True)

num_samples=args.n
size=args.size
models = [args.model]

for model in models:
    prompt = args.prompt
    save_path = f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}_{model}_{prompt.replace(' ', '_')}.png"
    save_path = os.path.join(save_dir, save_path)
    generate_and_save_image(prompt, save_path, model, num_samples, size)