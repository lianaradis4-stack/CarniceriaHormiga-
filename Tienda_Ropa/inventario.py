import streamlit as st
from streamlit_gsheets import GSheetsConnection

# 1. Creamos la conexión con Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# 2. Leemos la planilla (asegúrate de que el nombre del archivo en 
# la configuración de Streamlit coincida con el nombre de tu hoja)
df = conn.read(spreadsheet="InventarioTienda", usecols=[0, 1, 2, 3])

st.title("👗 Inventario de la Tienda")

# 3. Mostramos los datos de forma elegante
st.dataframe(df, use_container_width=True)

# 4. (Opcional) Si querés que ella vea totales rápidos
total_productos = len(df)
st.metric("Productos cargados", total_productos)
