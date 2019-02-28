
class Slideshow:
    def __init__(self):
        self.slides=[]
    def addSlide(self,slide):
        self.slides+=[slide]
    def toString(self):
        s=""
        s+=str(len(self.slides))+"\n"
        for i in self.slides:
            s+=str(i.toString())+"\n"
        return s


    