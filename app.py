import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import logging
import openai
from math import comb  # Importar la función comb para calcular combinaciones


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
openai.api_key = st.secrets["openai"]["api_key"]

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

st.markdown('<p style="font-size:16px;">Lee más sobre la <a href="https://www.linkedin.com/posts/warketing_el-poder-de-una-comunidad-robusta-y-solida-activity-7112052608076242945-Lm2q/?utm_source=share&utm_medium=member_desktop">Formula Warketing</a>.</p>', unsafe_allow_html=True)


# Get the number of contacts from the user
n = st.number_input('¿Cuántos contactos tienes en tu red?', min_value=0, value=5, format='%d')

# Calcula el número de combinaciones posibles para n elementos tomados de 2 en 2
num_combinaciones = comb(n, 2) if n >= 2 else 0

# Muestra el total de la combinación al usuario
st.write(f"Con {n} contactos, tienes {num_combinaciones} posibles interacciones únicas.")

st.header('Obtén ideas para mejorar tus interacciones', divider='rainbow' )

st.write('¿Cómo puedes mejorar el alcance de tu red? ¿Qué estrategias puedes implementar para maximizar el potencial de tu comunidad? ¡Haz magía para obtener ideas y recomendaciones!')

# Create a button, and when it's pressed, generate a recommendation
if st.button('Haz magía ✨'):
    prompt = f"Tienes una red de {n} contactos con {num_combinaciones} posibles interacciones únicas. ¿Cómo puedo mejorar mi efecto de network?"
    
    system_message = {
        "role": "system",
        "content": "Eres un AI experto consultor en marketing, y tu rol es recomendar estrategias para mejorar el alcance de una red, considerando la fórmula [ C(n, k) = \\frac{n!}{k!(n - k)!} ] donde (n) es el número total de elementos (miembros de la comunidad) y (k) es el número de elementos seleccionados a la vez (interacciones entre miembros). Responder en la menor cantidad de palabras y en frases completas. Da recomendaciones concretas y creativas, usa tu imaginación."
    }
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[system_message, {"role": "user", "content": prompt}],
            temperature=1,
            max_tokens=200,  # Ajusta según sea necesario para una sola línea de recomendación
        )
        idea = response['choices'][0]['message']['content'].strip()
        st.write(idea)
    except openai.error.OpenAIError as e:
        st.error(f"Error al generar recomendación: {e}")

st.header('Visualiza Tu Red', divider='rainbow' )

# Create a Graph
G = nx.complete_graph(n)

# Assign positions to each node using a circular layout
pos = nx.circular_layout(G)

# Draw the Graph using Matplotlib
plt.figure(figsize=(6,6))
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=15, font_weight='bold', alpha=0.6, edge_color='gray')
st.pyplot(plt)

st.markdown('<p style="font-size:16px;">Made for fun by <a href="http://kemeny.studio">kemeny.studio</a></p>', unsafe_allow_html=True)
