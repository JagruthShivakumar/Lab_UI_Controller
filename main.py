import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import threading
import time
import random
import pandas as pd

data = []
running = False

def generate_data():
    global running, data
    while running:
        value = random.uniform(20.0, 25.0)
        timestamp = pd.Timestamp.now()
        data.append((timestamp, value))
        update_plot()
        time.sleep(1)

def start():
    global running
    running = True
    threading.Thread(target=generate_data).start()

def stop():
    global running
    running = False

def update_plot():
    if len(data) > 0:
        times, values = zip(*data[-20:])
        ax.clear()
        ax.plot(times, values, marker='o')
        ax.set_title("Live Sensor Data")
        ax.set_xlabel("Time")
        ax.set_ylabel("Value")
        canvas.draw()

def save_data():
    # Save the data to CSV
    df = pd.DataFrame(data, columns=["Timestamp", "Value"])
    df.to_csv("experiment_data.csv", index=False)

    # Create the explanation file (data_explanation.txt)
    with open("data_explanation.txt", "w") as f:
        f.write("""
### Data Explanation for "experiment_data.csv"

This file contains the recorded sensor data from the lab experiment. It consists of two columns:

1. **Timestamp**: The exact date and time when the data was collected.
2. **Value**: The simulated sensor data reading at the given timestamp.

#### Structure of the Data

| Timestamp (Date and Time)          | Value (Sensor Reading)          |
|------------------------------------|---------------------------------|
""")

        # Add a sample of the data
        for row in data[:5]:  # Just first 5 rows for sample
            f.write(f"| {row[0]} | {row[1]} |\n")

        f.write("""
#### Columns Description:

1. **Timestamp**:
   - This represents the **exact date and time** the sensor data was recorded.
   - Format: `YYYY-MM-DD HH:MM:SS.mmmmmm` (microsecond precision).
   - Example: `2025-04-30 17:05:21.676854` means the data was recorded on **April 30, 2025, at 17:05:21 and 676854 microseconds**.

2. **Value**:
   - This is the **sensor reading** at the given timestamp.
   - It is a **floating-point number** representing a measurement, such as temperature, voltage, or another relevant value.
   - Example: `24.622818734339784` is the simulated sensor reading at that timestamp.

#### Observations:

- The **timestamps** are **sequential**, increasing by approximately 1 second, as per the data collection logic.
- The **values** are **randomly generated** within a specified range to simulate sensor fluctuations during the experiment.

---

#### Example Interpretation:

| Timestamp                      | Value        |
|---------------------------------|--------------|
| 2025-04-30 17:05:21.676854      | 24.622818734 |
| 2025-04-30 17:05:22.762808      | 24.921818900 |
| 2025-04-30 17:05:23.823464      | 22.690492717 |

- **2025-04-30 17:05:21.676854**: At this time, the sensor reading was **24.62**.
- **2025-04-30 17:05:22.762808**: One second later, the sensor reading increased slightly to **24.92**.
- **2025-04-30 17:05:23.823464**: Another second later, the reading dropped to **22.69**.

#### Usage:

- You can use this data to:
  - Analyze trends over time.
  - Plot the data for visualization.
  - Apply data analysis techniques such as smoothing, averaging, or filtering.

This file is a key output of the lab experiment simulation, and you can use it for further analysis or experiments.
""")

root = tk.Tk()
root.title("Lab Experiment UI")

mainframe = ttk.Frame(root, padding="10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Button(mainframe, text="Start", command=start).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(mainframe, text="Stop", command=stop).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(mainframe, text="Save", command=save_data).grid(row=0, column=2, padx=5, pady=5)

fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=1, column=0)

root.mainloop()
