class {{ project_name|title }}Error(Exception):
    def __init__(self, errcode, status=400, message=''):
        self.errcode = errcode
        self.status = status
        self.message = message
