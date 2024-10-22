import sys
import gradio as gr
from langchain.chat_models import ChatOpenAI
from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, ServiceContext, PromptHelper
import os
from dotenv import load_dotenv, find_dotenv

# Load environment variable for OpenAI API Key
os.environ["OPENAI_API_KEY"] = "[PUT_YOUR_OPENAI_KEY_HERE]"
# load_dotenv(find_dotenv())
# OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def initialize_index(directory_path):
    max_input_size = 200
    num_output_tokens = 100
    max_chunk_overlap = 20
    chunk_size_limit = 600

    prompt_helper = PromptHelper(
        max_input_size, num_output_tokens, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
    
    llm_predictor = LLMPredictor(llm=ChatOpenAI(
        temperature=0.7, model_name="gpt-3.5-turbo", max_tokens=num_output_tokens))

    # Read documents from the specified directory
    documents = SimpleDirectoryReader(directory_path).load_data()
    
    # Initialize index with the documents' data
    service_context = ServiceContext.from_defaults(
        llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    
    document_index = GPTSimpleVectorIndex.from_documents(
        documents, service_context=service_context)

    # Save the created index to disk
    document_index.save_to_disk('index.json')
    return document_index

def respond_to_query(user_input):
    # Load the index from disk
    document_index = GPTSimpleVectorIndex.load_from_disk('index.json')
    
    # Get the response for the user's question
    response = document_index.query(user_input, response_mode="compact")
    return response.response

# Initialize the index
initialize_index("docs")

# Enhanced Gradio UI for Batik Chatbot
chatbot_interface = gr.Interface(
    fn=respond_to_query,
    inputs=gr.Textbox(
        lines=3,
        placeholder="Tanyakan tentang desain Batik Lasem Anda di sini...",
        label="Pertanyaan Anda",
        interactive=True
    ),
    outputs=gr.Textbox(
        label="Jawaban Chatbot",
        placeholder="Jawaban akan muncul di sini...",
        interactive=False
    ),
    title="Batik ChatBot: Ahli Batik Lasem",
    description="Selamat datang di Batik ChatBot! Tanya apa saja tentang desain Batik Lasem dan dapatkan jawaban dari sistem berbasis AI kami.",
    theme="compact",
    layout="vertical",
    allow_screenshot=True,
    article="<p style='text-align: center; color: #5a5a5a;'>Dapatkan pengetahuan tentang seni Batik Lasem dengan chatbot kami!</p>",
    css=".output-textbox { background-color: #f9f9f9; }"  # Light gray background for the output
)

chatbot_interface.launch(share=True)
