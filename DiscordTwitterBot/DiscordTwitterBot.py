
#DO NOT MODIFY TOKEN AND DO NOT SHARE TOKEN
TOKEN = 'NTcxMTYyMTIzNTgyMDQ2MjA5.XMJwYQ.bSBuE55-s8cdC47OsdJQais4zUM'

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

client = MyClient()
client.run(TOKEN)
