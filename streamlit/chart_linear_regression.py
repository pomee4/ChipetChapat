import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.linear_model import LinearRegression

# Adatok beállítása
data = {'Date': ['2023-01', '2023-02', '2023-03', '2023-04', '2023-05'],
        'Value': [200, 250, 220, 270, 260]}
df = pd.DataFrame(data)

# Dátumok számértékre alakítása a regresszióhoz
df['Date'] = pd.to_datetime(df['Date'])
df['Date_ordinal'] = df['Date'].map(pd.Timestamp.toordinal)  # Dátum konvertálása számmá

# Lineáris regressziós modell létrehozása:
#    - A sklearn.linear_model.LinearRegression osztályt használjuk a lineáris regresszióhoz.
X = df[['Date_ordinal']]
y = df['Value']
model = LinearRegression()
model.fit(X, y)

# Előrejelzés készítése
y_pred = model.predict(X)

# Diagram létrehozása
#Diagram készítése:
#   - Az eredeti adatokat pontokként (scatter) 
#   - Az előrejelzett értékeket vonalként (plot) jelenítjük meg
fig, ax = plt.subplots()
ax.scatter(df['Date'], df['Value'], color='blue', label='Eredeti Adatok')  # Eredeti adatok
ax.plot(df['Date'], y_pred, color='red', label='Lineáris Regresszió')  # Lineáris regressziós egyenes
ax.set_title('Lineáris Regresszió az Energiafelhasználás Időbeli Alakulására')
ax.set_xlabel('Idő')
ax.set_ylabel('Érték')
ax.legend()
ax.grid(True)

# Diagram megjelenítése Streamlitben
st.pyplot(fig)
