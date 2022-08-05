""" custom exception handlers """
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    handlers = {
        'Http404': _handle_negociation_error,
    }

    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        handler_function = handlers[exception_class]
        handler_function(exc, response, context )

    return response


def _handle_negociation_error(exc, response):
    response.status_code = exc.status_code
    response.data = {'message': exc.message}

