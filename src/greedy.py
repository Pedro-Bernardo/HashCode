from Slideshow import *
def greedy(lista): #lista de Slides
    s=Slideshow()
    s.addSlide(lista[0])
    ids= list(range(len(lista)))
    maxi=-1
    idMaxi=0
    while len(lista)>0:
        for i in ids:
            aux=s.compare(lista[i])
            if aux>maxi:
                maxi=aux
                idMaxi=i
        del ids[idMaxi]
        s.addSlide(lista[idMaxi])
    return s
    
        


