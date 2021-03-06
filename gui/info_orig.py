import sys
import os
from PyQt5 import QtGui
import info_collector
import subprocess
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout, QTextEdit
from PyQt5.QtGui import QColor
from utils.config import Config

class Info(QWidget):


    def __init__(self):
        super(Info, self).__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(800, 500)
        self.setWindowTitle('InfoCollector by Florian Gemperle')

        # Buttons
        self.btn_start = QPushButton('Start Run', self)
        self.btn_start.clicked.connect(self.start_run)
        self.btn_start.resize(self.btn_start.sizeHint())

        btn_config = QPushButton('Show Config', self)
        btn_config.clicked.connect(self.output)
        btn_config.resize(btn_config.sizeHint())

        btn_b_log = QPushButton('Show InfoCollector Log', self)
        btn_b_log.clicked.connect(self.show_infolog)
        btn_b_log.resize(btn_b_log.sizeHint())

        btn_quit = QPushButton('Quit', self)
        btn_quit.clicked.connect(self.close)
        # btn_quit.clicked.connect(self.update_status)
        btn_quit.resize(btn_quit.sizeHint())

        self.btn_abort = QPushButton('Abort Run', self)
        self.btn_abort.clicked.connect(self.abort_run)
        self.btn_abort.resize(self.btn_abort.sizeHint())
        self.btn_abort.setEnabled(False)

        # Text Area
        self.output_area = QTextEdit(self)
        self.output_area.setFixedSize(750, 375)
        self.output_area.setReadOnly(True)

        # Status
        self.txt_total = QLabel('Total: 0', self)
        self.txt_success = QLabel('Success: 0', self)
        self.txt_failed = QLabel('Failed: 0', self)
        self.txt_duplicates = QLabel('Duplicates: 0', self)

        self.txt_total.setObjectName('txt_total')
        self.txt_success.setObjectName('txt_success')
        self.txt_failed.setObjectName('txt_failed')
        self.txt_duplicates.setObjectName('txt_duplicates')

        self.txt_total.setStyleSheet('color: black; font-size: 14px; font: bold')
        self.txt_success.setStyleSheet('color: green; font-size: 14px; font: bold')
        self.txt_failed.setStyleSheet('color: red; font-size: 14px; font: bold')
        self.txt_duplicates.setStyleSheet('color: blue; font-size: 14px; font: bold')

        # Layout
        grid = QGridLayout(self)
        grid_status = QGridLayout()
        grid_output = QGridLayout()
        grid_buttons = QGridLayout()

        grid.addLayout(grid_status, 0, 0)
        grid.addLayout(grid_output, 1, 0)
        grid.addLayout(grid_buttons, 2, 0)

        grid_status.addWidget(self.btn_start, 0, 0)
        grid_status.addWidget(self.txt_total, 0, 1)
        grid_status.addWidget(self.txt_success, 0, 2)
        grid_status.addWidget(self.txt_failed, 0, 3)
        grid_status.addWidget(self.txt_duplicates, 0, 4)

        grid_output.addWidget(self.output_area, 0, 0)

        grid_buttons.addWidget(btn_config, 3, 0)
        grid_buttons.addWidget(btn_b_log, 3, 1)
        grid_buttons.addWidget(self.btn_abort, 3, 2)
        grid_buttons.addWidget(btn_quit, 3, 3)
        self.setLayout(grid)

    def show_config(self):
        program = 'C:/Program Files (x86)/Notepad++/notepad++.exe'
        file = 'C:/BulkChanger/config.ini'
        subprocess.Popen([program, file])

    def show_infolog(self):
        program = 'C:/Program Files (x86)/Notepad++/notepad++.exe'
        file = 'C:/BulkChanger/infocollector.log'
        subprocess.Popen([program, file])

    def abort_run(self):
        # logging.warning('execution: aborted by user')
        self.btn_abort.setEnabled(False)
        self.btn_start.setEnabled(True)
        self.output_append('black', 'RUN ABORTED')

    def start_run(self):
        # logging.info('execution: run started by user')
        info_collector.start_info()
        self.btn_start.setEnabled(False)
        self.btn_abort.setEnabled(True)
        self.output_append('black', 'START RUN')

    def update_status(self, total, success, failed, duplicates):
        self.txt_total.setText('Total: ' + str(total))
        self.txt_success.setText('Success: ' + str(success))
        self.txt_failed.setText('Failed: ' + str(failed))
        self.txt_duplicates.setText('Duplicates: ' + str(duplicates))

    def output(self):
        self.output_append('red', 'Mein Name ist Eugen')

    def output_append(self, color, text):
        if color.upper() == 'RED':
            self.output_area.setTextColor(QColor(255, 0, 0))
        elif color.upper() == 'GREEN':
            self.output_area.setTextColor(QColor(0, 128, 0))
        elif color.upper() == 'BLUE':
            self.output_area.setTextColor(QColor(0, 0, 250))
        else:
            self.output_area.setTextColor(QColor(0, 0, 0))
        self.output_area.append(text)



