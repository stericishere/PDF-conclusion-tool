import openai

openai.api_key = "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"

def chat_with_gpt3(prompt):
    if len(prompt) > 1000:
        return "Too much page"
    response = openai.completions.create(
        model = "gpt-3.5-turbo",
        prompt = "Write me a conclusion \"" + prompt + "\"",
        stop = None  # You can provide a list of strings to indicate stopping criteria.
    )
    return response.choices[0].text.strip()