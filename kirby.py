import discord
import random

class MyClient(discord.Client):

    async def on_ready(self): #runs when bot joins
        print('Logged in')
        print(self.user.name)
        print(self.user.id)

    async def on_message(self, message): #runs on command
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if "hello kirby" in message.content.lower() or "hi kirby" in message.content.lower():
            responses=['Poyo!', 'POYO!!!', "poyo...","poyo"]
            await message.channel.send(responses[random.randint(0,3)].format(message))
        if "kirby" in message.content.lower() or "kirb" in message.content.lower() or "kerbe" in message.content.lower():
            responses=['Poyo?', 'poyo?', "poyo..?","Poyo?!", "POYO!","Poyo!","poyo","poyo..."]
            await message.channel.send(responses[random.randint(0,7)].format(message))

        if "thonk" in message.content:
            await message.channel.send('<:thonk:427839286197354498>'.format(message))

        if "squid" in message.content:

            await message.channel.send('<:Squid1:316026011693219841><:Squid2:316026053816614943><:Squid3:316026084380639233><:Squid2:316026053816614943><:Squid4:316026122662051850>'.format(message))

        if "bruh" in message.content.lower():
            await message.channel.send('https://tenor.com/view/bruh-gif-5156041'.format(message))

        if "xd" in message.content.lower():
            await message.channel.send('<:xd:494274299998371842>'.format(message))

        if "kirby spam" in message.content.lower():
            await message.channel.send('<:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465><:kerbe:586965684920254465>'.format(message))

        if message.content.startswith("obama gaming"):
            await message.channel.send('obama gaming'.format(message))

        if "yobama gaming" in message.content.lower():
            await message.channel.send("shut up".format(message))

        if "<@586581993819602956>" in message.content.lower():
            await message.channel.send("don't mention me or my mom <@!237236044599263232> ever again".format(message))

client = MyClient()
client.run('NTg2NTgxOTkzODE5NjAyOTU2.XPqHjw.UIo7h9OfxeBH0-NJWwqxCuyiHI8')
