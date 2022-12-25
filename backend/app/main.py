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

@app.post("/user/attach")
def attach_user(project_id: int, user_login: str):
    # debug code
    if len(projects) == 0:
        projects[project_id] = Project("")
    if len(users) == 0:
        users[user_login] = User(user_login, "qwerty")
    # end debug code

    user = users[user_login]
    projects[project_id].addUser(user_login, "qwerty")
    return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={ "status": True }
        )

@app.post("/user/dettach")
def detach_user(project_id: int, user_login: str):
    projects[project_id].removeUser(user_login)
    return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={ "status": True }
    )
