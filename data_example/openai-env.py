

#%%
from openai import OpenAI
client = OpenAI()


response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
#    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "What tourist sites do you recommend in Shanghai?"},
#    {"role": "user", "content": "Where was it played?"}
  ]
)

# %%
# the returned context
response.choices[0].message.content
# %%
