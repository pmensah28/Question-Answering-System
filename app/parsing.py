# Import the necessary Libraries
import pandas as pd
import json
import re
# Reading the contents of one of the files "kwame-legal-LG-1680770745754_Technical.txt" file
with open("/home/prince/Dropbox/Question-Answering-System/dataset/Corpus/kwame-legal-LG-1680770745754_Technical.txt", "r") as file:
    technical_content = file.read()
# Displaying the first 100 characters to understand the structure
# print(technical_content[:100])

# Splitting the content by __section__ and __paragraph__ markers
sections = technical_content.split("__section__")[1:]  # Skipping the first empty split
paragraphs = [section.split("__paragraph__")[1:] for section in sections]  # Skipping the first empty split in each section
paragraphs = [item.strip() for sublist in paragraphs for item in sublist if item.strip()]

# Combining all the extracted passages into one passage
combined_passage = ' '.join(paragraphs)

# Splitting the combined passage into chunks of 5-sentences each
sentences = re.split(r'(?<=[.!?])\s+', combined_passage)
chunks_of_five_sentences = [' '.join(sentences[i:i+5]) for i in range(0, len(sentences), 5)]

# Displaying the first 2 chunks to check the results
# print(chunks_of_five_sentences[:2])

# Reading the contents of the kwame-legal-LG-1680770745754_Metadata.json file
with open("/home/prince/Dropbox/Question-Answering-System/dataset/Corpus/kwame-legal-LG-1680770745754_Metadata.json", "r") as file:
    metadata = json.load(file)

# Preparing the data for the CSV
data = {
    "Passage": chunks_of_five_sentences,
    "Metadata": [json.dumps(metadata) for _ in range(len(chunks_of_five_sentences))]
}
# Creating a DataFrame
df = pd.DataFrame(data)

# Saving the DataFrame to a CSV file
csv_path = "/home/prince/Dropbox/question_answering/docs/passage_metadata.csv"
df.to_csv(csv_path, index=False)

#Loading the passage_metadata dataframe
pm_df = pd.read_csv("/home/prince/Dropbox/Question-Answering-System/docs/passage_metadata.csv")
print(pm_df.head())