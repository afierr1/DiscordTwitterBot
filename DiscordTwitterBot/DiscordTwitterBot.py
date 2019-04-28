
#DO NOT MODIFY TOKEN AND DO NOT SHARE TOKEN
TOKEN = 'NTcxMTYyMTIzNTgyMDQ2MjA5.XMJwYQ.bSBuE55-s8cdC47OsdJQais4zUM'

import discord
import MyTwitterAPI




class MyClient(discord.Client):
    #prints on terminal when bot logs into Discord
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
    #When message is received, these action will be performed
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

        if message.content.startswith('!bye'):
            await message.channel.send('Bye {0.author.mention}'.format(message))

        if message.content.startswith('!get_tweet'):
            self.tweet = MyTwitterAPI.GetTwitter().getTweet(message.content)
            await message.channel.send(str(self.tweet).format(message))

client = MyClient()
client.run(TOKEN)






