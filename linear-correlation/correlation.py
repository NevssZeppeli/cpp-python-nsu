import numpy as np
import matplotlib.pyplot as plt


def decorrelate(xy):
    mean = np.mean(xy, axis=0)
    std = np.std(xy, axis=0)

    std = np.where(std == 0, 1.0, std)
    normal = (xy - mean) / std # нормализуем данные через вычитание среднего значения и деление на СКО 

    theta = np.pi / 4
    u, v = np.cos(theta), np.sin(theta)

    R = np.array([[u, -v], 
                  [v,  u]])
    
    xieta = normal @ R.T # поворот на угол 45

    def direct(data):
        norm = (data - mean) / std
        return norm @ R.T
        
    def inverse(data):
        inv_rot = data @ R 
        return inv_rot * std + mean
    
    return xieta, direct, inverse

def plot(xy, xieta):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    center = np.mean(xy, axis=0) # выделяем среднее значение
    cov = np.cov(xy.T)

    """
    cov = [[var(x),    cov(x,y)],
           [cov(x,y),  var(y)  ]] 
    Ковариационная матрица. Состоит из дисперсий и ковариаций между x,y. Ковариационная матрица нужна для определения "главных направлений" данных. 
    """

    eigvals, eigvecs = np.linalg.eig(cov) # собственные числа и векторы
    
    for i in range(2):
        ax1.arrow(center[0], center[1], 
                eigvecs[0,i] * 2 * np.sqrt(eigvals[i]),
                eigvecs[1,i] * 2 * np.sqrt(eigvals[i]),
                color='red', width=0.05, head_width=0.1, alpha=0.8)

    ax1.scatter(xy[:, 0], xy[:, 1], color='blue', s=0.5)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.grid(True)
    
    ax2.scatter(xieta[:, 0], xieta[:, 1], color='red', s=0.5)
    ax2.set_xlabel('ξ')
    ax2.set_ylabel('η')
    ax2.grid(True)

    center_new = np.mean(xieta, axis=0)

    ax2.set_aspect('equal')
    #std_xi, std_eta = np.std(xieta, axis=0)
    ax2.arrow(center_new[0], center_new[1], 1, 0, 
              color='blue', width=0.03, head_width=0.08, alpha=0.8)
    ax2.arrow(center_new[0], center_new[1], 0, 1, 
              color='blue', width=0.03, head_width=0.08, alpha=0.8)
    ax2.set_xlim(-4, 4)
    ax2.set_ylim(-4, 4)

    plt.tight_layout()
    plt.show()
    plt.savefig('scatter.png')


np.random.seed(100)
x = np.random.normal(2, 1.5, 1000) # 1000 рандомных чисел для независимой переменной
y = -1.2*x + 5 + np.random.normal(0, 0.8, 1000) # x создает основную линейную зависимость + шум
data = np.column_stack([x, y])

xieta, direct, inverse = decorrelate(data)

plot(data, xieta)