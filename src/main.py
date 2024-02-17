from openai import OpenAI

client = OpenAI(api_key='')

response = client.completions.create(model="gpt-3.5-turbo",
prompt="Please tell me the most delicious Thai curry restaurant in Tokyo.",
temperature=0.7,
max_tokens=100
)

print(response.choices[0].text)
