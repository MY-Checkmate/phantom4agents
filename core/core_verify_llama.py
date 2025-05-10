from transformers import LlamaForCausalLM, LlamaTokenizer

# Load the locally saved model and tokenizer
SAVE_PATH = "C:/professorai/1MANARMOUR/core/llama_model"
print("Loading the model and tokenizer...")
tokenizer = LlamaTokenizer.from_pretrained(SAVE_PATH)
model = LlamaForCausalLM.from_pretrained(SAVE_PATH)
print("Model and tokenizer loaded successfully!")

# Prompt for testing
input_text = "What are the top 5 penetration testing tools?"
print(f"Input Prompt: {input_text}")

# Tokenize input
inputs = tokenizer(input_text, return_tensors="pt")

# Generate response
print("Generating response...")
outputs = model.generate(inputs["input_ids"], max_length=50, num_return_sequences=1)

# Decode and print the response
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(f"Llama Response: {response}")