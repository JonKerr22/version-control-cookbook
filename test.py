import sys
sys.path.append('../')


import numpy as np
import git 
import pathlib
import random

from DataEntities.users import User
from DataEntities.fullRecipe import FullRecipe
from DataEntities.recipeEntry import RecipeEntry
from Services.fileServices import *


#arr = np.array([1,2,3,4,5])
#print(arr)

test_repo = git.Repo("testRepo")

ms = True

#hey these are gitignored files for now, don't need all that garbage in my github
testUserPath1 = "newUserRepos/users/271444183"
testUserPath2 = "newUserRepos/users/953598005"

userTestRepo1 = git.Repo(testUserPath1)
testCommits1 = list(userTestRepo1.iter_commits())
userTestRepo2 = git.Repo(testUserPath2)
testCommits2 = list(userTestRepo2.iter_commits()) #so 0th commit is most recent

#""" temp comment - here to stop constant repos getting redone
genUserId = random.randint(1, 1000000000)
testUser = User(genUserId, "ctor Username", "goodemail@email.website")

testRecipe = FullRecipe(genUserId, 1) #magic number 1: just test id for now
testRecipe.CreateFirstRecipeVersion("meatballs", "meat, salt, pepper, breadcrumbs, egg")


userRepoPath = "newUserRepos/"
#GenerateUserDirectory(testUser, userRepoPath)
userDirPath = userRepoPath+ "users/" + str(testUser.userId) + "/"
#GenerateRecipeFileForEntry(testRecipe, userDirPath)    #remember for now delete this after createed, but it works
                                                        #will need to pass a user path still, and also tie this into making it a git repo
#"""

""" temp comment - here to stop constant repos getting redone
test_repo = git.Repo("testRepo")

test_repo.clone("../nestedDir")
#^ remember to delete the tests of these
"""
brkpnt = True




"""
so basic ass steps for now
can do, use .git folder to generate files in another location

basic building block is just from the library, basically read in a foler with a .git file in it
likely would have a user folder, with each .git file being their cookbook
and then it's just going through files to pull out the raw .txt info (likely in the future would
be .html so that they can have styling to recipes, but as is for now)


soo that's all fantastic
I also gotta set up users with logins

and run it through a flask server
which connects to an angular front end to actually display the text is a good way

but these are notes for me in order to do an initial commit of this whole ass thing to github
"""
