import gradio as gr
from gpt4all import GPT4All

# Laden Sie mehrere Modelle (angenommen, Sie haben mehrere Modelle zur Auswahl)
model_names = ["Llama 3 Instruct"]
models = {name: GPT4All(model=name) for name in model_names}

def generate_text(model_name, prompt):
    model = models[model_name]
    response = model.generate(prompt)
    return response

# Erstellen der Gradio-Oberfläche
iface = gr.Interface(
    fn=generate_text,
    inputs=[
        gr.inputs.Dropdown(choices=model_names, label="Choose Model"),
        gr.inputs.Textbox(lines=4, placeholder="Enter your prompt here", label="Prompt")
    ],
    outputs=gr.outputs.Textbox(label="Response"),
    title="GPT-4-All Interface"
)

iface.launch(server_name="0.0.0.0", server_port=7860)
