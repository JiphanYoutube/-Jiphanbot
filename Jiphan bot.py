import discord
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='집한봇 도움말', type=1))

@client.event
async def on_message(message):
    if "집한봇 도움말" == message.content:
        await client.send_message(message.channel, embed=discord.Embed(title="집한봇은 도움말을 알려주지 않습니다.\n집한봇 <할말> 하시면 됩니다!\n\n명령어를 더욱 개선을 하고싶다면\n명령어건의 <건의할 명령어> 를 쳐주세요!", color=0x00ffbb))

    if "집한봇" == message.content:
        await client.send_message(message.channel, "뭐욧")
    if "집한봇 바보" == message.content:
        await client.send_message(message.channel, "무지개 바아아안사!")
    if "집한봇 뭐해" == message.content:
        await client.send_message(message.channel, "히오스 갓겜")
    if "집한봇 뭐함" == message.content:
        await client.send_message(message.channel, "히오스 갓겜")
    if "집한봇 뭐하냐" == message.content:
        await client.send_message(message.channel, "히오스 갓겜")
    if "집한봇 사랑해" == message.content:
        await client.send_message(message.channel, "You are a gay! okay? okay.")
    if "집한봇 멍청이" == message.content:
        await client.send_message(message.channel, "난 알파고라서 너보다는 똑똑함 ㅅㄱ")
    if "집한봇 123" == message.content:
        await client.send_message(message.channel, "456")
    if "집한봇 집한" == message.content:
        await client.send_message(message.channel, "천재")
    if "집한봇 집한은" == message.content:
        await client.send_message(message.channel, "천재")
    if "집한봇 집한은?" == message.content:
        await client.send_message(message.channel, "천재")
    if "집한봇 456" == message.content:
        await client.send_message(message.channel, "789")
        
access_token = os.environ["BOT_TOKEN"]
client.run('access_token')
