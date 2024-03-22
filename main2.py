import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

# Dados para a tabela
x = np.arange(0, 150, 5)
k = 14  # W/mK
m = ((100 * 5 * 10**-3 * np.pi) / (k * (np.pi * (5 * 10**-3)**2) / 4))**-(1/2)

# Para cada elemento de x, calcula-se e^(mx) e armazena em y
y = np.exp(-m * x, dtype=np.float64)

# Calcular a temperatura em cada ponto de x e armazenar em T
T = 75 * y + 25

# Criar o DataFrame
dados = {
    'x * 10^-3': x,
    'e^(mx)': y,
    'T(x)': T
}
tabela = pd.DataFrame(dados)

# Definir os dados de entrada (x) e saída (T)
x_train = x.reshape(-1, 1)
T_train = T.reshape(-1, 1)

# Definir o modelo de rede neural
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Compilar o modelo
model.compile(optimizer='adam', loss='mean_squared_error')

# Treinar o modelo
history = model.fit(x_train, T_train, epochs=1000, verbose=0)

# Plotar a perda durante o treinamento
plt.plot(history.history['loss'])
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Training Loss')
plt.show()

# Fazer previsões com o modelo treinado
predictions = model.predict(x_train)

# Plotar os dados originais e as previsões
plt.plot(x_train, T_train, 'b.', label='Original Data')
plt.plot(x_train, predictions, 'r-', label='Predictions')
plt.xlabel('x (m)')
plt.ylabel('T (°C)')
plt.title('Temperature x Position Prediction')
plt.legend()
plt.grid(True)
plt.show()
