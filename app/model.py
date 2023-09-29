from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np

# Load the model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Load the passages and metadata CSV file
df = pd.read_csv('/home/prince/Dropbox/Question-Answering-System/docs/passage_metadata.csv')

# Generate embeddings for each passage
embeddings = model.encode(df['Passage'].tolist())
# Displaying the first 2 embeddings for inspection
print(embeddings[:2])

# Add the embeddings to the DataFrame
df['Embedding'] = embeddings.tolist()

# Save the updated DataFrame to a new CSV file
df.to_csv('/home/prince/Dropbox/Question-Answering-System/docs/passage_metadata_emb.csv', index=False)

print("Embeddings generated successfully and saved to passage_metadata_emb.csv.")