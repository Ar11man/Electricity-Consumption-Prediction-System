import pandas as pd
import matplotlib.pyplot as plt

def show_graph(records):
    if not records:
        return

    data = []

    for record in records:
        data.append([record[2], record[3]])

    df = pd.DataFrame(data, columns=["Date", "Units"])

    df.groupby("Date")["Units"].sum().plot(kind="bar")

    plt.xlabel("Date")
    plt.ylabel("Electricity Consumption (kWh)")
    plt.title("Daily Electricity Consumption")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()