

def parseInput(path):
    photos = []
    lines = []

    with open(path, 'r') as file:
        lines = file.readlines()[1:]
    
    for l in lines:
        l = l[:-1]
        tokens = l.split(' ')
        photos.append([tokens[0], tokens[2:]])

    return photos


def outputSlides(outpath, slideshow):
    with open(outpath, 'w') as out:
        out.write(slideshow.toString())


def orientationDic(photos):
    dic = {'H': [], 'V': []}

    for p in photos:
        dic[p[1][0]].append([p[0], p[1][1]])

    return dic

#[['H', ['cat', 'beach']],['V', ['cat', 'old people']]]