import random
def make_random_list (num, range_start, range_end):
 numlist = []
 for num in range(num):
     numlist.insert(num,random.randint(range_start, range_end))

     return numlist
    
#print(make_random_list(75,150, 500))

def ask_for_list():
    num1 = int(input("enter a number:   ")
    num2 = int(input("enter another number:   ")
    num3 = int(input("enter a final number:   ")
    return make_random_list(a,b,c)
