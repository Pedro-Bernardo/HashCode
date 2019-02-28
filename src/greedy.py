from Slideshow import *
from Slide import *
def greedy(lista): #lista de Slides
    s=Slideshow()
    s.addSlide(lista[0])
    ids= list(range(1,len(lista)))
    maxi=-1
    idMaxi=0
    while len(ids)>0:
        for i in range(len(ids)):
            aux=s.compare(lista[ids[i]])
            if aux>maxi:
                maxi=aux
                idMaxi=i
        s.addSlide(lista[ids[idMaxi]])
        del ids[idMaxi]
        
    return s
    
def greedyVertical(verticais): #[[ids,[tags]]]
    def compare(p1,p2):
        counter=0
        for i in p1:
            if i in p2:
                counter+=1
        return min(len(p1)-counter,counter,len(p2)-counter)
   
    result=[]
    ids= list(range(len(verticais)))
    while len(ids)>0:
        maxi=-1
        idMaxi=0
        for i in range(1,len(ids)):
            aux=compare(verticais[ids[0]][1],verticais[ids[i]][1])
            if aux>maxi:
                maxi=aux
                idMaxi=i
        result+=[Slide([verticais[ids[0]],verticais[ids[idMaxi]]])]
        print(ids)
        del ids[idMaxi]
        del ids[0]
    for i in result:
        print(i.toString())

greedyVertical([[0,["oi","crlh","eheheh"]],[1,["d","w"]],[2,["oi","qqqq"]],[3,["d","aaa"]]])