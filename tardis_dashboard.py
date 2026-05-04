import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import joblib

st.set_page_config(page_title="Dashboard", layout='centered')
st.title("Dashboard Sncf")

# Loading the model and data
model = joblib.load("model.pkl")


data = pd.read_csv("cleaned_dataset.csv")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m")
data["Mois"] = data["Date"].dt.month

# Calculating the historical average delay per journey and per month
data["retard_moyen_mois_global"] = (
    data.groupby(["Gare de départ", "Gare d'arrivée", "Mois"])
    ["Retard moyen de tous les trains au départ"].transform("mean")
)

stations = [
    "Mois",
    "Service",
    "Gare de départ",
    "Gare d'arrivée",
    "Nombre de circulations prévues",
    "retard_moyen_mois_global",
]

# Encoding columns to match the model's columns
X = pd.get_dummies(data[stations])

noms_mois = {
    "JANUARY": 1, "FEBRUARY": 2, "MARCH": 3, "APRIL": 4,
    "MAY": 5, "JUNE": 6, "JULY": 7, "AUGUST": 8,
    "SEPTEMBER": 9, "OCTOBER": 10, "NOVEMBER": 11, "DECEMBER": 12
}


new_data = pd.DataFrame(pd.read_csv('cleaned_dataset.csv'))
new_data["Date"] = pd.to_datetime(new_data["Date"])
head = new_data.head(1000)

gares_depart = sorted(data["Gare de départ"].str.strip().unique())

col1, col2 = st.columns(2)

with col1:
    gare_depart = st.selectbox("Departure station", gares_depart, index=gares_depart.index("MULHOUSE VILLE"))

# Filtering arrival stations based on the selected departure station
gares_arrive_possibles = sorted(
    data[data["Gare de départ"].str.strip() == gare_depart]["Gare d'arrivée"].str.strip().unique()
)

with col2:
    gare_arrive = st.selectbox("Arrival station", gares_arrive_possibles, index=gares_arrive_possibles.index("PARIS LYON") if "PARIS LYON" in gares_arrive_possibles else 0)

selection_label = st.selectbox("Month of journey", list(noms_mois.keys()))
selection_date = noms_mois[selection_label]  # Converting month name to number

if st.button("Estimate the delay"):

    # Finding rows matching the selected journey
    valeur = data[
        (data["Gare de départ"].str.strip() == gare_depart) &
        (data["Gare d'arrivée"].str.strip() == gare_arrive) &
        (data["Mois"] == selection_date)
    ]

    if valeur.empty:
        st.error("No routes found for this combination.")
    else:
        # Calculating journey averages
        number_journeys = valeur["Nombre de circulations prévues"].mean()
        average_delay_month_global = valeur["retard_moyen_mois_global"].iloc[0]
        service = valeur["Service"].mode()[0]

        input_df = pd.DataFrame([[
            selection_date,
            service,
            valeur["Gare de départ"].iloc[0],
            valeur["Gare d'arrivée"].iloc[0],
            number_journeys,
            average_delay_month_global
        ]], columns=stations)

        # Encoding and aligning columns with the model's columns
        input_encoded = pd.get_dummies(input_df)
        input_encoded = input_encoded.reindex(columns=X.columns, fill_value=0)

        prediction = model.predict(input_encoded)[0]

        # Converting prediction to minutes and seconds
        minutes = int(prediction)
        secondes = int((prediction - minutes) * 60)

        st.success(f"The estimated delay for this journey is {minutes} min {secondes} sec")

retard_moyen_trains_départ = "Retard moyen de tous les trains au départ"
fig_2 = new_data.set_index("Date").resample("ME")[retard_moyen_trains_départ].mean()

plt.style.use("default")
bg_color = "#0D1117"
line_color = "#3DDC6E"

fig, ax = plt.subplots(figsize=(10,5))

fig.patch.set_facecolor(bg_color)
ax.set_facecolor(bg_color)

ax.plot(fig_2.index, fig_2.values, color=line_color, linewidth=2)

ax.set_title("Average delay of all departing trains (2018-2026)", color="white")
ax.set_ylabel("Delay (min)", color="white")

ax.tick_params(colors="white")

for spine in ax.spines.values():
    spine.set_color("white")

ax.grid(True)

plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt.gcf())