from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

import os
import sys

fpath = os.path.join(os.path.dirname(__file__), "src")
sys.path.append(fpath)

from src.project import Project
from src.user import User

app = FastAPI()

projects = dict()
users = dict()

# add user to project
@app.post("/user/attach")
def attach_user(projectId: int, userLogin: str):
    # debug code
    if len(projects) == 0:
        projects[projectId] = Project("123")
    if len(users) == 0:
        users[userLogin] = User(userLogin, "qwerty")
    # end debug code

    user = users[userLogin]
    projects[projectId].addUser(userLogin, "qwerty")
    return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={ "status": True }
        )

# remove user from project
@app.post("/user/dettach")
def detach_user(projectId: int, userLogin: str):
    projects[projectId].removeUser(userLogin)
    return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={ "status": True }
    )

# get all users
@app.post("/users")
def get_users():
    return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={ "users": list(users.keys()) }
    )

# get all users from project
@app.post("/projects/users")
def get_users_from_project(projectId: int):
    return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={ "users": list(projects[projectId].users.keys()) }
    )
