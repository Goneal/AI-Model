from transformers import AutoTokenizer
from datasets import load_from_disk

# Load the dataset
dataset = load_from_disk('swift_functions_dataset')

# Initialize the tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")

def tokenize_code(code_list):
    tokenized_codes = []
    for code in code_list:
        tokens = tokenizer.encode(code, return_tensors='pt', truncation=True, max_length=512)
        tokenized_codes.append(tokens)
    return tokenized_codes

# Tokenize inputs and outputs
tokenized_inputs = tokenize_code(dataset['input_text'])
tokenized_outputs = tokenize_code(dataset['output_text'])

# Print some examples
print(f"Number of tokenized examples: {len(tokenized_inputs)}")
print("\nExample of tokenized input:")
print(tokenized_inputs[0])
print("\nDecoded tokenized input:")
print(tokenizer.decode(tokenized_inputs[0][0]))

print("\nExample of tokenized output:")
print(tokenized_outputs[0])
print("\nDecoded tokenized output:")
print(tokenizer.decode(tokenized_outputs[0][0]))

# Save tokenized data (optional)
# You might want to save this data for future use
import torch

torch.save({
    'tokenized_inputs': tokenized_inputs,
    'tokenized_outputs': tokenized_outputs
}, 'tokenized_swift_functions.pt')

print("\nTokenized data saved to 'tokenized_swift_functions.pt'")
