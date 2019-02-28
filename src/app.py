from utils import *
from Slide import Slide
from Slideshow import Slideshow
import sys



def Main(input_path):
    input_data = parseInput(input_path)
    
    # add the ID to the photos
    for i in range(len(input_data)):
        input_data[i] = [i, input_data[i]]

    orientation_dic = orientationDic(input_data)
    photo_list = photoList(input_data)

    # build horizontal slides
    hslides = []
    vslides = orientation_dic['V']
    
    for s in orientation_dic['H']:
        hslides.append(Slide([s]))


    #print(str([s.toString() for s in hslides]))
    #print(str(vslides))
    """
    print(input_data)
    print(photo_list)
    print(orientation_dic)

    s = Slide([photo_list[0]])
    s2 = Slide([photo_list[1],photo_list[2]])
    print(s.toString())
    print(s2.toString())
    ss = Slideshow()
    ss.addSlide(s)
    ss.addSlide(s2)
    print(ss.toString())
    """

if __name__ == '__main__':
    Main(sys.argv[1])