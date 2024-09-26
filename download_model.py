from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "ammarnasr/codegen-350M-mono-swift"

# Download the model and tokenizer
print("Downloading model...")
model = AutoModelForCausalLM.from_pretrained(model_name)
print("Model downloaded successfully.")

print("Downloading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
print("Tokenizer downloaded successfully.")

print("Model and tokenizer are ready for use.")
