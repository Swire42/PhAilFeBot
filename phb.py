import discord
import tok
import random
import time
import motus
import math
import sql

def proba(a, b, tau, t):
    return random.random() < b+(a-b)*math.exp(-t/tau)

class Bot(discord.Client):
    def __init__(self):
        super().__init__()
        self.sqldb=sql.SQLDB()
        self.motusGame=None
        self.motusLock=False
        self.time = time.time()
        self.elleTime = time.time()
        self.ditTime = time.time()
        self.shitTime = time.time()

    async def on_ready(self):
        print("["+time.asctime()+"] Logged in.")

    async def sayElle(self, chan):
        tab=['**Elle a pas encore mangé !**',
                '__**ELLE A PAS ENCORE MANGÉ !**__',
                '**eLlE a PaS eNcOrE mAnGé !**',
                '**3773 A PA5 3NC0R3 MANG3 !**',
                '**ELLE** a pas __encore__ mangé...']
        await chan.send(random.choice(tab))

    async def on_message(self, msg):
        if (msg.author == self.user):
            return

        async def cmdElle(msg):
            text = str(msg.content).lower()
            if proba(0.33, 0.75, 10*60, time.time()-self.elleTime):
                self.elleTime = time.time()
                if ("elle" in text) and ("mang" not in text):
                    await self.sayElle(msg.channel)

        async def cmdBadLang(msg):
            text = str(msg.content).lower()

            if sum([k in text.split() for k in ["certe", "certes"]]):
                await msg.add_reaction("😡");

            if ("elle" in text and "mang" in text) and ("pas" not in text) and ("?" not in text):
                await msg.add_reaction("😡");
                await self.sayElle(msg.channel)

            if ("elle" in text and "mang" in text) and ("?" in text):
                await self.sayElle(msg.channel)

            if ("phailf" in text) and ("PhAilF" not in str(msg.content)):
                await msg.add_reaction("😡");

        async def cmdMotus(msg):
            text = str(msg.content).lower()
            if msg.channel.name=="motus":
                if self.motusGame==None:
                    if "motus" in text:
                        self.motusGame=motus.Motus()
                        await msg.channel.send("```\n"+self.motusGame.txt()+"\n```")
                else:
                    ret=self.motusGame.submit(text, msg.author.display_name)
                    if len(text)==8:
                        if ret>=0:
                            await msg.channel.send("```\n"+self.motusGame.txt()+"\n```")
                            if self.motusGame.win():
                                await msg.channel.send("```\n"+self.motusGame.scoreboard()+"\n```")
                                await msg.channel.send("https://fr.wiktionary.org/wiki/"+"".join(self.motusGame.word).lower())
                                self.motusGame=None
                    if ret==-7 and text[0]==(self.motusGame.word[0].lower()):
                        await msg.add_reaction("7️⃣")
                    if ret==-9 and text[0]==(self.motusGame.word[0].lower()):
                        await msg.add_reaction("9️⃣")
                    if ret==-8:
                        await msg.add_reaction("📖")

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
            if proba(0.33, 0.75, 10*60, time.time()-self.ditTime):
                self.ditTime = time.time()

                text = str(msg.content)
                pos = text.lower().find("di")
                if pos == -1:
                    pos = text.lower().find("dy")
                if pos != -1:
                    if text[pos+2:len(text)]:
                        if text[pos+3:pos+4] == ' ':
                            if text[pos+3:len(text)]:
                                await msg.channel.send(text[pos+3:len(text)])
                        else:
                            await msg.channel.send(text[pos+2:len(text)])

        async def cmdShit(msg):
            if proba(0.01*self.sqldb.size(), 0.25, 60*60, time.time()-self.shitTime):
                self.shitTime = time.time()
                text=self.sqldb.get()
                if text is not None:
                    await msg.channel.send(text)

        await cmdElle(msg)
        await cmdBadLang(msg)
        await cmdMotus(msg)
        await cmdPerdu(msg)
        await cmdDit(msg)
        await cmdShit(msg)

    async def on_reaction_add(self, reaction, user):
        if "PhAilFeBot" in str(user): return
        if len(reaction.message.content)<=100:
            self.sqldb.add(reaction.message.content)

if __name__ == "__main__":
    bot = Bot()

bot.run(tok.TOKEN)
