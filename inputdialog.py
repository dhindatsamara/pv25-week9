import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QInputDialog, QMessageBox
)
from PyQt5.QtGui import QIntValidator


class InputForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Dialog Input")
        self.setFixedSize(400, 150)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Full Name")
        self.name_btn = QPushButton("Get Name")
        self.name_btn.clicked.connect(self.get_name_dialog)

        name_layout = QHBoxLayout()
        name_layout.addWidget(self.name_input)
        name_layout.addWidget(self.name_btn)

        self.language_input = QLineEdit()
        self.language_input.setPlaceholderText("Favorite Programming Language")
        self.language_btn = QPushButton("Get Language")
        self.language_btn.clicked.connect(self.get_language_dialog)

        language_layout = QHBoxLayout()
        language_layout.addWidget(self.language_input)
        language_layout.addWidget(self.language_btn)

        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Age")
        self.age_input.setValidator(QIntValidator(0, 120))  
        self.age_btn = QPushButton("Get Age")
        self.age_btn.clicked.connect(self.get_age_dialog)

        age_layout = QHBoxLayout()
        age_layout.addWidget(self.age_input)
        age_layout.addWidget(self.age_btn)

        self.show_result_button = QPushButton("Show Result")
        self.show_result_button.clicked.connect(self.show_result)

        layout = QVBoxLayout()
        layout.addLayout(name_layout)
        layout.addLayout(language_layout)
        layout.addLayout(age_layout)
        layout.addStretch()
        layout.addWidget(self.show_result_button)

        self.setLayout(layout)

        self.language_map = {
            "c": "C",
            "c++": "C++",
            "java": "Java",
            "python": "Python"
        }

    def get_name_dialog(self):
        text, ok = QInputDialog.getText(self, "Input Name", "Input your name:")
        if ok and text:
            self.name_input.setText(text)

    def get_language_dialog(self):
        options = ["C", "C++", "Java", "Python"]
        item, ok = QInputDialog.getItem(self, "Input Language", "Choose your favorite programming language:", options, editable=False)
        if ok and item:
            self.language_input.setText(item)

    def get_age_dialog(self):
        age, ok = QInputDialog.getInt(self, "Input Age", "Input your age:", min=0, max=120)
        if ok:
            self.age_input.setText(str(age))

    def show_result(self):
        nama = self.name_input.text().strip()
        bahasa = self.language_input.text().strip().lower()
        usia_text = self.age_input.text().strip()

        if not nama or not bahasa or not usia_text:
            QMessageBox.warning(self, "Warning", "Please complete all fields first.")
            return

        if bahasa in self.language_map:
            bahasa = self.language_map[bahasa]
            self.language_input.setText(bahasa)
        else:
            QMessageBox.critical(self, "Error", "Programming language must be C, C++, Java, or Python.")
            return

        try:
            usia = int(usia_text)
        except ValueError:
            QMessageBox.critical(self, "Error", "Age must be a number between 0 and 120.")
            return

        QMessageBox.information(
            self,
            "Result",
            f"Name: {nama}\nFavorite Programming Language: {bahasa}\nAge: {usia}"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InputForm()
    window.show()
    sys.exit(app.exec_())
