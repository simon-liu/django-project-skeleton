from rest_framework.exceptions import PermissionDenied, Throttled
from rest_framework.response import Response
from rest_framework.views import exception_handler

from common.const import ErrorCode
from common.exceptions import {{ project_name|title }}Error


class ViewMixin(object):

    def build_ok_response(self, data=None, status=200):
        return Response({'code': ErrorCode.OK, 'data': data}, status=status)

    def raise_error(self, errcode, message='', status=400):
        raise {{ project_name|title }}Error(errcode=errcode, status=status, message=message)


def custom_exception_handler(exc, context):
    if isinstance(exc, PermissionDenied):
        errcode = ErrorCode.PERMISSION_DENIED
        return Response(
            status=403,
            data={
                'code': errcode,
                'message': ErrorCode.message(errcode)
            }
        )

    if isinstance(exc, Throttled):
        errcode = ErrorCode.TOO_MANY_REQUESTS
        return Response(
            status=429,
            data={
                'code': errcode,
                'message': ErrorCode.message(errcode)
            }
        )

    if isinstance(exc, {{ project_name|title }}Error):
        return Response(
            status=exc.status,
            data={
                'code': exc.errcode,
                'message': ErrorCode.message(exc.errcode),
                'debug': str(exc.message)
            }
        )

    return exception_handler(exc, context)
