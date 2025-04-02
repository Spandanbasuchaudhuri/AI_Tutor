# course_generator/course_content_gen.py

import ollama

def generate_module_content(module_name, course_topic):
    """
    Generate detailed course content for a specific module using Llama3 via Ollama.
    The response will be streamed and should contain at least 1500 words.
    """
    prompt = (
        f"You are a skilled course content generator. The course topic is '{course_topic}'. "
        f"Generate detailed educational content for the module titled '{module_name}'. "
        f"Your response should be very comprehensive and contain at least 2500 words. "
        f"Break down the content into several sections with clear headers, include real-world examples, "
        f"explanations, and practical insights. Focus on thorough detail, and ensure the content is "
        f"structured logically. Do NOT include quizzes or exercises; just provide the detailed content."
    )

    response = ollama.chat(
        model="llama3:8b",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )

    content = ""
    for chunk in response:
        content += chunk['message']['content']
        yield content