import matplotlib.pyplot as plt
import numpy as np
from main import main_func, main_func_proizvodn

# создаём рисунок с координатную плоскость
fig = plt.subplots()

x = np.linspace(-5, 5, 100)

plt.plot(x, main_func(x))
plt.plot(x, main_func_proizvodn(x))

plt.xlabel('Ось х') #Подпись для оси х
plt.ylabel('Ось y') #Подпись для оси y
plt.title('График функции') #Название

ax = plt.gca()

# plot X - axis    
ax.axhline(y=0, color='k')

# plot Y - axis    
ax.axvline(x=0, color='k')
plt.show()