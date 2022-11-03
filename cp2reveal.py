import glob, random
from pprint import pprint as pp
 
SHUFFLE_TIME = 99
SRC_PATH = "/Users/m1/Desktop/JustCactus/*.png"
OUTPUT_DIR = "./assets"

# get input files to chunk
chunk = [ f for f in glob.glob(SRC_PATH) ]

# shuffle
for rnd in range(1, SHUFFLE_TIME+1):
    random.shuffle(chunk)

# copy to asset folder
for (id, path) in enumerate(chunk):
    cmd = "cp {} {}/{}.png".format(path, OUTPUT_DIR, id)
    print(cmd)
