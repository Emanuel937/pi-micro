api_key = 'sk-85t8bl_uOr9tHMUnCu7EpnaZ64gasx7m1Kw3f_Ncg0T3BlbkFJl08d7KucpX8NGykdObUF-HexfQaPH8EKAUylZqOQkA'

from openai import OpenAI
import os

client = OpenAI(
    api_key=api_key
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)