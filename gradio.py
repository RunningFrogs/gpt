import torch
from gpt4all import GPT4All  # Stellen Sie sicher, dass dies der richtige Import ist
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
import gradio as gr

# Pfad zu Ihrem LocalDocs-Modell
model_path = "/path/to/your/localdocs_model.gguf"

# Laden des Modells
model = GPT4All(model_path)

def generate_text(prompt):
    response = model.generate(prompt)
    return response

def search_docs(query_str):
    ix = open_dir("indexdir")
    qp = QueryParser("content", schema=ix.schema)
    query = qp.parse(query_str)
    results = []
    with ix.searcher() as searcher:
        results = searcher.search(query, limit=10)  # Begrenzen auf die Top 10 Ergebnisse
        return [hit['content'] for hit in results]

def query_and_generate(query):
    docs = search_docs(query)
    context = " ".join(docs)
    prompt = f"Answer the question based on the following documents:\n\n{context}\n\nQuestion: {query}\nAnswer:"
    response = generate_text(prompt)
    return response

iface = gr.Interface(
    fn=query_and_generate,
    inputs=gr.Textbox(lines=2, placeholder="Enter your query here", label="Query"),
    outputs=gr.Textbox(label="Response"),
    title="LocalDocs Search Interface"
)

if __name__ == '__main__':
    print("Starting the server... Visit the link below to use the interface.")
    iface.launch(server_name="0.0.0.0", server_port=7860, share=True)
