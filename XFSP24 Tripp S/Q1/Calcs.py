import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Model:
    def calculate_sto(self, weight, thrust, s=1000, C_Lmax=2.4, rho=0.002377, C_D0=0.0279, gc=32.174):
        # Basic calculation of STO based on thrust and weight variations
        v_stall = np.sqrt(weight / (0.5 * rho * s * C_Lmax))
        v_to = 1.2 * v_stall
        a = gc * (thrust / weight)
        b = gc / (weight * 0.5 * rho * s * C_D0)
        sto = np.array(
            [v_to * np.log((a / (a - b * v ** 2))) / (a - b * v ** 2) for v in np.linspace(0, v_to, num=100)])
        return sto


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super(PlotCanvas, self).__init__(fig)
        self.setParent(parent)

    def plot(self, weight, thrust):
        model = Model()
        sto = model.calculate_sto(weight, thrust)
        self.ax.clear()
        self.ax.plot(sto)
        self.ax.set_title('Take-off Distance vs. Thrust')
        self.ax.set_xlabel('Thrust')
        self.ax.set_ylabel('STO')
        self.draw()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Airplane Take-Off Simulation")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.weight_input = QLineEdit(self)
        self.weight_input.setPlaceholderText("Enter Weight in pounds")
        layout.addWidget(self.weight_input)

        self.thrust_input = QLineEdit(self)
        self.thrust_input.setPlaceholderText("Enter Thrust in pounds force")
        layout.addWidget(self.thrust_input)

        btn = QPushButton('Calculate STO', self)
        btn.clicked.connect(self.plot)
        layout.addWidget(btn)

        self.canvas = PlotCanvas(self, width=8, height=6)
        layout.addWidget(self.canvas)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def plot(self):
        weight = float(self.weight_input.text())
        thrust = float(self.thrust_input.text())
        self.canvas.plot(weight, thrust)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())