from user import User

class Task:

    _global_id = 0

    def __init__(self, name, description, status, author, executor):
        self._name = name
        self._description = description
        self._status = status
        self._author = author
        self._executor = executor

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def description(self) -> str:
        return self._description

    @name.setter
    def description(self, description):
        self._description = description

    @property
    def status(self):
        return self._status

    @name.setter
    def status(self, status):
        self._status = status

    @property
    def author(self) -> User:
        return self._author

    @property
    def executor(self) -> str:
        return self._executor

    @name.setter
    def name(self, executor):
        self._executor = executor