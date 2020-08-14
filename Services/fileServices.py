import sys
sys.path.append('../')

import os
import io

from DataEntities.fullRecipe import FullRecipe
from DataEntities.users import User
from Services.repoServices import *

def GenerateRecipeFileForEntry(recipe: FullRecipe, filePath: str):
    #will need to make sure in user file, aka need to write in a relative path
    recipeEntry = recipe.GetLatestRecipeVersion()
    fileName = recipeEntry.recipeName + ".txt"
    fileContent = recipeEntry.recipeText
    file = open(filePath + fileName, "w+")
    file.write(fileContent)

    bkpnt = True

    file.close()

    CommitRecipeUserRepo(filePath, "adds/updates recipe")

def GenerateUserDirectory(user: User, dirPath: str):
    userPath = "users/" + str(user.userId) + "/"
    if not os.path.exists(dirPath+userPath):
        os.makedirs(dirPath+userPath)
        print("new repo for user: " + str(user.userId)) #TEMP - hey this maybe not to keep forver, but def for now
    userFileName = "userInfo.txt"
    userFileContent = user.username + "\n" + user.email + "\n" + "cookbooks: " + ",".join(user.GetAllUserCookBookIds(True)) + "\n"
    file = open(dirPath+userPath+userFileName, "w+")
    file.write(userFileContent)

    bkpnt = True

    file.close()

    InitNewUserRepo(dirPath+userPath,userFileName)

