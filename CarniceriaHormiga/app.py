import streamlit as st
from dataclasses import dataclass

# Estructura del registro
@dataclass
class Producto:
    id_producto: int
    nombre: str
    precio: float
    stock: int

# Inventario de Carnicería Hormiga
inventario = {
    201: Producto(201, "Costilla", 8500.0, 15),
    202: Producto(202, "Vacío", 9200.0, 10),
    203: Producto(203, "Chorizo", 3500.0, 100),
    204: Producto(204, "Milanesa de Nalga", 7800.0, 20),
    205: Producto(205, "Aguja", 4200.0, 25),
    206: Producto(206, "Matambre", 8900.0, 8),
    207: Producto(207, "Falda", 5500.0, 12)
}

if 'carrito' not in st.session_state:
    st.session_state.carrito = []

# Interfaz
st.set_page_config(page_title="Carnicería Hormiga", layout="wide")
st.title("🥩 Carnicería Hormiga - Sistema de Ventas")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Catálogo de Cortes Chaqueños")
    for id_p, prod in inventario.items():
        with st.container():
            c1, c2 = st.columns([3, 1])
            c1.write(f"**{prod.nombre}** | Precio: ${prod.precio} | Stock: {prod.stock}")
            if c2.button("Agregar", key=f"add_{id_p}"):
                st.session_state.carrito.append(prod)
                st.success(f"{prod.nombre} al carrito")

with col2:
    st.subheader("🛒 Carrito de Compras")
    if st.session_state.carrito:
        total = 0
        for i, item in enumerate(st.session_state.carrito):
            st.write(f"{i+1}. {item.nombre}: ${item.precio}")
            total += item.precio
        st.divider()
        st.write(f"### Total: ${total}")
        if st.button("Finalizar compra"):
            st.balloons()
            st.success("¡Compra realizada con éxito!")
            st.session_state.carrito = []
    else:
        st.info("El carrito está vacío.")