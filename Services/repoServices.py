import sys
sys.path.append('../')

import os
import io

import git 

#Just a wrapper for gitpython
def InitNewUserRepo(fullDirPath: str, userInfoFileName: str):
    newRepo = git.Repo.init(fullDirPath)
    newRepo.index.add([userInfoFileName])
    newRepo.index.commit("Creates User File, inits user repo")
    newRepo.create_head("master")
