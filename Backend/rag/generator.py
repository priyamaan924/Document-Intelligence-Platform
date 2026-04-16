def generate_answer(question, context):
    context_text = " ".join(context)
    return f"Based on books: {context_text[:200]}... Answer: {question}"