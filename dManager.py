import os
import time
import json


def log(val):
    with open(os.environ.get("USERPROFILE")+"\\dir_manager\\log.txt", 'a') as file:
        file.writelines(val)
        file.writelines('\n')
        file.writelines('*'*50)
        file.writelines('\n')


def moveF(path, file, map, mapping, rename=0):
    try:
        print("*"*50)
        if "#" in file:
            os.rename(path+'\\'+file,
                      mapping["fileM"][map]+"\\"+"'"+file.replace(map, "").replace("#", "")+(""if rename == 0 else str(rename)))
            log(path+'\\'+file+" -> " + mapping["fileM"][map] +
                "\\"+file.replace("#", "")+(""if rename == 0 else str(rename)))
        else:
            os.rename(
                path+'\\'+file, mapping["fileM"][map]+"\\"+file+(""if rename == 0 else str(rename)))

            log(path+'\\'+file+" -> " + mapping["fileM"][map] +
                "\\"+file+(""if rename == 0 else str(rename)))

    except FileExistsError:
        moveF(path, file, map, mapping, rename=rename+1)


def fSort(path, mapping):
    files = [f for f in os.listdir(path) if os.path.isfile(path+"\\"+f)]
    for file in files:
        for map in mapping["fileM"]:
            if map in file:
                moveF(path, file, map, mapping)
                break
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
    mapping = json.load(
        open(os.environ.get("USERPROFILE")+"\\dir_manager\\mapping.json"))
    target = mapping["target_dir"]
    monitor(target, mapping)


if __name__ == "__main__":
    main()
