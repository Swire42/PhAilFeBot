import discord
import tok
import random
import time
import motus

class Bot(discord.Client):
    def __init__(self):
        super().__init__()
        self.motusGame=None

    async def on_ready(self):
        print("["+time.asctime()+"] Logged in.")

    async def on_message(self, msg):
        if (msg.author == self.user):
            return

        async def cmdElle(msg):
            text = str(msg.content)
            if "elle" in text.lower():
                if "elle" in text.lower().split():
                    if random.randint(0,3)!=0:
                        return

                tab=['**Elle a pas encore mangé !**',
                        '__**ELLE A PAS ENCORE MANGÉ !**__',
                        '**eLlE a PaS eNcOrE mAnGé !**',
                        '**3773 A PA5 3NC0R3 MANG3 !**',
                        '**ELLE** a pas __encore__ mangé...']
                await msg.channel.send(random.choice(tab))

        async def cmdBadLang(msg):
            text = str(msg.content).lower()

            if sum([k in text.split() for k in ["certe", "certes"]]):
                    await msg.add_reaction("😡");

        async def cmdMotus(msg):
            text = str(msg.content).lower()
            if msg.channel.name=="motus":
                if self.motusGame==None:
                    if text=="motus":
                        self.motusGame=motus.Motus()
                        await msg.channel.send("```\n"+self.motusGame.txt()+"\n```")
                else:
                    if len(text)==8:
                        ret=self.motusGame.submit(text, msg.author.display_name)
                        if ret>=0:
                            await msg.channel.send("```\n"+self.motusGame.txt()+"\n```")
                            if self.motusGame.win():
                                await msg.channel.send("```\n"+self.motusGame.scoreboard()+"\n```")
                                self.motusGame=None

        await cmdElle(msg)
        await cmdBadLang(msg)
        await cmdMotus(msg)

if __name__ == "__main__":
    bot = Bot()

bot.run(tok.TOKEN)
