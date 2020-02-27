import math

# a method that returns sin(x) if sin(x) >= 0, 0 is returned otherwise
def f(x):
    sin_x = math.sin(x)
    # use ternary operator to shorten it
    return sin_x if sin_x >= 0 else 0


def run_test_f_x():  # runs two possible test cases for f(x)
    test_f_x_sin_x_greater_than_zero()
    test_f_x_sin_x_less_than_zero()


def test_f_x_sin_x_greater_than_zero():
    x = 90
    expected_result = math.sin(x)
    actual_result =f(x)
    assert expected_result == actual_result, "error in the function f(x). expected value greater than or equal to 0"
    # it's too uncomfortable to not receive a message after a successful test, so we print one
    print("passsed test_f_x_sin_x_greater_than_zero(). Exiting this test...")


def test_f_x_sin_x_less_than_zero():
    x = -1;
    expected_result = 0
    actual_result = f(x)
    assert expected_result == actual_result, "error! expected value is 0"
    # it's too uncomfortable to not receive a message after a successful test, so we print one
    print("passsed test_f_x_sin_x_less_than_zero(). Exiting this test...")


run_test_f_x()


r"""
PS D:\Program Files\Python_projects\IN-KJM1900\Oppgaver\Uke37> python .\half_wave.py
passsed test_f_x_sin_x_greater_than_zero(). Exiting this test...
passsed test_f_x_sin_x_less_than_zero(). Exiting this test...
"""
