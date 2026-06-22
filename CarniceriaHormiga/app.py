# --- EN LUGAR DE ST.COLUMNS ---
# Eliminamos las columnas y usamos el sidebar para el carrito
st.title("🥩 CARNICERÍA HORMIGA")

if st.session_state.compra_finalizada:
    st.success("¡Compra realizada con éxito! Vuelva pronto.")
    if st.button("🛒 Seguir comprando"):
        st.session_state.compra_finalizada = False
        st.session_state.carrito = {}
        st.rerun()
else:
    # --- CATÁLOGO PRINCIPAL ---
    st.subheader("Selección de Cortes")
    # Usamos columnas solo para el layout de los productos
    cols = st.columns(3) 
    for i, (id_p, prod) in enumerate(inventario.items()):
        with cols[i % 3]:
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

    # --- CARRITO FLOTANTE (SIDEBAR) ---
    with st.sidebar:
        st.header("🛒 Tu Pedido")
        total = 0
        if not st.session_state.carrito:
            st.write("El carrito está vacío.")
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
            
            st.markdown(f"### Total: ${total}")
            if st.button("Finalizar Pedido"):
                st.session_state.compra_finalizada = True
                st.rerun()
