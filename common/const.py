class ErrorCode(object):
    OK = 0
    TOO_MANY_REQUESTS = 1
    PERMISSION_DENIED = 2

    _messages = {
        OK: 'OK',
        TOO_MANY_REQUESTS: 'TOO_MANY_REQUESTS',
        PERMISSION_DENIED: 'PERMISSION_DENIED',
    }

    @classmethod
    def message(cls, code):
        return cls._messages[code]
