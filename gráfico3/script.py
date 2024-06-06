import matplotlib.pyplot as plt


x = ['A', 'B', 'C', 'D', 'E']
y = [10, 20, 15, 25, 30]


plt.bar(x,y)

plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.title('Meu Gráfico de Barras')

plt.show()