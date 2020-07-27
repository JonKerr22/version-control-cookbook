from .fullRecipe import FullRecipe
from datetime import datetime

class UserCookBook:
    """
    schema:
        cookbookId - int
        userId - int
        allRecipes - list of type FullRecipe
        createdDate - dateTime

    """
    def __init__(self):
        self.cookbookId = 0
        self.userId = 0
        self.allRecipes = []
        self.allRecipes.append(FullRecipe())
        self.createdDate = datetime.now()