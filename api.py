import base64
import datetime
import os
import re
import sys

from openai import OpenAI

def clean_for_ascii(text):
    # Replace common problematic characters
    replacements = {
        # Smart quotes to regular quotes
        '"': '"',
        ''': "'",  # Smart apostrophes to regular apostrophes  
        ''': "'",
        '—': '-',  # Em dash to hyphen
        '–': '-',  # En dash to hyphen
        '…': '...',  # Ellipsis to three dots
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    # Remove any remaining non-ASCII characters
    text = re.sub(r'[^\x00-\x7F]+', '', text)

    return text

def main():

    # Initialize the OpenAI client and prepare the prompt
    client = OpenAI()

    # Get the current date
    current_date = datetime.date.today()

    try:
        # Generate a highly specific and creative prompt for a panda actively participating in today's events
        system_prompt = """You are a creative prompt engineer specializing in unique, visually striking image descriptions. 
        Create prompts that are specific, unexpected, and memorable. Focus on unusual angles, interesting details, 
        and creative interpretations that an AI image generator can render beautifully. Ensure all generated text is 
        ASCII-only, fits within a 120-token limit, and ends with complete sentences and proper punctuation."""

        text_prompt = f"""Create a detailed, creative image prompt featuring a panda as the main character actively participating in or celebrating a real global cultural, historical, or seasonal event happening on {current_date}. 
        
        Requirements:
        - The panda should be DOING something related to the event, not just observing
        - Include specific visual details (clothing, props, setting, lighting, mood)
        - Make it whimsical but respectful to the cultural significance
        - Add unique artistic elements that make the image memorable
        - Specify art style or photographic technique for visual impact
        - Keep it family-friendly and culturally sensitive
        
        TOKEN LIMIT AWARENESS:
        - Plan the response to fit within 100 tokens
        - Prioritize complete sentences over quantity
        - Use only ASCII-safe characters
        - Allowed punctuation: ., !, ?, :, -, ' (apostrophe), " (quotation marks)
        - Forbidden punctuation: non-ASCII symbols, emojis, or excessive special characters
        
        Format: Start with "A [art style] image of..." and make it vivid and specific."""

        # Use the chat completions endpoint with a current model
        text_response = client.chat.completions.create(
            model="gpt-4.1-nano",  # Using GPT-4.1 Nano as it is cheaper, which is necessary given the complexity of our prompt
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text_prompt}
            ],
            max_tokens=100,  # Increased token limit leads to more detailed prompts, but is more expensive
            temperature=0.8,  # Higher creativity
            presence_penalty=0.6,  # Encourage more unique/original content
            frequency_penalty=0.4   # Reduce repetitive phrases
        )

        # Extract the generated text from the response
        generated_text = text_response.choices[0].message.content

        # Clean the generated text to ensure it is ASCII-compatible and use it as the prompt
        prompt = clean_for_ascii(generated_text.strip())

        print(f"Generated prompt: {prompt}")

        # Generate an image using the OpenAI API with the specified prompt
        img = client.images.generate(
            model="dall-e-3",  # Specify the model to use for image generation
            prompt=prompt,  # Use the generated prompt retrieved from the text model
            size="1024x1024",  # Specify the size of the generated image
            response_format="b64_json"  # Request base64 format
        )

        # Check if the response contains the expected data
        if not img or not img.data or not img.data[0].b64_json:
            raise ValueError("No image data returned from the API.")

        # Extract the base64-encoded image data from the API response
        image_base64 = img.data[0].b64_json
        image_bytes = base64.b64decode(image_base64)  # Decode the base64 data into image bytes

        print("Image generation successful. Saving the image...")

        # Ensure the 'images' directory exists before saving the generated image
        os.makedirs("images", exist_ok=True)

        print("Directory 'images' exists or created successfully.")

        # Save the image with a timestamped filename for archival purposes
        with open(f"images/panda_{current_date}.png", "wb") as f:
            f.write(image_bytes)

        # Save the image with a fixed filename for easy reference
        with open("images/panda_current.png", "wb") as f:
            f.write(image_bytes)

        print(f"Image 'panda_{current_date}' saved successfully.")
        print(f"Image 'panda_current' saved successfully.")

        # Ensure the 'prompts' directory exists before saving the generated prompt
        os.makedirs("prompts", exist_ok=True)

        print("Directory 'prompts' exists or created successfully.")

        # Save the prompt with a timestamped filename for archival purposes
        with open(f"prompts/prompt_{current_date}.txt", "w") as f:
            f.write(prompt)

        # Save the prompt with a fixed filename for easy reference
        with open("prompts/prompt_current.txt", "w") as f:
            f.write(prompt)

        print(f"Prompt 'prompt_{current_date}' saved successfully.")
        print(f"Prompt 'prompt_current' saved successfully.")

        # Update the README file with the prompt text
        with open("README.md", "r") as readme_file:
            readme_content = readme_file.readlines()

        updated_readme_content = []
        for line in readme_content:
            if line.strip() == "![screenshot](images/panda_current.png)":
                updated_readme_content.append(line)
                updated_readme_content.append(f"\n**Prompt:** {prompt}\n")
                break  # Stop processing after replacing the prompt
            else:
                updated_readme_content.append(line)

        with open("README.md", "w") as readme_file:
            readme_file.writelines(updated_readme_content)

        print("README updated successfully.")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)



if __name__ == '__main__':
    main()

