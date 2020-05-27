import discord
import token

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

        text = str(message.content == 'test')
        message.channel.send('Test !')

if __name__ == "__main__":

    bot = Bot()

bot.run(TOKEN)
