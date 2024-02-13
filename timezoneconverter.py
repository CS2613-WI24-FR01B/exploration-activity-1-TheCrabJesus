import sys
import pendulum
import time
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QVBoxLayout, QWidget, QStackedWidget, QLabel, QSizePolicy
from PyQt6.QtCore import Qt, QTimer
WINDOW_SIZE = 500

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        # Create the toolbar
        toolbar = QToolBar(self)
        self.addToolBar(toolbar)
        
        # Add spacing between the toolbar buttons
        toolbar.setStyleSheet("QToolBar{spacing:25px;}");
        
        # Add stretchable space on the left
        left_spacer = QWidget()
        left_spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        toolbar.addWidget(left_spacer)

        # Create Home button and add to toolbar
        home_button = QPushButton('Home')
        home_button.clicked.connect(self.show_home_window)
        toolbar.addWidget(home_button)

        # Create View Timezone button and add to toolbar
        view_timezones_button = QPushButton('View Timezones')
        view_timezones_button.clicked.connect(self.show_view_timezones_window)
        toolbar.addWidget(view_timezones_button)

        # Create Plan Trip button and add to toolbar
        plan_trip_button = QPushButton('Plan Trip')
        plan_trip_button.clicked.connect(self.show_plan_trip_window)
        toolbar.addWidget(plan_trip_button)

        # Create Exit button and add to toolbar
        exit_button = QPushButton('Exit')
        exit_button.clicked.connect(self.close)
        toolbar.addWidget(exit_button)
        
        # Add stretchable space on the right
        right_spacer = QWidget()
        right_spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        toolbar.addWidget(right_spacer)

        # Create a stacked widget to switch between different windows
        self.stacked_widget = QStackedWidget(self)

        # Create the home window (Index 0)
        self.home_window = QWidget(self)
        self.home_window_layout = QVBoxLayout(self.home_window)
        # Create the title label
        self.home_title_label = QLabel('<h1>Timezone Converter</h1>', alignment=Qt.AlignmentFlag.AlignCenter)
        self.home_window_layout.addWidget(self.home_title_label)
        # Create the current time label
        self.home_current_time_label = QLabel("<h3>Current Time: </h3>", alignment=Qt.AlignmentFlag.AlignCenter)
        self.home_window_layout.addWidget(self.home_current_time_label)
        # Create the current timezone label
        self.home_current_timezone_label = QLabel("<h3>Current Timezone: </h3>", alignment=Qt.AlignmentFlag.AlignCenter)
        self.home_window_layout.addWidget(self.home_current_timezone_label)
        # Add a stretch to the layout so the elements stay grouped
        self.home_window_layout.addStretch()
        self.stacked_widget.addWidget(self.home_window)

        # Create the View Timezones window (Index 1)
        self.view_timezones_window = QWidget(self)
        self.view_timezones_window_layout = QVBoxLayout(self.view_timezones_window)
        # Create the title label
        self.view_timezones_title_label = QLabel('<h1>View Timezones</h1>', alignment=Qt.AlignmentFlag.AlignCenter)
        self.view_timezones_window_layout.addWidget(self.view_timezones_title_label)
        # Add a stretch to the layout so the elements stay grouped
        self.view_timezones_window_layout.addStretch()
        self.stacked_widget.addWidget(self.view_timezones_window)

        # Create the Plan Trip window (Index 2)
        self.plan_trip_window = QWidget(self)
        self.plan_trip_window_layout = QVBoxLayout(self.plan_trip_window)
        # Create the title label
        self.plan_trip_title_label = QLabel('<h1>Plan Trip</h1>', alignment=Qt.AlignmentFlag.AlignCenter)
        self.plan_trip_window_layout.addWidget(self.plan_trip_title_label)
        # Add a stretch to the layout so the elements stay grouped
        self.plan_trip_window_layout.addStretch()
        self.stacked_widget.addWidget(self.plan_trip_window)

        # Set up the main window layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(toolbar)
        layout.addWidget(self.stacked_widget)

        self.show_home_window()
        
        # Start a timer to update the current time label every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_current_time)
        # PyQt's timer works with milliseconds, so 1000 milliseconds = 1 second
        self.timer.start(1000)

    def show_home_window(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_view_timezones_window(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_plan_trip_window(self):
        self.stacked_widget.setCurrentIndex(2)          
        
    def update_current_time(self):
        # Get the current time using pendulum
        current_time = pendulum.now().format("HH:mm A")

        # Update the current time label
        self.home_current_time_label.setText(f"<h3>Current Time: {current_time}</h3>")  

if __name__ == '__main__':
    app = QApplication([])
    main_window = Window()
    main_window.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
    main_window.show()
    sys.exit(app.exec())