# Lab Experiment Controller UI

A Python-based graphical user interface (GUI) for simulating and controlling mock lab experiments. This project allows helps users to interact with simulated sensor data in real-time, visualize the data through live updating plots, and save the collected data to a CSV file for further analysis. It is intended for use in experimental setups where lab parameters, such as voltage and material types, need to be adjusted dynamically.

---

## Repository Description

### Features:
- **Simulated Sensor Data**: Generates random sensor data to simulate experiments (e.g., voltage, temperature).
- **Live Data Plot**: Visualizes real-time sensor data with a continuously updating plot.
- **Data Preprocessing**: Implements simple data preprocessing techniques like moving averages to smooth sensor data.
- **CSV Export**: Allows users to save the experiment data, including timestamps and sensor values, into a CSV file for further analysis.
- **User Interface**: Simple and intuitive UI built using Tkinter for ease of use during lab experiments.

---

### Technologies Used:
- **Python 3**: Programming language used to build the application.
- **Tkinter**: Python library for creating the GUI.
- **Matplotlib**: Used for plotting real-time sensor data.
- **Pandas**: Used for handling and preprocessing the data.

---

### Usage:
1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the program**:
   ```bash
   python main.py
   ```
3. **Interact with the application**:
   - Start and stop the simulated data collection using the provided buttons.
   - Visualize real-time sensor data on the plot.
   - Save the collected data to a CSV file for future reference.

---

### Example Workflow:
1. Launch the application.
2. Click **Start** to begin generating and visualizing sensor data.
3. Observe the live-updating plot of sensor readings.
4. Click **Save** to export the data to a CSV file for further analysis.
5. Click **Stop** to end the simulation.


