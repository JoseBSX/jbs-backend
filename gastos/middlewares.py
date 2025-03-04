import uuid


class AddIDHeaderMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["X-Request-ID"] = str(uuid.uuid4())
        return response
