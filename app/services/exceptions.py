class TaskServiceException(Exception):
    pass


class TaskNotFoundException(TaskServiceException):
    pass


class InvalidTaskNumberException(TaskServiceException):
    pass
