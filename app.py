import gradio as gr
from gpt4all import GPT4All

# Pfad zum Modell
model_path = "/path/to/your/model.gguf"

# Laden des Modells
model = GPT4All(model_path)

def generate_text(prompt):
    response = model.generate(prompt)
    return response

# Erstellen der Gradio-Oberfläche
iface = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(lines=4, placeholder="Enter your prompt here", label="Prompt"),
    outputs=gr.Textbox(label="Response"),
    title="GPT-4-All Interface"
)

iface.launch(server_name="0.0.0.0", server_port=7860)
