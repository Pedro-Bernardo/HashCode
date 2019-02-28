from utils import *
from Slide import Slide
import sys



def Main(input_path):
    input_data = parseInput(input_path)
    
    # add the ID to the photos
    for i in range(len(input_data)):
        input_data[i] = [i, input_data[i]]

    



if __name__ == '__main__':
    Main(sys.argv[1])