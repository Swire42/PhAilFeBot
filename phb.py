import discord
import tok
import random

class Bot(discord.Client):
    def __init__(self):
        super().__init__()

    async def on_ready(self):
        print("logged in as")
        print(self.user.name)
        print(self.user.id)

    async def on_message(self,message):
        if (message.author == self.user):
            return

        text = str(message.content)
        if "elle" in text.lower():
            if "encore" in text.lower():
                if random.randint(0,4)!=0:
                    return

            tab=['**Elle a pas encore mangé !**',
                    '__**ELLE A PAS ENCORE MANGÉ !**__',
                    '**eLlE a PaS eNcOrE mAnGé !**',
                    '**3773 A PA5 3NC0R3 MANG3 !**',
                    '**ELLE** a pas __encore__ mangé...']
            await message.channel.send(random.choice(tab))

if __name__ == "__main__":

    bot = Bot()

bot.run(tok.TOKEN)
