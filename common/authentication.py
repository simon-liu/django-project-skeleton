from rest_framework import authentication


class AnonymousUser(object):
    id = 0

    @property
    def is_authenticated(self):
        return False


class TokenAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        setattr(request, 'user', None)
        setattr(request, 'user_id', 0)

        return None, None


class FakeAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        user = FakeUser()

        setattr(request, 'user', user)
        setattr(request, 'user_id', user.id)

        return user, None


class FakeUser(object):
    id = 1

    @property
    def is_authenticated(self):
        return True
