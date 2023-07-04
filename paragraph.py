import json

input_file = 'test.json'

# Read the JSON file
with open(input_file, 'r') as file:
    sentences = json.load(file)

# Merge the sentences into a single paragraph
paragraph = ' '.join(sentences)

print(paragraph)