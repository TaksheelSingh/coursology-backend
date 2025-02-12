from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization")

def summarize_text(text):
    """
    Summarize the given text (could be from a PPT or any other content).
    """
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']
