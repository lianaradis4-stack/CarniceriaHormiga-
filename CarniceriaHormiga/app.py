import streamlit as st
from dataclasses import dataclass

# 1. Definición de la estructura de datos
@dataclass
class Producto:
    id_producto: int
    nombre: str
    precio: float
    stock: int

# 2. Inventario optimizado con diccionario (Búsqueda O(1))
inventario = {
    201: Producto(201, "Costilla", 8500.0, 15),
    202: Producto(202, "Vacío", 9200.0, 10),
    203: Producto(203, "Chorizo", 3500.0, 100),
    204: Producto(204, "Milanesa de Nalga", 7800.0, 20),
    205: Producto(205, "Aguja", 4200.0, 25),
    206: Producto(206, "Matambre", 8900.0, 8),
    207: Producto(207, "Falda", 5500.0, 12)
}

# 3. Gestión de estado para el carrito
if 'carrito' not in st.session_state:
    st.session_state.carrito = []

# 4. Interfaz Web Profesional
st.set_page_config(page_title="Carnicería Hormiga", layout="wide")
st.title("🥩 Carnicería Hormiga - Sistema de Ventas")
st.markdown("---")

col1, col2 = st.columns([2, 1])

# Catálogo a la izquierda
with col1:
    st.subheader("Catálogo de Cortes Chaqueños")
    for id_p, prod in inventario.items():
        with st.container():
            c1, c2 = st.columns([3, 1])
            c1.write(f"**{prod.nombre}** | Precio: ${prod.precio} | Stock: {prod.stock}")
            if c2.button("Agregar", key=f"add_{id_p}"):
                st.session_state.carrito.append(prod)
                st.toast(f"{prod.nombre} agregado al carrito")

# Carrito a la derecha
with col2:
    st.subheader("🛒 Tu Carrito")
    if st.session_state.carrito:
        total = 0
        for i, item in enumerate(st.session_state.carrito):
            subcol1, subcol2 = st.columns([3, 1])
            subcol1.write(f"{item.nombre} - ${item.precio}")
            # Botón para eliminar un ítem específico
            if subcol2.button("❌", key=f"del_{i}"):
                st.session_state.carrito.pop(i)
                st.rerun()
            total += item.precio
        
        st.divider()
        st.write(f"### Total: ${total}")
        
        if st.button("Finalizar Pedido"):
            st.success("¡Compra realizada! Te esperamos en Carnicería Hormiga.")
            st.session_state.carrito = [] # Vaciamos el carrito
            st.rerun() # Recargamos para limpiar la vista
    else:
        st.info("El carrito está vacío.")
