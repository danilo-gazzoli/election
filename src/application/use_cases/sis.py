import sys
import os

novo_caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
print("Caminho adicionado:", novo_caminho)
sys.path.append(novo_caminho)
print("Caminhos no sys.path:")
for caminho in sys.path:
    print(caminho)