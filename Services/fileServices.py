import sys
sys.path.append('../')

import os
import io

from DataEntities.recipeEntry import RecipeEntry

def GenerateFileForEntry(recipeEntry: RecipeEntry):
    fileName = recipeEntry.recipeName + ".txt"
    fileContent = recipeEntry.recipeText
    file = open(fileName, "w+")
    file.write(fileContent)

    bkpnt = True

    file.close()