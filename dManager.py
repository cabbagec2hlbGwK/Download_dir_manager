import os
import time
import json
import sys


def log(val, userprofile):
    with open(userprofile+"\\dir_manager\\log.txt", 'a') as file:
        file.writelines(val)
        file.writelines('\n')
        file.writelines('*'*50)
        file.writelines('\n')


def moveF(path, file, map, mapping, userprofile, rename=0):
    try:
        print("*"*50)
        if "#" in file:
            os.rename(path+'\\'+file,
                      mapping["fileM"][map]+"\\"+"'"+file.replace(map, "").replace("#", "")+(""if rename == 0 else str(rename)))
            log(path+'\\'+file+" -> " + mapping["fileM"][map] +
                "\\"+file.replace("#", "")+(""if rename == 0 else str(rename)), userprofile)
        else:
            os.rename(
                path+'\\'+file, mapping["fileM"][map]+"\\"+file+(""if rename == 0 else str(rename)))

            log(path+'\\'+file+" -> " + mapping["fileM"][map] +
                "\\"+file+(""if rename == 0 else str(rename)), userprofile)

    except FileExistsError:
        moveF(path, file, map, mapping, rename=rename+1)


def fSort(path, mapping, userprofile):
    files = [f for f in os.listdir(path) if os.path.isfile(path+"\\"+f)]
    for file in files:
        for map in mapping["fileM"]:
            if map in file:
                moveF(path, file, map, mapping, userprofile)
                break
    return


def monitor(path, mapping, userprofile):
    files = os.listdir(path)
    while True:
        time.sleep(10)
        if files != os.listdir(path):
            fSort(path, mapping, userprofile)
            files = os.listdir(path)


def main():
    userprofile = sys.argv[1]
    print(os.curdir)
    mapping = json.load(
        open(userprofile+"\\dir_manager\\mapping.json"))
    target = mapping["target_dir"]
    monitor(target, mapping, userprofile)


if __name__ == "__main__":
    main()
main()
