
import discord

TOKEN = 'NTU5MjA4MDE4NTcxNDI3ODQz.XqM_5A.OMcC9XrYq1cPZhKDVuEg3YxxNgQ'

client = discord.Client()
channel = client.get_channel(id)
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await  channel.send(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
