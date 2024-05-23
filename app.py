import gradio as gr
from gpt4all import GPT4All

# Path to the model
model_path = "/path/to/your/model.gguf"

# Load the model
model = GPT4All(model_path)

def generate_text(prompt):
    response = model.generate(prompt)
    return response

# Create the Gradio interface
iface = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(lines=4, placeholder="Enter your prompt here", label="Prompt"),
    outputs=gr.Textbox(label="Response"),
    title="GPT-4-All Interface"
)

if __name__ == '__main__':
    print("Starting the server... Visit the link below to use the interface.")
    iface.launch(server_name="0.0.0.0", server_port=7860, share=True)
