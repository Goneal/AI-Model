from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftConfig, PeftModel
import torch

# Initialize tokenizer and model
model_name = "ammarnasr/codegen-350M-mono-swift"  # A model for Swift code generation
peft_config = PeftConfig.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(peft_config.base_model_name_or_path)
model = AutoModelForCausalLM.from_pretrained(peft_config.base_model_name_or_path)
model = PeftModel.from_pretrained(model, model_name)

def generate_code_for_task(task_description):
    prompt = f"""
// Swift iOS Development Task:
// {task_description}

// Requirements:
// 1. Generate a complete, well-structured Swift code snippet for iOS.
// 2. Use UIKit for UI components unless SwiftUI is specified.
// 3. Include necessary imports (e.g., UIKit, Foundation, SwiftUI if needed).
// 4. Implement proper error handling using do-catch blocks or Result type.
// 5. Add explanatory comments for complex logic.
// 6. Ensure the code is syntactically correct and follows Swift 5+ coding conventions.
// 7. Use modern iOS development patterns (e.g., delegation, closures, Combine).
// 8. Implement only the functionality described in the task.
// 9. Use appropriate access control modifiers (public, private, etc.).
// 10. Implement proper memory management (avoid retain cycles, use weak/unowned references).
// 11. Use guard statements for early exits and optional unwrapping.
// 12. Follow SOLID principles and use design patterns where applicable.
// 13. Implement unit tests for the generated code when appropriate.
// 14. Use async/await for asynchronous operations when applicable.
// 15. Implement proper documentation using Swift-style comments (///).
// 16. Consider using property wrappers like @Published for SwiftUI if relevant.
// 17. Implement proper state management (e.g., ObservableObject for SwiftUI).
// 18. Use Swift Package Manager for dependencies if needed.
// 19. Implement proper localization support using NSLocalizedString.
// 20. Consider accessibility features (e.g., VoiceOver support).

import UIKit
import Foundation

// MARK: - Implementation

"""
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    attention_mask = torch.ones_like(input_ids)  # Create attention mask

    print(f"Input IDs shape: {input_ids.shape}")
    print(f"Attention mask shape: {attention_mask.shape}")

    try:
        with torch.no_grad():
            print("Starting model generation...")
            output = model.generate(
                input_ids,
                attention_mask=attention_mask,  # Add attention mask
                max_length=2500,  # Increased to allow for more comprehensive implementations
                num_return_sequences=1,
                do_sample=False,  # Changed to False for compatibility with beam search
                repetition_penalty=1.5,  # Increased to further reduce repetition
                pad_token_id=tokenizer.eos_token_id,
                no_repeat_ngram_size=5,  # Increased to avoid larger phrase repetitions
                early_stopping=True,
                length_penalty=1.8,  # Increased to encourage longer, more detailed responses
                num_beams=4  # Added for beam search
            )
            print(f"Generation complete. Output shape: {output.shape}")

        code_snippet = tokenizer.decode(output[0], skip_special_tokens=True)
        print(f"Decoded snippet length: {len(code_snippet)}")
        return post_process_code(code_snippet.split("// MARK: - Implementation")[-1].strip())
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def post_process_code(code):
    # Remove any remaining markdown code block syntax
    code = code.replace("```swift", "").replace("```", "")

    # Ensure proper indentation
    lines = code.split("\n")
    indented_lines = []
    indent_level = 0
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.endswith("{"):
            indented_lines.append("    " * indent_level + stripped_line)
            indent_level += 1
        elif stripped_line.startswith("}"):
            indent_level = max(0, indent_level - 1)
            indented_lines.append("    " * indent_level + stripped_line)
        else:
            indented_lines.append("    " * indent_level + stripped_line)

    return "\n".join(indented_lines)

def post_process_code(code):
    # Remove any non-Swift content that might have been generated
    lines = code.split('\n')
    swift_code = []
    in_swift_block = False
    for line in lines:
        if line.strip().startswith('```swift'):
            in_swift_block = True
            continue
        elif line.strip().startswith('```'):
            in_swift_block = False
            continue
        if in_swift_block or not line.strip().startswith('```'):
            swift_code.append(line)
    return '\n'.join(swift_code)

if __name__ == "__main__":
    tasks = [
        'Create a LoginViewController with UITextField for email and password, and a UIButton for login. Implement basic UI setup and constraints using UIKit.',
        'Implement a UserAuthenticationManager class with methods for user login and registration using URLSession for network requests.',
        'Set up a CoreDataManager class to handle Core Data stack initialization and provide methods for saving and fetching User entities.'
    ]

    for task in tasks:
        code = generate_code_for_task(task)
        if code:
            processed_code = post_process_code(code)
            print(f"Task: {task}\nCode:\n{processed_code}\n")
            print("-" * 80 + "\n")
        else:
            print(f"Failed to generate code for task: {task}\n")

    print("Note: The generated code may require further refinement and adaptation for a specific iOS project.")
