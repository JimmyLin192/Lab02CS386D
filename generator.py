import sys, os
from random import shuffle
from random import seed
from random import randint

INT_MIN = 1
INT_MAX = 50000
LEN_TEXT = 247

# helper function
def usage(): 
    print "This program aims at generating a dataset of random value for CS386D Lab 01 and 02." 
    print "Usage: "
    print "    python generator.py [num_rows] [out_file]"

def generate_random_integer(lower=INT_MIN, upper=INT_MAX):
    return randint(lower, upper)

def generate_random_text(length=LEN_TEXT):
    chars = [ chr(randint(48,90)) for i in range(length) ]
    result = "".join(chars)
    result = result.replace("\n", "n")
    result = result.replace(",", "c")
    result = result.replace('''"''', "'")
    return result

def quote(word):
    return '''"''' + str(word) + '''"'''

def random_generate(v1fout, num_rows):
    for v1key in range(num_rows):
        # generate random values for each columns
        ht = generate_random_integer(0, 99999)
        tt = generate_random_integer(0, 9999)
        ot = generate_random_integer(0, 999)
        filler = generate_random_text()
        # generate strings for output
        v1instance = (v1key, ht, tt, ot, filler)
        v1string = ",".join(quote(val) for val in v1instance)
        # write to out file
        v1fout.write(v1string) 
        v1fout.write("\r\n")
        # update v1key
        v1key += 1

# main entrance
if __name__ == "__main__":
    # examine arguments
    nargs = len(sys.argv)
    if nargs != 3:
        usage()
        sys.exit(-1)
    # parse arguments
    num_rows = int(sys.argv[1])
    v1ofname = sys.argv[2] 
    # generate data of random values and write to <ofname>
    v1fout = open(v1ofname, "w+")
    seed(1)
    data = random_generate(v1fout, num_rows)
    v1fout.close()
