###################
Strealit környezetben tesztelve
###################
A projekt requirements.txt fájljába adjátok hozzá a PyYAML csomagot:

Parancs kiadása:
PyYAML

Töltsétek fel a módosított requirements.txt fájlt a GitHub-repozitóriumba.

A Streamlit Cloud automatikusan észlelni fogja a változást, és újratelepíti a szükséges csomagokat, vagy a "Manage app" felületen kérhetitek az alkalmazás újraindítását.

###################

Venv: Ez a beépített Python-virtuális környezet. Ha egyszerű, gyors és könnyen kezelhető környezetre van szükséged, válaszd ezt. Ideális kisebb projektekhez.

###################

Telepített csomagok:

pip install matplotlib
pip install pandas
pip install streamlit
pip install scikit-learn

###################

Környezet aktiválása:
  - A terminálon futtasd az alábbi parancsot, hogy a pandas csomagot a virtuális környezetben biztosan elérd:
  - Ellenőrizd a telepített csomagokat: A parancs segítségével listázhatod a telepített csomagokat, hogy meggyőződj róla, hogy a pandas és matplotlib elérhető:

source .venv/bin/activate
pip list
