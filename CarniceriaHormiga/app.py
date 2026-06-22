import streamlit as st
from dataclasses import dataclass

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Carnicería Hormiga", layout="wide")

# --- ESTILOS CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .card { 
        background-color: #262730; 
        padding: 20px; 
        border-radius: 15px; 
        border: 1px solid #ff4b4b; 
        margin-bottom: 10px;
    }
    h1 { color: #ff4b4b; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

@dataclass
class Producto:
    id_producto: int
    nombre: str
    precio: float
    stock: int

# Inventario (Usando el ID como clave principal)
inventario = {
    201: Producto(201, "Costilla", 8500.0, 15),
    202: Producto(202, "Vacío", 9200.0, 10),
    203: Producto(203, "Chorizo", 3500.0, 100),
    204: Producto(204, "Milanesa de Nalga", 7800.0, 20),
    205: Producto(205, "Aguja", 4200.0, 25),
    206: Producto(206, "Matambre", 8900.0, 8),
    207: Producto(207, "Falda", 5500.0, 12)
}

# Estado de la sesión
if 'carrito' not in st.session_state: st.session_state.carrito = {} # Diccionario {id: cantidad}
if 'compra_finalizada' not in st.session_state: st.session_state.compra_finalizada = False

st.title("🥩 CARNICERÍA HORMIGA")

if st.session_state.compra_finalizada:
    st.success("¡Compra realizada con éxito! Vuelva pronto.")
    if st.button("🛒 Seguir comprando"):
        st.session_state.compra_finalizada = False
        st.session_state.carrito = {}
        st.rerun()
else:
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Selección de Cortes")
        for id_p, prod in inventario.items():
            with st.container():
                st.markdown(f"""<div class="card">
                        <h4>{prod.nombre}</h4>
                        <p>Precio: ${prod.precio} | Stock: {prod.stock}</p>
                    </div>""", unsafe_allow_html=True)
                if st.button("Agregar al carrito", key=f"add_{id_p}"):
                    # Lógica con clave primaria
                    if id_p in st.session_state.carrito:
                        st.session_state.carrito[id_p] += 1
                    else:
                        st.session_state.carrito[id_p] = 1
                    st.rerun()

    with col2:
        st.subheader("🛒 Tu Pedido")
        total = 0
        for id_p, cantidad in st.session_state.carrito.items():
            prod = inventario[id_p]
            subtotal = prod.precio * cantidad
            total += subtotal
            
            subc1, subc2 = st.columns([3, 1])
            subc1.write(f"{prod.nombre} (x{cantidad}): ${subtotal}")
            if subc2.button("❌", key=f"del_{id_p}"):
                del st.session_state.carrito[id_p]
                st.rerun()
        
        st.markdown(f"### Total: ${total}")
        if st.session_state.carrito and st.button("Finalizar Pedido"):
            st.session_state.compra_finalizada = True
            st.rerun()
