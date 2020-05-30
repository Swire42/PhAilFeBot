import random

class MotusDB:
    def __init__(self):
        with open("words", "r") as f:
            self.db=set([w for w in f.read().split() if len(w)==8])

db=MotusDB()

class Motus:
    def __init__(self):
        global db

        self.word=list(random.sample(db.db, 1)[0].upper())
        self.liste=[]
        self.found=["." for k in range(8)]
        self.found[0]=self.word[0]
        self.scores=dict()

        n=ord(self.word[0])-ord("A")
        self.submit(['alterees', 'batieres', 'contrees', 'deparees', 'enrouees', 'foutites', 'graciees', 'haleines', 'inserees', 'jaunites', 'karaites', 'lacerees', 'manieres', 'notaries', 'ouarines', 'partites', 'quintoie', 'reperees', 'surliees', 'tritiees', 'urinates', 'varietes', 'wurmiens', 'xanthome', 'yoyottas', 'zerotees'][n], "PhAilFeBot")
        self.submit(['assoupit', 'bouclant', 'chouinat', 'droiture', 'eventait', 'feculait', 'gagaouze', 'hourdent', 'ioulerai', 'jonglait', 'kiloeuro', 'loquetai', 'mollachu', 'nuptiale', 'opsomane', 'puniront', 'qataries', 'riboulat', 'saoudite', 'tabouise', 'utopiste', 'vouvoyat', 'webradio', 'xeriques', 'yttrique', 'zinguait'][n], "PhAilFeBot")

    def submit(self, w, name):
        global db
        score=0

        if (len(w)!=8) or (w[0].upper() != self.word[0]) or (w.lower() not in db.db):
            if len(w)==7: return -7
            if len(w)==9: return -9
            if len(w)==8 and w.lower() not in db.db: return -8
            return -1

        w=list(w.lower())
        tmp=self.word.copy()
        for k in range(8):
            if w[k].upper()==self.word[k]:
                score+=w[k].upper()!=self.found[k]
                w[k]=w[k].upper()
                self.found[k]=w[k]
                tmp.remove(w[k])

        for k in range(8):
            if w[k]==w[k].lower():
                if w[k].upper() in tmp:
                    w[k]=w[k].upper()
                    tmp.remove(w[k])

        self.liste.append(w)

        if name not in self.scores:
            self.scores[name]=score
        else:
            self.scores[name]+=score

        return score

    def txt(self):
        ret=""
        for w in self.liste:
            ret+="".join(w)+"\n"
        ret+="".join(self.found)
        return ret

    def win(self):
        return '.' not in self.found

    def scoreboard(self):
        t=list(self.scores.items())
        t.sort(key=(lambda x: -x[1]))

        ret=""
        for k in t:
            ret+=str(k[1])+" "+k[0]+"\n"
        ret+="- "+str(len(self.liste))+" Essais -"
        return ret
