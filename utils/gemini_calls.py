import google.generativeai as genai

def call_gemini(api_key, idea, prompt):
    # Create the model
    genai.configure(api_key=api_key)
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
        }
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config=generation_config,
        system_instruction="Act as a senior project manager with vast experience in software development. Do not include any extra text in your responses.",
        )

    # Get response
    my_prompt = prompt + idea
    response=model.generate_content(my_prompt)
    
    return response.text

