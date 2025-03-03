from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

completion = client.chat.completions.create(
  model="meta/llama-3.3-70b-instruct",
  messages=[{"role":"user","content":"Tell me about Machine Learning."}],
  temperature=0.2,
  top_p=0.7,
  max_tokens=1024,
  stream=True,
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")
