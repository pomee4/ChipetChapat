import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Adatok beállítása: Ugyanazokat az adatokat használjuk, mint a vonaldiagram esetén.
data = {'Date': ['2023-01', '2023-02', '2023-03', '2023-04', '2023-05'],
        'Value': [200, 250, 220, 270, 260]}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Oszlopdiagram létrehozása
#Oszlopdiagram készítése:
#   - Az ax.bar() függvényt használjuk, amely létrehozza az oszlopdiagramot.
#   - A color='skyblue' opcióval adunk neki egy halványkék színt.
#Grid:
#   - Csak a y tengelyen kapcsoljuk be a rácsvonalakat, hogy jobban látható legyen az értékek különbsége.
fig, ax = plt.subplots()
ax.bar(df['Date'], df['Value'], color='skyblue')
ax.set_title('Energiafelhasználás Időbeli Alakulása')
ax.set_xlabel('Idő')
ax.set_ylabel('Érték')
ax.grid(True, axis='y')

# Diagram megjelenítése Streamliten
st.pyplot(fig)
