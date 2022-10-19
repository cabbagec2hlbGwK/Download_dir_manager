import sys
import os
import time
import json


def moveF(path, file, map, mapping, rename=0):
    try:
        if "#" in file:
            os.rename(path+'\\'+file,
                      mapping["fileM"][map]+"\\"+file.replace(map, "").replace("#", "")+(""if rename == 0 else str(rename)))
        else:
            os.rename(
                path+'\\'+file, mapping["fileM"][map]+"\\"+file+(""if rename == 0 else str(rename)))

    except FileExistsError:
        moveF(path, file, map, mapping, rename=rename+1)


def fSort(path, mapping):
    files = [f for f in os.listdir(path) if os.path.isfile(path+"\\"+f)]
    print(files)
    for file in files:
        print(file)
        for map in mapping["fileM"]:
            print(map)
            if map in file:
                moveF(path, file, map, mapping)
    return


def monitor(path, mapping):
    files = os.listdir(path)
    while True:
        time.sleep(5)
        if files != os.listdir(path):
            fSort(path, mapping)
            files = os.listdir(path)


def main():
    print(os.curdir)
    mapping = json.load(open("mapping.json"))
    target = mapping["target_dir"]
    print(target)
    monitor(target, mapping)


if __name__ == "__main__":
    main()
