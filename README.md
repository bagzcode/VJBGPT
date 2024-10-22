# Batik-ChatBot Repository

This repository contains a chatbot application that uses OpenAI's GPT-3.5-turbo model to answer questions related to Batik Lasem designs. The chatbot is powered by the LangChain and LlamaIndex libraries and provides a web-based interface using Gradio.

## Features

- **ChatGPT-3.5 Integration:** The chatbot uses the GPT-3.5-turbo model to process user queries.
- **Document Indexing:** The application reads and processes documents from the `docs/` folder to create a vector-based index using LlamaIndex.
- **Web Interface:** A user-friendly web interface is provided via Gradio for easy interaction.
- **Customizable:** The chatbot can be modified to answer questions based on any document set by replacing the content in the `docs/` folder.

## Files

- **model.py:** The core script that initializes the document index and chatbot interface.
- **requirements.txt:** Lists the Python dependencies required to run the project.

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/bagzcode/VJBGPT.git](https://github.com/bagzcode/VJBGPT.git)
   cd batik-chatbot
2. **Install Dependencies:** Install the required Python packages by running:
   ```bash
   pip install -r requirements.txt
3. **Set Up OpenAI API Key:**
   - Replace [PUT_YOUR_OPENAI_KEY_HERE] in model.py with your OpenAI API key.
   - Alternatively, you can use a .env file. Uncomment the .env related lines in the script and add the following to a .env file:
   ```bash
   OPENAI_API_KEY=your-api-key-here
4. **Run the Application:** Start the chatbot by running the model.py script:
   ```bash
   python model.py

This will launch a web interface where you can ask questions about Batik Lasem designs.

## License
This project is licensed under the MIT License.

### Key Additions:
- Included a section on setting up a virtual environment using both `venv` and `conda`.
- Provided commands to create and activate the virtual environment before installing dependencies.

This should help users set up the project environment correctly!
