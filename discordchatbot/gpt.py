import openai

openai.api_key = 'XXXXXXX'

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "당신의 이름은 지피티입니다. 디스코드 채팅방에서 코딩을 도와주는 봇입니다."},
        {"role": "user", "content": "파이썬에서 별표를 삼각형으로 찍는 방법은?"}
    ]
)

print(response.choices[0].message.content)