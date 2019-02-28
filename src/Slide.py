

class Slide:
    def __init__(self, photos):
        self.tags = set()
        self.idPhotos = []

        for p in photos:
            self.idPhotos.append(p[0])
            self.tags = self.tags.union(set(p[1]))

        self.nTags = len(self.tags)

    def getTags(self):
        return self.tags
    def getNTags(self):
        return self.nTags
    def score(self,slide):
        counter=0
        for i in self.tags:
            if i in slide.getTags():
                counter+=1
        return min(len(self.tags)-counter,counter,len(slide.getTags())-counter)
    def toString(self):
        if len(self.idPhotos)==2:
            return str(self.idPhotos[0])+" "+str(self.idPhotos[1])
        else:
            return str(self.idPhotos[0])


    
    
    