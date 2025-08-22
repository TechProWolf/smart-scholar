from transformers import pipeline

summarizer = pipeline('summarization')

def summarize_text(text, length='medium'):
    if len(text) > 4000:
        text = text[:4000]

    config = {
        'short': (40,15),
        'medium': (80, 60),
        'long': (160, 140)
    }

    max_len, min_len = config.get(length, (100, 30))
    result = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
    return result[0]['summary_text']
