import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Dados para a tabela

x = np.arange(0, 150, 5)
# k is the heat transfer coefficient
k = 14 # W/mK
m = ((100*5*10**-3*np.pi)/(k*(np.pi*(5*10**-3)**2)/4))**-(1/2) # m is the constant of the exponential function e^(mx)
print(m)

# Para cada elemento de x, calcula-se e^(mx) e armazena em y
y = np.exp(-m*x, dtype=np.float64)

# Calcular a temperatura em cada ponto de x e armazenar em T
T = 75*y + 25

dados = {
    'x * 10^-3': x,
    'e^(mx)': y,
    'T(x)': T
}

# Criar o DataFrame
tabela = pd.DataFrame(dados)

# Exibir a tabela
print(tabela)

# Make a plot graphic of data x and T


plt.plot(x, T, 'r--')
plt.xlabel('x (m)')
plt.ylabel('T (°C)')
plt.title('Temperature x Position')
plt.grid(True)
plt.show()

