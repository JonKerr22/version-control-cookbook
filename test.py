import numpy as np
import git 
import pathlib

arr = np.array([1,2,3,4,5])
#print(arr)

ms = True
#print("hello world")



test_repo = git.Repo("testRepo")

test_repo.clone("../nestedDir")
#^ remember to delete the tests of these

brkpnt = True


#dataPath = pathlib.Path("testRepo")


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
