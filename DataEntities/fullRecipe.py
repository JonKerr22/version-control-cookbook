from .recipeEntry import RecipeEntry
from datetime import datetime

class FullRecipe:

    """
    schema:
        recipeId = int
        cookbookId = int
        allEntries = list with RecipieEntry type in it - not stored in DB, use a procedure to get list from id to generate
        createdDate = dateTime        
    """
    def __init__(self):
        self.recipeId = 0
        self.cookbookId = 0
        self.allEntries = []
        self.allEntries.append(RecipeEntry()) #init list with one entry
        self.createdDate = datetime.now()
    
    def UpdateRecipe(self, newRecipeObj):
        self.allEntries.append(newRecipeObj)

    def CreateFirstRecipeVersion(self, recipeName, recipeText):
        firstEntry = RecipeEntry(recipeName, recipeText, 1)
        self.allEntries = [] #clear list
        self.allEntries.append(firstEntry)

    def ClearAllRecipeEntries(self):
        self.allEntries = []

