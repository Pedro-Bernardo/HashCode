

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

#[['H', ['cat', 'beach']],['V', ['cat', 'old people']]]