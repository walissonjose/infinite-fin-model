# Determinar a distribuição de temperatura

## Condição onde o tamanho da aleta é inifito

### Importando bibliotecas
bibliotecas utilizadas:
```python
import numpy as np
import matplotlib.pyplot as plt
```

Para uma aleta muito longa, a temperatura na extremidade da aleta é proporcional a temperatura da base.
O problema das aletas infinitas é uma análise térmica comum em engenharia que envolve determinar a temperatura ao longo de uma aleta (ou barra) que está exposta a uma fonte de calor em uma extremidade e tem uma condição de resfriamento (ou isolamento térmico adiabático) na outra extremidade.
A análise térmica de materiais em regime estacionário envolve considerações fundamentais, como a constância da condutividade térmica (k), a predominância da condução unidimensional de calor, a ausência de geração interna de calor, a uniformidade do coeficiente de transferência de calor convectivo (ℎ) ao longo da superfície do material e a dispersibilidade da radiação térmica. Além disso, em certos casos, a temperatura ao longo da espessura de uma aleta pode ser assumida como uniforme. Essas condições simplificam a modelagem matemática e a análise do comportamento térmico dos materiais, sendo essenciais para o projeto e a otimização de uma variedade de sistemas e processos industriais.
A distribuição de temperatura pode ser descrita pelas equações a seguir.
Distribuição de temperatura para o caso geral: (x)=T(x)-Tinfinito
Parâmetro adimensional: m2=hPkAr
Aleta infinita (L): (L)=0
Distribuição de temperatura para aletas infinitas: b=e-mx
De forma semelhante ao problema de van der vusse, a IA foi treinada usando os dados teóricos, desconsiderando a etapa de validação.


