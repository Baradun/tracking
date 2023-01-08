from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

import os
import sys

fpath = os.path.join(os.path.dirname(__file__), "src")
sys.path.append(fpath)

from src.project import Project
from src.user import User

from models import users_scheme
import databases

import models
from sqlalchemy.orm import Session
from pydantic import BaseModel

DATABASE_URL = "postgresql://postgres:123456@localhost/TestDB"
base = databases.Database(DATABASE_URL)

app = FastAPI()

projects = dict()
users = dict()

@app.on_event("startup")
async def startup():
    await base.connect()


@app.on_event("shutdown")
async def shutdown():
    await base.disconnect()


# --------
# Users
# --------


# ## add user to project
# @app.post("/users/attach")
# def attach_user(projectId: int, userLogin: str):
#     # debug code
#     if len(projects) == 0:
#         projects[projectId] = Project("123")
#     if len(users) == 0:
#         users[userLogin] = User(userLogin, "qwerty")
#     # end debug code
#
#     user = users[userLogin]
#     projects[projectId].addUser(userLogin, "qwerty")
#     return JSONResponse(
#                 status_code=status.HTTP_200_OK,
#                 content={"status": True}
#         )
#
# # remove user from project
# @app.post("/users/dettach")
# def detach_user(projectId: int, userLogin: str):
#     projects[projectId].removeUser(userLogin)
#     return JSONResponse(
#                 status_code=status.HTTP_200_OK,
#                 content={ "status": True }
#     )
#
# # get all users
# @app.post("/users")
# async def get_users():
#     return JSONResponse(
#                 status_code=status.HTTP_200_OK,
#                 content={ "users": list(users.keys()) }
#                 # content={ "users": database.fetch_all(query) }
#     )

# {
# "users": ["user1", "user2", "user3"]
# }
@app.post("/users")
def get_users(db: Session):
    users = db.querry(models.User).all()
    if len(users) == 0:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"users": []},
        )
    return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"users": [str(i.login) for i in users]},
        )

@app.post("users/login")
def users_login():
    pass

@app.post("users/register")
def users_register():
    pass

@app.post("users/attach")
def users_attach():
    pass

@app.post("users/detach")
def users_detach():
    pass

@app.post("users/roles/get")
def get_users_role():
    pass

@app.post("users/roles/change")
def change_users_role():
    pass

# --------
# Projects
# --------


# # get all users from project
# @app.post("/projects/users")
# def get_users_from_project(projectId: int):
#     return JSONResponse(
#                 status_code=status.HTTP_200_OK,
#                 content={"users": list(projects[projectId].users.keys()) }
#     )


class ProjectRequest(BaseModel):
    projectId: str

@app.post("/projects/users")
def get_users_in_project(db: Session, project: ProjectRequest):
    return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"users": [str(i.login) for i in db.querry(models.ProjectsUsers).filter(models.ProjectsUsers.project_id == project.Id)]},
        )

@app.post("/projects")
def get_progects(db: Session):
    pass


@app.post("/projects/create")
def create_project():
    pass


@app.post("/projects/change")
def change_project():
    pass


@app.post("/projects/testers")
def get_projects_testers():
    pass

@app.post("/projects/test/suites")
def get_projects_tests_suites():
    pass

@app.post("/projects/test/cases")
def get_projects_tests_cases():
    pass

@app.post("/projects/test/runs")
def get_projects_tests_runs():
    pass

@app.post("/projects/test/generate")
def generate_projects_tests_url():
    pass


# --------
# Tasks
# --------

@app.post("/tasks")
def get_tasks():
    pass


@app.post("/task")
def get_task():
    pass

@app.post("/task/create")
def create_task():
    pass


@app.post("/task/transit")
def transit_task():
    pass