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

inventario = {
    201: Producto(201, "Costilla", 8500.0, 15),
    202: Producto(202, "Vacío", 9200.0, 10),
    203: Producto(203, "Chorizo", 3500.0, 100),
    204: Producto(204, "Milanesa de Nalga", 7800.0, 20),
    205: Producto(205, "Aguja", 4200.0, 25),
    206: Producto(206, "Matambre", 8900.0, 8),
    207: Producto(207, "Falda", 5500.0, 12)
}

if 'carrito' not in st.session_state: st.session_state.carrito = {} 
if 'compra_finalizada' not in st.session_state: st.session_state.compra_finalizada = False

st.title("🥩 CARNICERÍA HORMIGA")

if st.session_state.compra_finalizada:
    st.success("¡Compra realizada con éxito! Vuelva pronto.")
    if st.button("🛒 Seguir comprando"):
        st.session_state.compra_finalizada = False
        st.session_state.carrito = {}
        st.rerun()
else:
    # Creamos dos columnas principales: 70% catálogo, 30% carrito
    col_main, col_cart = st.columns([0.7, 0.3])

    with col_main:
        st.subheader("Selección de Cortes")
        # Grilla de 2 columnas para los productos dentro del espacio del catálogo
        g_cols = st.columns(2)
        for i, (id_p, prod) in enumerate(inventario.items()):
            with g_cols[i % 2]:
                with st.container():
                    st.markdown(f"""<div class="card">
                            <h4>{prod.nombre}</h4>
                            <p>Precio: ${prod.precio} | Stock: {prod.stock}</p>
                        </div>""", unsafe_allow_html=True)
                    if st.button("Agregar", key=f"add_{id_p}"):
                        if id_p in st.session_state.carrito:
                            st.session_state.carrito[id_p] += 1
                        else:
                            st.session_state.carrito[id_p] = 1
                        st.rerun()

    with col_cart:
        # Contenedor visual para el carrito a la derecha
        st.subheader("🛒 Tu Pedido")
        total = 0
        
        if not st.session_state.carrito:
            st.info("El carrito está vacío.")
        else:
            for id_p, cantidad in list(st.session_state.carrito.items()):
                prod = inventario[id_p]
                subtotal = prod.precio * cantidad
                total += subtotal
                
                st.write(f"**{prod.nombre}**")
                c1, c2, c3, c4 = st.columns([2, 1, 1, 1])
                c1.write(f"Cant: {cantidad} | ${subtotal}")
                
                if c2.button("➕", key=f"add_s_{id_p}"):
                    st.session_state.carrito[id_p] += 1
                    st.rerun()
                if c3.button("➖", key=f"sub_s_{id_p}"):
                    if st.session_state.carrito[id_p] > 1:
                        st.session_state.carrito[id_p] -= 1
                    else:
                        del st.session_state.carrito[id_p]
                    st.rerun()
                if c4.button("🗑️", key=f"del_s_{id_p}"):
                    del st.session_state.carrito[id_p]
                    st.rerun()
            
            st.markdown(f"---")
            st.markdown(f"### Total: ${total}")
            if st.button("Finalizar Pedido"):
                st.session_state.compra_finalizada = True
                st.rerun()
