# OpenAI Image Tools

1. Get OpenAI API key from [here](https://platform.openai.com/api-keys)
2. Install dependencies

```bash
pip install openai
```

## Generate Images

```bash 
export OPENAI_API_KEY=YOUR_API_KEY
python generate.py  --n 1 --model dall-e-2 --size 1024x1024 --prompt "An impressionist-style landscape painting reminiscent of Monet or Manet. The scene showcases a peaceful countryside with a meandering river surrounded by vibrant greenery and blooming flowers."
```

<img src="generated_images/example.png" alt="Variation 0" width="256">

## Create Variations

```bash 
export OPENAI_API_KEY=YOUR_API_KEY
python variation.py --n 1 --model dall-e-2 --image-path generated_images/example.png --size 1024x1024
```

<img src="variation_images/example.png" alt="Variation 0" width="256">

## Edit Images

```bash 
export OPENAI_API_KEY=YOUR_API_KEY
python edit.py --prompt "A dark and moody landscape painting reminiscent of Monet or Manet. The scene showcases a stormy countryside with a meandering river surrounded by vibrant greenery and blooming flowers." --n 1 --model dall-e-2 --image-path generated_images/example.png  --mask-path masks/example.png
```

<table>
  <tr>
    <td><img src="generated_images/example.png" alt="Generated Image" width="256"></td>
    <td><img src="masks/example.png" alt="Mask Image" width="256"></td>
    <td><img src="edited_images/example.png" alt="Edited Image" width="256"></td>
  </tr>
  <tr>
    <td>Generated Image</td>
    <td>Mask Image</td>
    <td>Edited Image</td>
  </tr>
</table>
