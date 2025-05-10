from transformers import LlamaForCausalLM, LlamaTokenizer

# Step 1: Define the model name (Llama-2 7B in this case)
MODEL_NAME = "meta-llama/Llama-2-7b"

# Step 2: Download the tokenizer and model
print("Downloading the tokenizer...")
tokenizer = LlamaTokenizer.from_pretrained(MODEL_NAME)
print("Tokenizer downloaded successfully!")

print("Downloading the Llama model...")
model = LlamaForCausalLM.from_pretrained(MODEL_NAME)
print("Model downloaded successfully!")

# Step 3: Save the model and tokenizer locally
SAVE_PATH = "C:/professorai/1MANARMOUR/core/llama_model"
print(f"Saving the model and tokenizer to {SAVE_PATH}...")
model.save_pretrained(SAVE_PATH)
tokenizer.save_pretrained(SAVE_PATH)
print("Model and tokenizer saved successfully!")