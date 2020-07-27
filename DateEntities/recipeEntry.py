from datetime import datetime

class RecipeEntry:
    """
    schema:
        recipeId - int
        cookbookId - int (many recipes in each cookbook, only one cookbook in a recipe)
        recipeName - string
        recipeText - string
        timestamp - DateTime
        idk if more needed
    """

    def __init__(self):
        self.entryId = 0
        self.recipeId = 0
        self.recipeName = ""
        self.recipeText = ""
        self.timestamp = datetime.now()