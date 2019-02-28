

class Slide:
    def __init__(self,t):
        self.tags=t
    def getTags(self):
        return self.tags
    def score(self,slide):
        counter=0
        for i in self.tags:
            if i in slide.getTags():
                counter+=1
        return min(len(self.tags-counter,counter,len(slide.getTags())-counter))

    
    
    