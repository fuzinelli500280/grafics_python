import pandas as pd

data = {
    "Nome": ["Alice", "Bob", "Carlos"],
    "Idade": [25, 30, 22],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
}

df = pd.DataFrame(data)
print(df)