import plotly.express as px
import pandas as pd

# Datos del timeline
data = pd.DataFrame({
    "Event": [
        "Fundación de SpaceX",
        "Primer lanzamiento exitoso del Falcon 1",
        "Dragon llega a la ISS",
        "Primer vuelo tripulado del Crew Dragon"
    ],
    "Date": ["2002-03-14", "2008-09-28", "2012-05-22", "2020-05-30"],
    "Tipo": ["Fundación", "Lanzamiento", "Misión", "Misión Tripulada"]
})

# Crear timeline
fig = px.timeline(
    data, 
    x_start="Date", 
    x_end="Date",  # Timeline de puntos en lugar de intervalos
    y="Event", 
    color="Tipo", 
    title="Timeline Interactivo - SpaceX",
    color_discrete_map={"Fundación":"#007BFF","Lanzamiento":"#28A745","Misión":"#FFC107","Misión Tripulada":"#DC3545"}
)

fig.update_yaxes(autorange="reversed")  # Para que el primer evento quede arriba
fig.update_layout(height=500, width=900, showlegend=True)

# Guardar como HTML
fig.write_html("timeline_spacex.html", include_plotlyjs='cdn')

print("Timeline generado: timeline_spacex.html")