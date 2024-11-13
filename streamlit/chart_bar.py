import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Adatok beállítása: Ugyanazokat az adatokat használjuk, mint a vonaldiagram esetén.
data = {'Date': ['2023-01', '2023-02', '2023-03', '2023-04', '2023-05'],
        'Value': [200, 250, 220, 270, 260]}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Oszlopdiagram létrehozása
#Dátum formázása:
#   - Az df['Date'].dt.strftime('%Y-%m') használatával az X tengelyen rövidebb, csak év-hónap formátumú dátumok jelennek meg.
fig, ax = plt.subplots()
ax.bar(df['Date'].dt.strftime('%Y-%m'), df['Value'], color='skyblue')  # Dátum formázása az X tengelyhez
ax.set_title('Energiafelhasználás Időbeli Alakulása')
ax.set_xlabel('Idő')
ax.set_ylabel('Érték')
ax.grid(True, axis='y')

# Diagram megjelenítése Streamliten
st.pyplot(fig)
