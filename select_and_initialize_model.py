from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftConfig, PeftModel
import torch

def select_and_initialize_model(model_name="ammarnasr/codegen-350M-mono-swift"):
    print(f"Initializing model: {model_name}")

    # Load PEFT configuration
    peft_config = PeftConfig.from_pretrained(model_name)

    # Initialize tokenizer
    tokenizer = AutoTokenizer.from_pretrained(peft_config.base_model_name_or_path)

    # Initialize model
    base_model = AutoModelForCausalLM.from_pretrained(peft_config.base_model_name_or_path)
    model = PeftModel.from_pretrained(base_model, model_name)

    return tokenizer, model

if __name__ == "__main__":
    # Select and initialize the model
    tokenizer, model = select_and_initialize_model()

    print("Model and tokenizer initialized successfully.")

    # Print model information
    print(f"Model architecture: {model.__class__.__name__}")
    print(f"Number of parameters: {sum(p.numel() for p in model.parameters())}")
    model.print_trainable_parameters()

    # Test tokenizer and model with a sample input
    sample_input = "// Write a Swift function to reverse a string."
    input_ids = tokenizer.encode(sample_input, return_tensors="pt")

    with torch.no_grad():
        output = model.generate(input_ids, max_length=200, num_return_sequences=1, do_sample=True, top_p=0.95, temperature=0.7)

    generated_code = tokenizer.decode(output[0], skip_special_tokens=True)
    print(f"\nSample input: {sample_input}")
    print(f"Generated output:\n{generated_code.strip()}")

    print("\nModel and tokenizer are ready for use in the AI iOS engineer project.")
