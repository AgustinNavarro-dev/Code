import openai

openai.api_key = "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"

def BasicGeneration(userPrompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "user", "content": userPrompt}
        ]
    )
    return completion.choices[0].message.content

prompt ="analiza el precio de la cryptomoneda Cardano el ultimo mes"

response = BasicGeneration(prompt)

print(response)