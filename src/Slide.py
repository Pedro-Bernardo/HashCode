

class Slide:
    def __init__(self,t):
        self.tags=[]
        self.idPhotos=[]
        for i in t:
            if i[1] not in self.tags:
                self.tags+=[i[1]]
            self.idPhotos+=[i[0]] 
        self.nTags=len(self.tags)
    def getTags(self):
        return self.tags
    def getNTags(self):
        return self.nTags
    def score(self,slide):
        counter=0
        for i in self.tags:
            if i in slide.getTags():
                counter+=1
        return min(len(self.tags-counter,counter,len(slide.getTags())-counter))
    def toString(self):
        if len(self.idPhotos)==2:
            return self.idPhotos[0]+" "+self.idPhotos[1]
        else:
            return self.idPhotos[0]


    
    
    