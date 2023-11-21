import numpy as np


############
class MyFun:

    def __init__(self, fun, df_dx_fun, df_dy_fun):
        self._fun = fun
        self._df_dx_fun = df_dx_fun
        self._df_dy_fun = df_dy_fun

    def df_dx(self, p_0):
        return self._df_dx_fun(p_0)

    def df_dy(self, p_0):
        return self._df_dy_fun(p_0)

    def __call__(self, p_0):
        return self._fun(p_0)


# chosen function

def get_two_dif_fun():
    # 3 * x^2 + x * y + 2 * y^2 - x - 4 * y
    def f(p_0):
        x, y = p_0
        return 3 * (x ** 2) + x * y + 2 * (y ** 2) - x - 4 * y

    def df_dx(p_0):
        x, y = p_0
        return 6 * x + y - 1

    def df_dy(p_0):
        x, y = p_0
        return x + 4 * y - 4
    
    return MyFun(fun=f, df_dx_fun=df_dx, df_dy_fun=df_dy)


def get_one_dif_fun():
    
    # (x + y) * |x + y|
    def f(p_0):
        x, y = p_0
        return (x + y) * np.abs(x + y)

    def df_dx(p_0):
        x, y = p_0
        return 2 * np.abs(x + y)

    def df_dy(p_0):
        x, y = p_0
        return 2 * np.abs(x + y)
    
    return MyFun(fun=f, df_dx_fun=df_dx, df_dy_fun=df_dy)


def df_dx(fun, p_0, eps):
    x, y = p_0
    return (fun((x + eps, y)) - fun((x, y))) / eps


def df_dy(fun, p_0, eps):
    x, y = p_0
    return (fun((x, y + eps)) - fun((x, y))) / eps
