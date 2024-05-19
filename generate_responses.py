import openai
import yaml
import os
import logging
from dotenv import load_dotenv
from tqdm import tqdm

# Load environment variables
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']
    except Exception as e:
        logging.error(f"Error generating response for prompt: {prompt} - {e}")
        return None

def save_to_file(output_folder, title, filename, content):
    os.makedirs(output_folder, exist_ok=True)
    file_path = os.path.join(output_folder, filename)
    with open(file_path, 'w') as file:
        file.write(f"# {title}\n\n{content}")
    logging.info(f"Saved response to {file_path}")

def main():
    config = load_yaml('config.yaml')
    output_folder = config['output_folder']
    context = config['context']
    objects = config['objects']

    for obj in tqdm(objects, desc="Processing prompts"):
        prompt = f"{context}\n\n{obj['prompt']}"
        title = obj['title']
        filename = obj['filename']
        
        response = generate_response(prompt)
        if response:
            save_to_file(output_folder, title, filename, response)

if __name__ == "__main__":
    main()
