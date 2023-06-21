import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':14})

times = ['Time A', 'Time B', 'Time C', 'Time D']
pontuacao_mulheres = [95, 82, 67, 80]
pontuacao_homens = [80, 91, 77, 65]

x = np.arange(len(times))

def autolabel(grupos):
    for i in grupos:
        h = i.get_height()
        ax.annotate('{}'.format(h),
                xy = (i.get_x()+i.get_width()/2,h),
                xytext = (0,3),
                textcoords = 'offset points',
                ha = 'center')

fig,ax = plt.subplots(figsize = (10,6))

largura = 0.35

grupo1 = ax.bar(x -largura/2, pontuacao_mulheres, largura, label = 'Mulheres', color = 'turquoise')
grupo2 = ax.bar(x +largura/2, pontuacao_homens, largura, label = 'Homens', color = 'tomato')

ax.set_title('Pontuação por grupo e por gênero')
ax.set_ylabel('Pontuação')

ax.legend()

ax.set_ylim([0,120])

ax.set_xticks(x)
ax.set_xticklabels(times)

autolabel(grupo1)
autolabel(grupo2)

plt.show()
