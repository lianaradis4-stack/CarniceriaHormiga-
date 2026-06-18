import streamlit as st
from dataclasses import dataclass

@dataclass
class Producto:
    id_producto: int
    nombre: str
    precio: float
    stock: int

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
    
# Variable para controlar si mostramos el mensaje de éxito
if 'compra_finalizada' not in st.session_state:
    st.session_state.compra_finalizada = False

st.set_page_config(page_title="Carnicería Hormiga", layout="wide")
st.title("🥩 Carnicería Hormiga")

# Lógica de mensaje de finalización
if st.session_state.compra_finalizada:
    st.success("¡Compra realizada con éxito!")
    if st.button("Deseo comprar otros productos"):
        st.session_state.compra_finalizada = False
        st.rerun()
    if st.button("Vuelva pronto"):
        st.info("¡Gracias por su visita!")
        st.stop()
else:
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Catálogo")
        for id_p, prod in inventario.items():
            c1, c2 = st.columns([3, 1])
            c1.write(f"**{prod.nombre}** | ${prod.precio}")
            if c2.button("Agregar", key=f"add_{id_p}"):
                st.session_state.carrito.append(prod)
                st.rerun() # Solo recargamos para que el carrito se actualice en silencio

    with col2:
        st.subheader("🛒 Carrito")
        if st.session_state.carrito:
            total = 0
            for i, item in enumerate(st.session_state.carrito):
                subc1, subc2 = st.columns([3, 1])
                subc1.write(f"{item.nombre}: ${item.precio}")
                if subc2.button("❌", key=f"del_{i}"):
                    st.session_state.carrito.pop(i)
                    st.rerun()
                total += item.precio
            st.write(f"### Total: ${total}")
            if st.button("Finalizar Pedido"):
                st.session_state.compra_finalizada = True
                st.rerun()
        else:
            st.info("El carrito está vacío.")
