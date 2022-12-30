import math  

def paint_calc(height, width, cover):
    area = height * width 
    num_of_cons = math.ceil(area /cover) 
    print(f"yOU WILL NEED {num_of_cons} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall:")) 
coverage = 5 
paint_calc(height=test_h, width=test_w, cover=coverage)