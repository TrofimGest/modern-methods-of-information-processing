import os

# 1 - i search imgs in current folder, if i need more imgs i search folders in folder and search imgs in them

def findDirsInFolder(folder):
    dirs=[]
    content = os.listdir(folder)
    for file in content:
        if os.path.isdir(os.path.join(folder, file)) and file != ".git" and file != ".idea" and file != "__pycache__" and file != "backgrounds" and file != "photos":
            dirs.append(file)
    return dirs

def findPhotosInFolder(folder):
    images=[]
    content = os.listdir(folder)
    for file in content:
        if os.path.isfile(os.path.join(folder, file)) and file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
            images.append(os.path.join(folder, file))
    return images


def getNPhotos(count):
    currentFolder = os.getcwd()
    images = findPhotosInFolder(currentFolder)

    foundCountOfPhotos = len(images)
    if(foundCountOfPhotos < count):
        dirs = findDirsInFolder(currentFolder)
        for file in dirs:
            newImages = findPhotosInFolder(os.path.join(currentFolder, file))
            if(foundCountOfPhotos + len(newImages) == count):
                return images
            elif(foundCountOfPhotos + len(newImages) > count):
                weNeed = count - foundCountOfPhotos
                i = 0
                while(i < weNeed):
                    images.append(newImages[i])
                    i = i + 1
                return images
            else:
                continue
    elif(foundCountOfPhotos > count):
        weNeedDelete = foundCountOfPhotos - count
        i = 0
        while(i < weNeedDelete):
            images.pop(-1)
            i = i + 1
        return images
    return images