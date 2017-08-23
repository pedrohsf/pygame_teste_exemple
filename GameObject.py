
import threading

class minhaThread (threading.Thread):
    def __init__(self, threadID, nome, contador):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.nome = nome
        self.contador = contador

    def run(self):
        print ("Iniciando thread %s com %d processos" % (self.name,self.contador))
        self.processo()
        print ("Finalizando " + self.nome)

    def processo(self):
        while self.contador:
            print ("Thread %s fazendo o processo %d" % (self.nome, self.contador))
            self.contador -= 1

threads = []
for i in range(3):
    threads.append(minhaThread(i,str(i), 500))
    threads[i].start()

while threads[0].isAlive() or threads[1].isAlive() or threads[2].isAlive():
    print("esperando")


print("acabou-se tudo")