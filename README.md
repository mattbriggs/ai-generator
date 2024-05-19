 AI Response Generator

This script generates AI responses from prompts specified in a YAML configuration file using OpenAI's GPT-4 model. The responses are saved as standalone Markdown files.

## Requirements

- Python 3.7+
- Virtual environment (recommended)

## requirements.txt

```text
openai
pyyaml
python-dotenv
tqdm

```

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory of the project and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

5. Create a `config.yaml` file in the root directory of the project with the following structure:
   ```yaml
   output_folder: "output"
   context: "Your context here"
   objects:
     - prompt: "Your AI prompt here"
       title: "Title for the prompt"
       filename: "filename.md"
     - prompt: "Another AI prompt here"
       title: "Another title"
       filename: "another_filename.md"
   ```

## Usage

Run the script:
```bash
python generate_responses.py
```

The script will process each prompt specified in the `config.yaml` file and save the responses as Markdown files in the specified output folder. Progress will be displayed in the command line, and logs will be written to `app.log`.

## Error Handling

If an error occurs while generating a response for a prompt, it will be logged in `app.log`, and the script will continue processing the remaining prompts.
```

### Example `config.yaml`

```yaml
output_folder: "output"
context: "Your context here"
objects:
  - prompt: "Your AI prompt here"
    title: "Title for the prompt"
    filename: "filename.md"
  - prompt: "Another AI prompt here"
    title: "Another title"
    filename: "another_filename.md"
```

This setup will guide you through the installation and usage of the script, ensuring it meets your specifications.