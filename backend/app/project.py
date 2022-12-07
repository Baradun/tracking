
class Project:

    __global_id = 0

    def __init__(self, name):
        self._id = Project.__global_id
        Project.__global_id += 1

        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def is_archived(self) -> bool:
        return self._is_archived

    @property
    def users(self) -> list:
        return self._users

    @property
    def tasks(self) -> list:
        return self._tasks

    def addUser(self, user):
        self._users.append(user)

    def assignTaskToUser(self, task, user):
        pass

    def getReport(self):
        pass

    def addTask(self, task):
        self._tasks.append(task)

    def removeTask(self, task):
        pass

    def archive(self):
        self.is_archived = True

    def unarchive(self):
        self.is_archived = False