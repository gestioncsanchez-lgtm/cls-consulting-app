import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Academia de Capacitación | Dr. Ing. César Luis Sánchez",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilos visuales corporativos
st.markdown("""
<style>
    .main { background-color: #f8fafc; color: #1e293b; }
    .hero-container {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        text-align: center;
    }
    .hero-title { font-size: 2rem; font-weight: 800; margin-bottom: 0.5rem; }
    .hero-subtitle { font-size: 1.1rem; color: #93c5fd; }
</style>
""", unsafe_allow_html=True)

# Encabezado institucional
st.markdown("""
<div class="hero-container">
    <div class="hero-title">CLS Consulting — Asistente de Capacitación Inteligente</div>
    <div class="hero-subtitle">Liderado por el Dr. Ing. César Luis Sánchez | Doctor en Administración & Ing. Electricista</div>
</div>
""", unsafe_allow_html=True)

# Presentación inicial del consultor virtual
st.write("""
👋 **¡Bienvenido a nuestro espacio interactivo de capacitación y mejora continua!**  
Soy tu facilitador virtual entrenado bajo la metodología del **Dr. Ing. César Luis Sánchez**. Mi objetivo es ayudarte a transformar conocimientos en resultados medibles.

Puedes consultarme o pedirme mini-capacitaciones sobre:
- 📈 **Gestión Empresarial y Estratégica** (KPIs, OKRs, Diagnóstico).
- ⚙️ **Calidad y Mejora Continua** (Optimización de procesos, costos de no calidad, 5S, auditorías).
- 🚚 **Logística y Operaciones** (Inventarios, almacenamiento, distribución).
- 🤝 **Liderazgo y Equipos de Trabajo**.
- 🤖 **Innovación e Inteligencia Artificial** en los negocios.
""")

# Inicializar el historial de chat en Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hola. Soy el asistente académico de CLS Consulting. ¿En qué área de gestión, calidad o logística te gustaría que nos enfoquemos hoy para tu capacitación o la de tu equipo?"
        }
    ]

# Mostrar historial de mensajes en la pantalla
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Lógica de respuesta del Chatbot emulando la consultoría del Dr. Ing. César Luis Sánchez
def generar_respuesta_experto(prompt_usuario):
    p = prompt_usuario.lower()
    
    if "calidad" in p or "proceso" in p or "mejora" in p:
        return ("### ⚙️ Módulo de Calidad y Mejora Continua\n\n"
                "Desde nuestra perspectiva en **CLS Consulting**, la calidad no es solo cumplir normas, sino eliminar los "
                "**costos de no calidad**. \n\n"
                "* **Pregunta de análisis para ti:** ¿Has mapeado recientemente los pasos críticos o cuello de botella en tus procesos operativos?\n"
                "* **Acción sugerida:** Implementar indicadores de control visual y ciclos de retroalimentación corta con los mandos medios.")
    
    elif "logistica" in p or "inventario" in p or "distribucion" in p or "almacen" in p:
        return ("### 🚚 Módulo de Logística y Operaciones\n\n"
                "Una gestión logística eficiente equilibra el nivel de servicio al cliente con la optimización de recursos financieros.\n\n"
                "* **Enfoque del Dr. Ing. César Luis Sánchez:** La logística debe estar alineada a la estrategia comercial de la empresa. "
                "Un error común es mantener inventarios excesivos que ocultan ineficiencias operativas.\n"
                "* **Pregunta de reflexión:** ¿Cuál es tu tasa actual de entregas a tiempo (On-Time In-Full / OTIF)?")
    
    elif "kpi" in p or "estrategia" in p or "gestion" in p or "indicador" in p:
        return ("### 📈 Módulo de Gestión Empresarial y Estratégica\n\n"
                "Lo que no se mide, no se puede mejorar. Para liderar con éxito, integramos herramientas directivas:\n\n"
                "1. **KPIs** (Indicadores Clave de Rendimiento) para el control operativo.\n"
                "2. **OKRs** para alinear los objetivos de la organización.\n"
                "3. **KRIs** para medir riesgos clave.\n\n"
                "¿Qué área específica de tu organización necesita un diagnóstico de indicadores en este momento?")
    
    elif "liderazgo" in p or "equipo" in p or "talento" in p:
        return ("### 🤝 Módulo de Liderazgo y Desarrollo de Equipos\n\n"
                "Las herramientas técnicas solo funcionan si las personas están comprometidas. El liderazgo efectivo en mandos medios y directivos "
                "requiere comunicación clara, delegación estructurada y el desarrollo de una cultura de aprendizaje permanente.")
    
    else:
        return (f"Excelente planteamiento. Como especialista formado bajo más de 30 años de trayectoria internacional, "
                f"te comento que para abordar tu consulta sobre *'{prompt_usuario}'* debemos aplicar un enfoque estructurado: "
                f"diagnóstico inicial, diseño de la solución y medición de resultados.\n\n"
                f"¿Te gustaría que desarrollemos un taller práctico o un plan paso a paso sobre este tema para tu equipo de trabajo?")

# Capturar la entrada del usuario en el chat
if prompt := st.chat_input("Escribe tu duda, consulta de procesos o pide una mini-capacitación..."):
    # Agregar mensaje del usuario al historial
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generar y mostrar respuesta del asistente
    with st.chat_message("assistant"):
        respuesta = generar_respuesta_experto(prompt)
        st.markdown(respuesta)
        
    # Guardar respuesta en el historial
    st.session_state.messages.append({"role": "assistant", "content": respuesta})
