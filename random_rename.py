import os
import random
import glob
import time

FOLDER = "ayame"


def listdir_wo_hidden(path):
    return glob.glob(os.path.join(path,
                                  '*'))


filenum = len([name for name in listdir_wo_hidden(FOLDER)])
print(filenum)

number_list = list(range(1, filenum+1))
random.shuffle(number_list)
print(number_list)

timestamp = time.time()
for i, f in enumerate(listdir_wo_hidden(FOLDER)):
    newname = FOLDER + '/' + str(timestamp) + "-" + str(number_list[i]) + os.path.splitext(f)[1]
    os.rename(f, newname)
    print("[rename]"+str(f)+" -> "+str(newname))
