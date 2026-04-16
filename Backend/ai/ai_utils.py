def generate_summary(text):
    return f"Summary: {text[:100]}..."

def classify_genre(text):
    if "love" in text.lower():
        return "Romance"
    elif "mystery" in text.lower():
        return "Mystery"
    elif "space" in text.lower():
        return "Sci-Fi"
    else:
        return "General"

def recommend(book_title):
    return [f"{book_title} - Part 2", f"More like {book_title}"]