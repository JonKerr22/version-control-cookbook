from datetime import datetime

class RecipeEntry:
    """
    schema:
        entryId - int
        recipeId - int (entries are active/older version of recipe)
        recipeName - string
        recipeText - string
        timestamp - DateTime
        idk if more needed
    """

    def __init__(self, recipeName=None, recipeText=None, recipeId=None):
        #self.entryId = 0 #TODO - how do auto generate this? 
        self.recipeId = recipeId if recipeId is not None else 0
        self.recipeName = recipeName if recipeName is not None else ""
        self.recipeText = recipeText if recipeText is not None else ""
        self.timestamp = datetime.now()