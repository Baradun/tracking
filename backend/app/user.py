from task import Task

class User:

    _global_id = 0

    def __init__(self, login: str, password: str):
        self._id = Task._global_id
        Task._global_id += 1

        self._login = login
        self._password = password
        self._is_logined = False

    @property
    def login(self) -> str:
        return self._login

    def tryLogin(self, password: str):
        if (password == self._password):
            self._is_logined = True
        else:
            pass # we should raise Exception

    def logout(self):
        self._is_logined = False

    def changePassword(self, oldPassword: str, newPassword: str):
        if (self._password == oldPassword):
            self._password = newPassword
        else:
            pass # TODO: raise exception

    def assignTask(self, task: Task):
        task.executor = self

    @property
    def tasks(self) -> list:
        return self._tasks