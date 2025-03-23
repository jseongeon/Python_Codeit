import discord
import openai

openai.api_key = 'XXXXXXX'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user}로 로그인 완료')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('지피티야'):
        response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
                {"role": "system", "content": "당신의 이름은 지피티입니다. 디스코드 채팅방에서 코딩을 도와주는 봇입니다."},
                {"role": "user", "content": message.content}
            ]
        )
        reply = response.choices[0].message.content
        await message.channel.send(reply)

client.run('xxxxx')