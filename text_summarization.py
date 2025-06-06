from transformers import pipeline

summarizer = pipeline("summarization")

text = """India, officially the Republic of India, is a country in South Asia..."""  # Long input

summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
print("Summary:\n", summary[0]['summary_text'])
    
