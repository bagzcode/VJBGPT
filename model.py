import sys
import gradio as gr
from langchain.chat_models import ChatOpenAI
from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, ServiceContext, PromptHelper
import os
from dotenv import load_dotenv, find_dotenv

os.environ["OPENAI_API_KEY"] = [PUT_YOUR_OPENAI_KEY_HERE]
# load_dotenv(find_dotenv())
# OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


def init_index(directory_path):
    # model params
    # max_input_size: maximum size of input text for the model.
    # num_outputs: number of output tokens to generate.
    # max_chunk_overlap: maximum overlap allowed between text chunks.
    # chunk_size_limit: limit on the size of each text chunk.
    max_input_size = 200
    num_outputs = 100
    max_chunk_overlap = 20
    chunk_size_limit = 600

    # llm predictor with langchain ChatOpenAI
    # ChatOpenAI model is a part of the LangChain library and is used to interact with the GPT-3.5-turbo model provided by OpenAI
    prompt_helper = PromptHelper(
        max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
    llm_predictor = LLMPredictor(llm=ChatOpenAI(
        temperature=0.7, model_name="gpt-3.5-turbo", max_tokens=num_outputs))

    # read documents from docs folder
    documents = SimpleDirectoryReader(directory_path).load_data()

    # init index with documents data
    # This index is created using the LlamaIndex library. It processes the document content and constructs the index to facilitate efficient querying
    service_context = ServiceContext.from_defaults(
        llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    index = GPTSimpleVectorIndex.from_documents(
        documents, service_context=service_context)

    # save the created index
    index.save_to_disk('index.json')

    return index


def chatbot(input_text):
    # load index
    index = GPTSimpleVectorIndex.load_from_disk('index.json')

    # get response for the question
    response = index.query(input_text, response_mode="compact")

    return response.response


# create index
init_index("docs")

# create ui interface to interact with gpt-3 model
iface = gr.Interface(fn=chatbot,
                     inputs=gr.components.Textbox(
                         lines=7, placeholder="Masukan Pertanyaan Anda disini"),
                     outputs="text",
                     title="Batik-ChatBot: Batik Expert Powered-by ChatGPT",
                     description="Tanya Pertanyaan Tentang Batik Lasem Desain Disini",
                     allow_screenshot=True)
iface.launch(share=True)
