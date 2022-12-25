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

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def author(self):
        return self._author

    @property
    def executor(self) -> str:
        return self._executor

    @executor.setter
    def executor(self, executor):
        self._executor = executor