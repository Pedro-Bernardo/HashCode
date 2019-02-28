
class Slideshow:
    def __init__(self):
        self.slides=[]
    def addSlide(self,slide):
        self.slides+=[slide]
    def toString(self):
        s=""
        s+=str(len(self.slides))
        for i in self.slides:
            s+="\n"+str(i.toString())
        return s
    def compare(self,slide):
        return self.slides[-1].score(slide)


    