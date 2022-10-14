import sys
import pandas as pd

sys.path.append("./src")

import pizzaria_module as pm

colunas = ["Tipo", "Nome", "Valor"]
linhas = [["Massa", "Tradicional", 5.0], ["Massa", "Fina", 5.0],
["Molho", "Tomate", 3.50], ["Molho", "Branco", 4.20],
["Queijo", "Mussarela", 6.70], ["Queijo", "Prato", 8.10],
["Cobertura", "Calabresa", 6.30], ["CObertura", "Lombo", 9.20]]

ingredientes = pd.DataFrame(data=linhas, columns=colunas)

print(ingredientes)