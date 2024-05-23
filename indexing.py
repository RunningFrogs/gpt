from whoosh.index import create_in
from whoosh.fields import Schema, TEXT
import os

# Definieren des Schemas und Erstellen des Indexes
schema = Schema(content=TEXT(stored=True))
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")
ix = create_in("indexdir", schema)

# Hinzufügen von Dokumenten zum Index
writer = ix.writer()
documents = ["path/to/document1.txt", "path/to/document2.txt"]  # Pfade zu Ihren Dokumenten
for doc_path in documents:
    with open(doc_path, 'r', encoding='utf-8') as file:
        content = file.read()
        writer.add_document(content=content)
writer.commit()
