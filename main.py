# made by following bro codes tutorial for learning purposes

# Import necessary modules
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, Qt, QTime
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        # Create a label to display the time
        self.time_label = QLabel(self)
        # Create a timer to update the time
        self.timer = QTimer(self)
        # Initialize the user interface
        self.initUI()

    def initUI(self):
        # Set the window title
        self.setWindowTitle("Digital Clock")
        # Set the window size and position
        self.setGeometry(600, 540, 300, 100)

        # Create a vertical box layout
        vbox = QVBoxLayout()
        # Add the time label to the layout
        vbox.addWidget(self.time_label)
        # Set the layout for the widget
        self.setLayout(vbox)

        # Center-align the time label
        self.time_label.setAlignment(Qt.AlignCenter)

        # Set the style for the time label (font size and color)
        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: hsl(185, 100%, 50%);")
        
        # Set the background color of the widget to black
        self.setStyleSheet("background-color: black;")

        # Load a custom font
        font_id = QFontDatabase.addApplicationFont("VampireWars.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        myfont = QFont(font_family, 150)
        # Apply the custom font to the time label
        self.time_label.setFont(myfont)

        # Connect the timer's timeout signal to the update_time method
        self.timer.timeout.connect(self.update_time)
        # Start the timer with a 1-second interval
        self.timer.start(1000)

        # Update the time immediately upon initialization
        self.update_time()

    def update_time(self):
        # Get the current time and format it as "hh:mm:ss AM/PM"
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        # Update the time label with the current time
        self.time_label.setText(current_time)
        
if __name__ == '__main__':
    # Create a QApplication instance
    app = QApplication(sys.argv)
    # Create an instance of the DigitalClock widget
    clock = DigitalClock()
    # Show the clock widget
    clock.show()
    # Start the event loop and exit when it's done
    sys.exit(app.exec_())
