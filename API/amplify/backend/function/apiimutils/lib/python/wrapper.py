import json
import os

from requests import HTTPError
from http import HTTPStatus
from functools import wraps
import boto3 #libraire qui permet de gérer aws avec python


def exception_handler(func):
    @wraps(func)
    def wrapper(event, context):
        print(event['headers']['x-api-key'])
        response = {}
        try:

            if not event['headers'].get('x-api-key'):# != secret_key:
                raise PermissionError('x-api-key missing or wrong')

            res = func(event, context)
            if res:
                response['body'] = res
            response['statusCode'] = HTTPStatus.OK
        except HTTPError as error:
            response['statusCode'] = error.response.status_code
        except PermissionError as error:
            response['body'] = str(error)
            response['statusCode'] = HTTPStatus.FORBIDDEN
        except Exception as error:
            response['body'] = str(error)
            response['statusCode'] = HTTPStatus.INTERNAL_SERVER_ERROR
        return response

    return wrapper