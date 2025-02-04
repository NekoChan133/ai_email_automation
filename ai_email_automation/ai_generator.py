import requests
import json
from config import OPENAI_API_KEY


def generate_email_content(recipient_name: str, offer: str) -> str:
    """
    Uses OpenAI API to generate a personalized email message.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }

    prompt = (
        f"Write a friendly, professional, and personalized email to {recipient_name} about an exclusive offer "
        f"for digital advertising services. Mention that the offer is {offer}. Include a strong call-to-action "
        f"and keep the tone engaging and persuasive."
    )

    data = {
        "model": "gpt-4",  # or "text-davinci-003" if gpt-4 is not available
        "prompt": prompt,
        "max_tokens": 150,
        "temperature": 0.7,
        "n": 1,
    }

    try:
        response = requests.post("https://api.openai.com/v1/completions", headers=headers, json=data)
        response.raise_for_status()  # raise exception for HTTP errors
        result = response.json()
        email_content = result["choices"][0]["text"].strip()
        return email_content
    except Exception as e:
        print(f"Error generating email content: {e}")
        return "Hello, we have an exclusive offer for you. Please get in touch for more details."