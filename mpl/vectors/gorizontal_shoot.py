# Визуализация задачи "Бросок тела под углом к горизонту"
# created by NickIT87

import matplotlib.patches as mpatches   # импорт mpl для отрисовки "легенды"
import matplotlib.pyplot as plt         # программный объект для отрисовки графика
import numpy as np                      # библиотека для работы с двумерными массивами
from scipy.constants import g           # гравитационная постоянная

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
axes.set_xlim([0,12000])    # X
axes.set_ylim([-5,5])       # Y
axes.set_zlim([0,4000])     # Z

# Заголовок графика
axes.set_title(
    'Бросок тела под углом к горизонту, \n на примере ттх полковой гаубицы Д30', 
    color='black'
)

# задание ттх для полковой гаубицы Д30
# начальная скорость
V0 = 740            # ОФЗ 690 м/с  КМЛ 740 м/с
# время
t = 23              # 22 cек.
# угол стрельбы
alpha = 45          # 47 град.

# уравнения движения
x=np.array(
    [V0*dt*np.cos(np.deg2rad(alpha)) for dt in range(t)]
)
y=np.array(
    [0 for dt in range(t)]  #Ось y = 0 (движение ветра не учитываем)
)
z=np.array(
    [V0*dt*np.sin(np.deg2rad(alpha))-(0.5*g*dt)**2 for dt in range(t)]
)

# отрисовка параболы
HEAT_projectile_line = axes.plot3D(x,y,z,'red')

# отрисовка описания ТТХ, "легенда"
red_patch = mpatches.Patch(color='red', label='HEAT projectile: V=740m/s; a=45deg.')
axes.legend(handles=[red_patch])

# отрисовка графика
plt.show()