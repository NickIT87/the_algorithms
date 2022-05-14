# Визуализация задачи "Бросок тела под углом к горизонту в безвоздушном пр-ве"
# created by NickIT87

import matplotlib.patches as mpatches   # импорт mpl для отрисовки "легенды"
import matplotlib.pyplot as plt         # программный объект для отрисовки графика
import numpy as np                      # библиотека для работы с двумерными массивами
from scipy.constants import g           # гравитационная постоянная
from math import pow

# базовые настройки координатной сетки
fig=plt.figure()
axes = plt.axes(projection='3d')

# обозначения меток и цветов координатных осей
axes.set_xlabel("X [abscissus] - dist. m.", color='black')
axes.set_ylabel("Y [ordinatus] - n/a", color='black')
axes.set_zlabel("Z [applicata] - alt. m.", color='black')
axes.tick_params(axis='x', colors='darkred')
axes.tick_params(axis='y', colors='darkgreen')
axes.tick_params(axis='z', colors='darkblue')

# настройки шага сетки
axes.set_xlim([0,60000])    # X
axes.set_ylim([-5,5])       # Y
axes.set_zlim([0,14000])     # Z

# Заголовок графика
axes.set_title(
    '''Бросок тела под углом к горизонту на примере ттх полковой гаубицы Д30\n
    (расчеты произведены без учета сопротивления воздуха)''', 
    color='black'
)

# задание ттх для полковой гаубицы Д30
# начальная скорость
V0 = 740            # ОФЗ 690 м/с  КМЛ 740 м/с
# время
t = 106              # 22 cек.
# угол стрельбы
alpha = 45          # 47 град.
print("t: {}".format(
    2 * V0 / g * np.sin(np.deg2rad(alpha))
))
print("Zmax; H: {}".format(
    pow(V0, 2)/(2*g) * pow(np.sin(np.deg2rad(alpha)), 2)
))
print("Horizontal len; X2: {}".format(
    pow(V0, 2)*np.sin(np.deg2rad(alpha * 2))/g
))
# уравнения движения
x=np.array(
    [V0*dt*np.cos(np.deg2rad(alpha)) for dt in range(t)]
)
y=np.array(
    [0 for dt in range(t)]  #Ось y = 0 (движение ветра не учитываем)
)
z=np.array(
    # общее уравнение движения с дифференцированием по времени
    # [V0*dt*np.sin(np.deg2rad(alpha))-0.5*g*pow(dt, 2) for dt in range(t)]
    
    # дифференцирование по оси Х (исключаем параметр t)
    [
        dx*np.tan(np.deg2rad(alpha))-g*pow(dx,2)/(2*pow(V0,2)*pow(np.cos(np.deg2rad(alpha)),2))
        for dx in x
    ]
)

# отрисовка параболы
HEAT_projectile_line = axes.plot3D(x,y,z,'red')

# отрисовка описания ТТХ, "легенда"
red_patch = mpatches.Patch(color='red', label='HEAT projectile: V=740m/s; a=45deg.')
axes.legend(handles=[red_patch])

# отрисовка графика
plt.show()