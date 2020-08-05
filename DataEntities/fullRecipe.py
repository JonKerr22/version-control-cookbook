from .recipeEntry import RecipeEntry
from datetime import datetime
from multipledispatch import dispatch

class FullRecipe:

    """
    schema:
        recipeId = int
        cookbookId = int
        allEntries = list with RecipieEntry type in it - not stored in DB, use a procedure to get list from id to generate
        createdDate = dateTime        
    """
    def __init__(self, cookbookId=None, recipeId=None):
        self.recipeId = recipeId if not None else 0
        self.cookbookId = cookbookId if not None else 0
        self.allEntries = []
        self.allEntries.append(RecipeEntry()) #init list with one entry
        self.createdDate = datetime.now()
    
    def UpdateRecipe(self, newRecipeName, newRecipeText):
        newRecipeObj = RecipeEntry(newRecipeName, newRecipeText, len(self.allEntries)+1, self.recipeId)
        self.allEntries.append(newRecipeObj)
        return self

    def CreateFirstRecipeVersion(self, recipeName, recipeText):
        firstEntry = RecipeEntry(recipeName, recipeText, 1, self.recipeId)
        self.allEntries = [] #clear list
        self.allEntries.append(firstEntry)
        return self

    def ClearAllRecipeEntries(self):
        self.allEntries = []
        return self

    def ReadRecipeWithAllVersions(self):
        for entry in self.allEntries:
            print(entry.GetRecipeEntry())

    def GetLatestRecipeVersion(self):
        return self.allEntries[-1]