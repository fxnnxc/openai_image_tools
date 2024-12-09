# OpenAI Image Tools


## Generate Images

```bash 
export OPENAI_API_KEY=YOUR_API_KEY
python generate.py --prompt "A cute dog" --n 1 --model dall-e-2 --size 1024x1024
```

## Create Variations

```bash 
export OPENAI_API_KEY=YOUR_API_KEY
python variation.py --n 1 --model dall-e-2 --image-path generated_images/cute_dog.png --size 1024x1024
```

## Edit Images

```bash 
export OPENAI_API_KEY=YOUR_API_KEY
python edit.py --prompt "A cute baby sea otter wearing a beret" --n 1 --model dall-e-2 --image-path generated_images/cute_dog.png
```