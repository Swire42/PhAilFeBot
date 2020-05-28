import discord
import tok
import random
import time
import motus

class Bot(discord.Client):
    def __init__(self):
        super().__init__()
        self.motusGame=None
        self.motusLock=False
        self.time = time.time()

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
            while self.motusLock:
                time.sleep(0.01)
            self.motusLock=True
            text = str(msg.content).lower()
            if msg.channel.name=="motus":
                if self.motusGame==None:
                    if "motus" in text:
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
            self.motusLock=False

        async def cmdPerdu(msg):
            text = str(msg.content).lower().split()
            if str(msg.channel) in ["settings"]:
                if time.time() - self.time >= 15*60:
                    if "j'ai" in text:
                        if "perdu" in text:
                            await msg.channel.send("**J'ai perdu !**")
                            self.time = time.time()
                if ("per" in text) and (time.time() - self.time >= 15*60) and (random.randint(0, 3)==0):
                    await msg.channel.send("**J'ai perdu !**")
                    self.time = time.time()

        async def cmdDit(msg):
            if random.randint(0, 3)==0:
                text = str(msg.content).lower()
                pos = text.find("di")
                if pos != -1:
                    if text[pos+2:len(text)]:
                        if text[pos+2] == 't':
                            if text[pos+3:len(text)]:
                                await msg.channel.send(text[pos+3:len(text)])
                        else:
                            await msg.channel.send(text[pos+2:len(text)])


        await cmdElle(msg)
        await cmdBadLang(msg)
        await cmdMotus(msg)
        await cmdPerdu(msg)
        await cmdDit(msg)

if __name__ == "__main__":
    bot = Bot()

bot.run(tok.TOKEN)
