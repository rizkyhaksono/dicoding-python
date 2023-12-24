import pandas as pd

data = {
    "Nama": ["Rizky", "Haksono", "Natee"],
    "Usia": [20, 21, 22],
    "Pekerjaan": ["Engineer", "UI/UX", "Gamer"],
}

df = pd.DataFrame(data)
print(df)
