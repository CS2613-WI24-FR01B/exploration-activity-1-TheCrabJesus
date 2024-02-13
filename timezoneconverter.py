import sys
import pendulum
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QStackedWidget, QLabel, QSizePolicy, QComboBox
from PyQt6.QtCore import Qt, QTimer, QSize
from PyQt6.QtGui import QIcon
WINDOW_SIZE = 500

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        # List of timezones
        file_name = 'timezones_utc.txt'
        with open(file_name, 'r') as file:
            timezone_list = file.readlines()
        
        # Set Application Title
        self.setWindowTitle('Timezone Converter')
        self.setStyleSheet("QMainWindow {background-color: rgb(40, 40, 40);}")
        
        # Create the toolbar
        toolbar = QToolBar(self)
        self.addToolBar(toolbar)
        
        # Add spacing between the toolbar buttons
        toolbar.setStyleSheet("QToolBar{spacing: 25px; background-color: rgb(53, 53, 53); padding: 5px 5px; border-radius: 5px}");
        
        # Add stretchable space on the left
        left_spacer = QWidget()
        left_spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        toolbar.addWidget(left_spacer)

        # Create Home button and add to toolbar
        home_button = QPushButton()
        home_button.setIcon(QIcon('Icons/home.png'))
        home_button.setIconSize(QSize(15, 15))
        home_button.setStyleSheet("""
            QPushButton {
                background-color: rgb(70, 129, 244);
                border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:pressed {
                background-color: rgb(60, 110, 208);
            }
        """)
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
        self.home_window.setStyleSheet('background-color: rgb(180, 180, 180); border-radius: 5px;')
        self.home_window_layout = QVBoxLayout(self.home_window)
        
        self.home_title_label = QLabel('<h1>Timezone Converter</h1>', alignment=Qt.AlignmentFlag.AlignCenter)
        self.home_window_layout.addWidget(self.home_title_label)
        
        self.home_current_time_label = QLabel("<h3>Current Time: </h3>", alignment=Qt.AlignmentFlag.AlignCenter)
        self.home_window_layout.addWidget(self.home_current_time_label)
        
        self.home_current_timezone_label = QLabel("<h3>Current Timezone: </h3>", alignment=Qt.AlignmentFlag.AlignCenter)
        self.home_window_layout.addWidget(self.home_current_timezone_label)
        
        self.home_window_layout.addStretch()
        self.stacked_widget.addWidget(self.home_window)

        # Create the View Timezones window (Index 1)
        self.view_timezones_window = QWidget(self)
        self.view_timezones_window.setStyleSheet('background-color: rgb(180, 180, 180); border-radius: 5px;')
        self.view_timezones_window_layout = QVBoxLayout(self.view_timezones_window)
        
        self.view_timezones_title_label = QLabel('<h1>View Timezones</h1>', alignment=Qt.AlignmentFlag.AlignCenter)
        self.view_timezones_window_layout.addWidget(self.view_timezones_title_label)
        
        chose_timezone_layout = QHBoxLayout()
        chose_timezone_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        choose_timezone_label = QLabel('<h4>Choose Timezone:</h4>')
        chose_timezone_layout.addWidget(choose_timezone_label)
        
        self.timezone_combobox = QComboBox()
        self.timezone_combobox.setStyleSheet('background-color: white;')
        
        for tz in timezone_list:
            self.timezone_combobox.addItem(tz)
            
        chose_timezone_layout.addWidget(self.timezone_combobox)
        
        self.view_timezones_window_layout.addLayout(chose_timezone_layout)
        
        self.timezones_current_time_label = QLabel("<h4>Current Local Time: </h4>", alignment=Qt.AlignmentFlag.AlignCenter)
        self.view_timezones_window_layout.addWidget(self.timezones_current_time_label)
        
        self.timezones_selected_time_label = QLabel("<h4>Local Time in </h4>", alignment=Qt.AlignmentFlag.AlignCenter)
        self.view_timezones_window_layout.addWidget(self.timezones_selected_time_label)
        
        self.view_timezones_window_layout.addStretch()
        self.stacked_widget.addWidget(self.view_timezones_window)

        # Create the Plan Trip window (Index 2)
        self.plan_trip_window = QWidget(self)
        self.plan_trip_window.setStyleSheet('background-color: rgb(180, 180, 180); border-radius: 5px;')
        
        self.plan_trip_window_layout = QVBoxLayout(self.plan_trip_window)
        self.plan_trip_title_label = QLabel('<h1>Plan Trip</h1>', alignment=Qt.AlignmentFlag.AlignCenter)
        self.plan_trip_window_layout.addWidget(self.plan_trip_title_label)
        
            # Start Timezone
        trip_start_timezone_layout = QHBoxLayout()
        trip_start_timezone_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        trip_start_timezone_label = QLabel("<h4>Start Timezone:</h4>")
        trip_start_timezone_layout.addWidget(trip_start_timezone_label)
        
        self.trip_start_timezone_combobox = QComboBox()
        self.trip_start_timezone_combobox.setStyleSheet('background-color: white;')
        
        for tz in timezone_list:
            self.trip_start_timezone_combobox.addItem(tz)
            
        trip_start_timezone_layout.addWidget(self.trip_start_timezone_combobox)
        self.plan_trip_window_layout.addLayout(trip_start_timezone_layout)
            # Start Time
        trip_start_time_layout = QHBoxLayout()
        trip_start_time_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
            # End Timezone
        trip_end_layout = QHBoxLayout()
        trip_end_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        trip_end_label = QLabel("<h4>Destination Timezone:</h4>")
        trip_end_layout.addWidget(trip_end_label)
        
        self.trip_end_combobox = QComboBox()
        self.trip_end_combobox.setStyleSheet('background-color: white;')
        
        for tz in timezone_list:
            self.trip_end_combobox.addItem(tz)
            
        trip_end_layout.addWidget(self.trip_end_combobox)
        self.plan_trip_window_layout.addLayout(trip_end_layout)
        # Trip Duration
        
        # Local Time at Arrival
        
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
        self.current_time_timer = QTimer(self)
        self.current_time_timer.timeout.connect(self.update_current_time)
        # PyQt's timer works with milliseconds, so 1000 milliseconds = 1 second
        self.current_time_timer.start(1000)
        
        # Update the current index of the combobox
        self.timezone_combobox.currentIndexChanged.connect(self.update_selected_timezone)
        
        # Start a timer to update the selected timezone label every second
        self.selected_timezone_timer = QTimer(self)
        self.selected_timezone_timer.timeout.connect(self.update_selected_timezone)
        self.selected_timezone_timer.start(1000)

    def show_home_window(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_view_timezones_window(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_plan_trip_window(self):
        self.stacked_widget.setCurrentIndex(2)          
        
    def update_current_time(self):
        # Get the current time using pendulum
        current_time = pendulum.now().format("HH:mm A")
        
        # Get the current local timezone using pendulum
        local_timezone = pendulum.now().timezone.name

        # Update the current time label
        self.home_current_time_label.setText(f"<h3>Current Time: {current_time}</h3>")
        
        # Update the current timezone labels
        self.home_current_timezone_label.setText(f"<h3>Current Timezone: {local_timezone}</h3>")
        self.timezones_current_time_label.setText(f"<h4>Current Local Time: {current_time}</h4>")
        
    def update_selected_timezone(self):
        file_name = 'timezones_names.txt'
        with open(file_name, 'r') as file:
            timezone_names = file.readlines()
            
        selected_index = self.timezone_combobox.currentIndex()
        selected_timezone = timezone_names[selected_index].strip()
        current_local_time = pendulum.now(selected_timezone).format("HH:mm A")
        self.timezones_selected_time_label.setText(f"<h4>Local Time in {selected_timezone}: {current_local_time}</h4>")

if __name__ == '__main__':
    app = QApplication([])
    main_window = Window()
    main_window.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
    main_window.show()
    sys.exit(app.exec())
    