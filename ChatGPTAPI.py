import openai

# Set up OpenAI API with your key
openai.api_key = ''



def main(prompt):
  full_prompt = prompt
  # Generate the response
  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=full_prompt,
    max_tokens=150
  )
  return response.choices[0].text.strip()
