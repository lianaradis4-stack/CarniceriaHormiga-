import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("👗 Inventario Tienda")

# Conectamos directo poniendo el ID acá, así no tenés que configurar nada más
conn = st.connection("gsheets", type=GSheetsConnection)

# Acá pegamos el ID directo
df = conn.read(spreadsheet="13GGCyTwzEqCUZbj7iFohsS60SmxGSmQNhmlLVgMwtHU", usecols=[0, 1, 2, 3])

st.dataframe(df)
