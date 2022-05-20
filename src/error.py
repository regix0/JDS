'''
error.py implementation
'''

from werkzeug.exceptions import HTTPException

class AccessError(HTTPException):

    '''
    Class Description:
        Access error

    Arguments:
        N/A

    Exceptions:
        N/A

    Return Value:
        N/A
    '''

    code = 403
    message = 'Access Error'

class InputError(HTTPException):

    '''
    Class Description:
        Input error

    Arguments:
        N/A

    Exceptions:
        N/A

    Return Value:
        N/A
    '''

    code = 400
    message = 'Input Error'

class Success(HTTPException):

    '''
    Class Description:
        Success

    Arguments:
        N/A

    Exceptions:
        N/A

    Return Value:
        N/A
    '''

    code = 200
