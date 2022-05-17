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
axes.set_zlim([0,30000])    # Z

# Заголовок графика
axes.set_title(
    '''Движение тяжелой материальной точки, брошенной под углом к горизонту.\n 
    (в однородном поле тяжести и безвоздушном пространстве) \n''', 
    color='black'
)

# функция расчета параболы
def draw_trajectory(V0:int, alpha:int, t_color:str, t_label:str, step:int=0, p_safe=False):
    # время полета
    t = 2 * V0 / g * np.sin(np.deg2rad(alpha))
    # Максимальный подъем
    H = pow(V0, 2)/(2*g) * pow(np.sin(np.deg2rad(alpha)), 2)
    # горизонтальная дальность, X1 = 0
    X2 = pow(V0, 2)*np.sin(np.deg2rad(alpha * 2))/g

    # уравнения движения
    x=np.array(
        [V0*dt*np.cos(np.deg2rad(alpha)) for dt in range(int(t))]
    )
    y=np.array(
        [step for dt in range(int(t))]  #Ось y = 0 (движение ветра не учитываем)
    )
    z=np.array(
        # общее уравнение движения с дифференцированием по времени
        # [V0*dt*np.sin(np.deg2rad(alpha))-0.5*g*pow(dt, 2) for dt in range(int(t))]
        
        # дифференцирование по оси Х (исключаем параметр t)
        [
            dx*np.tan(np.deg2rad(alpha))-g*pow(dx,2)/(2*pow(V0,2)*pow(np.cos(np.deg2rad(alpha)),2))
            for dx in x
        ]
    )
    # парабола безопасности
    z_safety = np.array(
        [
            pow(V0,2)/(2*g) - g/(2*pow(V0,2))*pow(dx, 2)
            for dx in x
        ]
    )
    # отрисовка параболы
    axes.plot3D(x,y,z, t_color)
    # отрисовка параболы безопасности, если аргумент p_safe=True
    if p_safe:
        axes.plot3D(x,y,z_safety, 'green')
    # максимальная точка подъема
    axes.scatter3D(X2/2, step, H, marker='x', c=t_color)
    # максимальная дальность
    axes.scatter3D(X2, step, 0, marker='*', c=t_color)
    # текст описания ТТХ, "легенда"
    return mpatches.Patch(
        color=t_color, 
        label=t_label + ' - V0:{0}m/s alpha:{1}deg H:{2:.2f}m t:{3:.2f}s S:{4:.2f}m'.format(
            V0, alpha, H, t, X2
        )
    )

# начальные скорости снарядов для полковой гаубицы Д30:
# ОФЗ 690 м/с  КМЛ 740 м/с

p1 = draw_trajectory(
    V0=690, alpha=45, t_color='blue', t_label='HIGH-EXPLOSIVE projectile', step=-4, p_safe=True
)
p2 = draw_trajectory(V0=740, alpha=45, t_color='red', t_label='HEAT projectile', p_safe=True)
p3 = draw_trajectory(V0=690, alpha=30, t_color='magenta', t_label='FlatTrajectory', step = 4)
p4 = draw_trajectory(V0=690, alpha=60, t_color='magenta', t_label='HingedTrajectory', step = 4)

# отрисовка легенды и графика
safety_parabola = mpatches.Patch(color='green', label='Парабола безопасности')
axes.legend(handles=[p1, p2, p3, p4, safety_parabola], loc='upper left')
plt.show()