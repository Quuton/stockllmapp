import gradio as gr
from controllers import rag, prompt
vector_db = rag.get_vectordb()

def get_prompt_response(query:str):
    context = vector_db.similarity_search(query,k=10)
    ai_message = prompt.send_prompt(query, str(context))
    return ai_message.content

def initialize():
    with gr.Blocks() as app:
        gr.Markdown("# PSE Stock LLM App")
        gr.Markdown("> Only PSE Stocks are supported, theres a limit on the API. Also only monthly data is available, daily would be too much")

        main_chat_input = gr.Textbox(label="Start Chatting:")
        
        # Dropdown menu
        # dropdown = gr.Dropdown(
        #     label="Choose an option:",
        #     choices=["Option 1", "Option 2", "Option 3"],
        #     value="Option 1"  # Default value
        # )
        
        main_chat_submit_button = gr.Button("Send")

        # Output display
        main_output_text = gr.Textbox(label="Output", interactive=False)

        # Define the interaction
        main_chat_submit_button.click(
            fn=get_prompt_response,
            inputs=[main_chat_input],
            outputs=main_output_text
        )

    return app
