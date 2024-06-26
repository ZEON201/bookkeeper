from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton,
                               QLineEdit, QComboBox, QTableWidget, QAbstractItemView)
from PySide6.QtWidgets import QHeaderView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.controller = any
        self.setWindowTitle("Программа для ведения бюджета")
        self.setFixedSize(300, 350)

        self.layout = QVBoxLayout()

        self.budget_monthly = QLabel('Бюджет на месяц: ')
        self.budget_weekly = QLabel('Бюджет на неделю: ')
        self.budget_daily = QLabel('Бюджет на день: ')
        self.layout.addWidget(self.budget_monthly)
        self.edit_budget_monthly = QLineEdit()
        self.layout.addWidget(self.edit_budget_monthly)
        self.layout.addWidget(self.budget_weekly)
        self.edit_budget_weekly = QLineEdit()
        self.layout.addWidget(self.edit_budget_weekly)
        self.layout.addWidget(self.budget_daily)
        self.edit_budget_daily = QLineEdit()
        self.layout.addWidget(self.edit_budget_daily)

        expenses_table = QTableWidget(4, 20)

        expenses_table.setColumnCount(4)
        expenses_table.setRowCount(20)
        expenses_table.setHorizontalHeaderLabels(
            "Дата Сумма Категория Комментарий".split())

        header = expenses_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.Stretch)

        expenses_table.setEditTriggers(
            QAbstractItemView.NoEditTriggers)
        expenses_table.verticalHeader().hide()

        self.layout.addWidget(expenses_table)

        self.budget_button = QPushButton('Задать бюджет')
        self.layout.addWidget(self.budget_button)
        self.budget_button.clicked.connect(self.on_budget_button_click)

        self.category = QComboBox(self)
        self.layout.addWidget(QLabel('Выберите категорию расхода:'))
        self.layout.addWidget(self.category)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)

    def set_controller(self, controller):
        self.controller = controller

    def refresh_budgets(self):
        bdgt = self.controller.read('Budget')
        self.budget_monthly.setText('Бюджет на месяц: ' + str(bdgt[0]))
        self.budget_weekly.setText('Бюджет на неделю: ' + str(bdgt[1]))
        self.budget_daily.setText('Бюджет на день: ' + str(bdgt[2]))

    def on_budget_button_click(self):
        self.controller.update('Budget', {'monthly': str(self.edit_budget_monthly.text()),
                                          'weekly': str(self.edit_budget_weekly.text()),
                                          'daily': str(self.edit_budget_daily.text())})
        self.refresh_budgets()

    def refresh_categories(self):
        cats = self.controller.read('Category')
        self.category.addItems(cats)