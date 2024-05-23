import gradio as gr
from gpt4all import GPT4All

# Definieren Sie die Modellpfade
model_paths = {
    "Model 1": "/path/to/your/model1.bin",
    "Model 2": "/path/to/your/model2.bin",
    "Model 3": "/path/to/your/model3.bin"
}

# Laden Sie die Modelle
models = {name: GPT4All(model=path) for name, path in model_paths.items()}

def generate_text(model_name, prompt):
    model = models[model_name]
    response = model.generate(prompt)
    return response

# Erstellen der Gradio-Oberfläche
iface = gr.Interface(
    fn=generate_text,
    inputs=[
        gr.inputs.Dropdown(choices=list(model_paths.keys()), label="Choose Model"),
        gr.inputs.Textbox(lines=4, placeholder="Enter your prompt here", label="Prompt")
    ],
    outputs=gr.outputs.Textbox(label="Response"),
    title="GPT-4-All Interface"
)

iface.launch(server_name="0.0.0.0", server_port=7860)
