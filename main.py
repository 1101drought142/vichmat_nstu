roots_interval = [
    [-4, -3],
    [-2, -1],
    [0, 1],
    [4, 5],
]

def main_func(x: float) -> float: 
    return (-x**4) + (15 * (x ** 2)) + (12 * x) - 10 

def main_func_proizvodn(x: float) -> float:
    return (-4 * (x ** 3)) + (30 * x) + 12

def main_func_proizvodn_2(x: float) -> float:
    return 30-(12*x)

def fi(x: float, lamd: float):
    return x + (lamd * main_func(x))

def get_lambd(start: int, end: int) -> float:
    step = 0.0001 
    max_mod = 0
    while (start < end):
        temp_res = main_func_proizvodn(start)
        if  abs(temp_res) > abs(max_mod):
            max_mod = temp_res
        start += step
    if (max_mod > 0):
        return 1/-max_mod
    else:
        return 1/abs(max_mod)

def next_step_newton(x : float) -> float:
    return x - (main_func(x))/(main_func_proizvodn(x))

def get_start_newton(x : float, prec : float) -> float:
    while (main_func(x) * main_func_proizvodn_2(x) <= 0):
        x += prec
    return x

def next_step_sec(x0 : float, x1 : float) -> float:
    return x0 - (((x0 - x1)*main_func(x0))/(main_func(x0) - main_func(x1)))

#Метод Ньютона
def newton(x0 : int, prec : float):
    x1 = next_step_newton(x0)
    while ( abs(x0 - x1) > prec): # 1.4
        print(f'x0 - {x0}; x1 - {x1}')
        x0 = x1
        x1 = next_step_newton(x0)
    return x1 
    
#Метод простых итераций
def simple_iteration(x0 : float, prec : float, lambd : float) -> float:
    x1 = fi(x0, lambd)
    while ( abs(x0 - x1) > prec): # 1.4
        print(f'x0 - {x0}; x1 - {x1}')
        x0 = x1
        x1 = fi(x0, lambd)
    return x1 

#Метод секущих
def sec_method(x0: float, x1 : float, prec : float):
    x2 = next_step_sec(x0, x1)
    while ( abs(x2 - x1) > prec): # 1.4
        print(f'x0 - {x0}; x1 - {x1}; x2 - {x2}')
        x0 = x1
        x1 = x2
        x2 = next_step_sec(x0, x1)
    return x2

def main():
    #Общие переменные
    prec = 0.001

    #Метода простых итераций
    #Для каждого интервала надо сделать функцию фи
    #Для каждой функцию фи надо посчитать лямбд
    print('Метод простых итераций')
    for interval in roots_interval:
        print(f'Начало интервала - {interval[0]}, Конец интервала - {interval[1]}')
        labmd = get_lambd(interval[0], interval[1])
        print(f'Лямбда - {labmd}')
        print('Начало итерации для данного интервала')
        result = simple_iteration(interval[0], prec, labmd)
        print('Конец итерации для данного интервала')
        print(f'Результат : {result}')

    #Метод Ньютона
    #Для метода ньютона надо утончить начальное прближние - f(x0) * f(x0)' > 0
    print('Метод Ньютона')
    for interval in roots_interval:
        print(f'Начало интервала - {interval[0]}, Конец интервала - {interval[1]}')
        temp_start = get_start_newton(interval[0], prec)
        print(f'Начальное приближение - {temp_start}')
        print('Начало итерации для данного интервала')
        result = newton(temp_start, prec)
        print('Конец итерации для данного интервала')
        print(f'Результат : {result}')

    #Метод секущих
    #Для метода секущих нужно получить два значения для начального приближения и уточнить их как для метода ньютона
    print('Метод секущих')
    for interval in roots_interval:
        print(f'Начало интервала - {interval[0]}, Конец интервала - {interval[1]}')
        temp_start_x0 = get_start_newton(interval[0], prec)
        temp_start_x1 = get_start_newton(temp_start_x0+prec, prec)
        print(f'Начальное приближение - x0 : {temp_start_x0}; x1 : {temp_start_x1}')
        print('Начало итерации для данного интервала')
        result = sec_method(temp_start_x0, temp_start_x1, prec)
        print('Конец итерации для данного интервала')
        print(f'Результат : {result}')

if __name__ == "__main__":
    main()