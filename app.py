import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.title('El Poder de una Comunidad')
st.header   ('La Formula Warketing')
st.markdown("""
🌐✨ **¡Descubre el Verdadero Potencial de Tu Comunidad con la Fórmula Warketing!** ✨🌐

¿Crees que se necesitan miles de seguidores para crear un impacto significativo en línea? ¡Reconsidéralo! Con "El Poder de una Comunidad - La Fórmula Warketing", ¡descubre el número de interacciones y el potencial de conversaciones únicas que pueden surgir incluso de una pequeña comunidad de 14 seguidores! 🚀🔍

🌟 **Explora el Poder de Tu Comunidad** 🌟
No subestimes el valor de cada conversación dentro de tu red. ¡Incluso una comunidad pequeña puede tener hasta 91 interacciones diferentes! ¿Y si tu comunidad es más grande? ¡Imagina las posibilidades! 💬🤝

📊 **¡Calcula y Visualiza Tu Impacto!** 📊
Usa la Fórmula Warketing para visualizar y entender el potencial de tu comunidad. ¡Descubre cuán grande y conectada puede ser realmente tu red y construye relaciones más profundas y significativas! 🌟🔗

💻 **¡Empieza Ahora! Descubre, Calcula y Maximiza el Poder Único de Tu Comunidad con la Fórmula Warketing!** 💻
""")


# Get the number of contacts from the user
n = st.number_input('¿Cuántos contactos tienes en tu red?', min_value=0, value=5, format='%d')

# Create a Graph
G = nx.complete_graph(n)

# Assign positions to each node using a circular layout
pos = nx.circular_layout(G)

# Draw the Graph using Matplotlib
plt.figure(figsize=(6,6))
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=15, font_weight='bold', alpha=0.6, edge_color='gray')
st.pyplot(plt)

st.markdown('<p style="font-size:16px;">Made for fun by <a href="http://kemeny.studio">kemeny.studio</a></p>', unsafe_allow_html=True)
