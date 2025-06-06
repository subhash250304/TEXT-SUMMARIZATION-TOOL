from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = "India is known for its cultural diversity because"
result = generator(prompt, max_length=60, num_return_sequences=1)

print("Generated Text:\n", result[0]['generated_text'])
