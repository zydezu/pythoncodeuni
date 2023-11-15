import math

def assert_equals(expected, function, params, description='', failed=''):
    """Assert that function(params) == expected and print a passed or failed message.

    Args:
        expected (any): the expected returned value of function(params)
        function (callable): the name of the function to be tested
        params (tuple): the list of the parameter needed for the function 'function'
        description (str, optional): The description of the parameter to be included in the printed message. Defaults to ''.
        failed (str, optional): the additional message to be printed in case the test fails. Defaults to ''.
    """
    try:
        assert expected == function(*params)
        print(f'{description} --> Passed!')
    except AssertionError:
        print(f'{description} --> Failed! The expected value was {expected} and the function returned {function(*params)}!' + failed)
    except Exception as e:
        print(f'{description} --> An error occured: ' + str(e))

def assert_is_None(function, params, description='', failed=''):
    """Assert that function(params) is None and print a passed or failed message.

    Args:
        function (callable): the name of the function to be tested
        params (tuple): the list of the parameter needed for the function 'function'
        description (str, optional): The description of the parameter to be included in the printed message. Defaults to ''.
        failed (str, optional): the additional message to be printed in case the test fails. Defaults to ''.
    """
    try:
        assert function(*params) is None
        print(f'{description} --> Passed!')
    except AssertionError:
        print(f'{description} --> Failed! The expected value was None and the function returned {function(*params)}! ' + failed)
    except Exception as e:
        print(f'{description} --> An error occured: ' + str(e))

def assert_almost_equal(expected, function, params, precision=5, description='', failed=''):
    """Assert that function(params) == expected and print a passed or failed message. As the expected 

    Args:
        expected (float): the expected returned value of function(params)
        function (callable): the name of the function to be tested
        params (tuple): the list of the parameter needed for the function 'function'
        precision (int, optional): The level of precision needed to assert the equality of the two floats using math.isclose(), 
            more precisely |function(parames) - expected|<10**(-precision). Defaults to 5.
        description (str, optional): The description of the parameter to be included in the printed message. Defaults to ''.
        failed (str, optional): the additional message to be printed in case the test fails. Defaults to ''.
    """
    try:
        assert math.isclose(expected, function(*params), abs_tol= 10**(-precision))
        print(f'{description} --> Passed!')
    except AssertionError:
        print(f'{description} --> Failed! The expected value was {expected} and the function returned {function(*params)}!' + failed)
    except Exception as e:
        print(f'{description} --> An error occured: ' + str(e))
