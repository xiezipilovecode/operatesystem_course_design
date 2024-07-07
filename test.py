import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, \
                             QLabel, QLineEdit, QPushButton, QMessageBox

class LoginRegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 布局设置
        layout = QVBoxLayout()

        # 登录区域
        loginLayout = QHBoxLayout()
        loginLabel = QLabel('Username:')
        usernameInput = QLineEdit()
        loginLabel.setBuddy(usernameInput)

        loginLayout.addWidget(loginLabel)
        loginLayout.addWidget(usernameInput)

        passwordLabel = QLabel('Password:')
        passwordInput = QLineEdit()
        passwordInput.setEchoMode(QLineEdit.Password)
        passwordLabel.setBuddy(passwordInput)

        loginLayout.addWidget(passwordLabel)
        loginLayout.addWidget(passwordInput)

        loginButton = QPushButton('Login')
        loginButton.clicked.connect(self.login)
        loginLayout.addWidget(loginButton)

        # 注册区域
        registerLayout = QHBoxLayout()
        registerLabel = QLabel('Create Account:')
        registerInput = QLineEdit()
        registerLabel.setBuddy(registerInput)

        registerLayout.addWidget(registerLabel)
        registerLayout.addWidget(registerInput)

        registerButton = QPushButton('Register')
        registerButton.clicked.connect(self.register)
        registerLayout.addWidget(registerButton)

        # 组合布局
        layout.addLayout(loginLayout)
        layout.addLayout(registerLayout)

        # 设置窗口标题和布局
        self.setWindowTitle('Login & Register')
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 150)

    def login(self):
        # 这里应该添加登录逻辑
        username = self.findChild(QLineEdit, 'usernameInput').text()
        password = self.findChild(QLineEdit, 'passwordInput').text()
        # 模拟登录验证
        if username == 'admin' and password == 'admin':
            QMessageBox.information(self, 'Login', 'Login Successful!')
        else:
            QMessageBox.warning(self, 'Login', 'Invalid username or password!')

    def register(self):
        # 这里应该添加注册逻辑
        username = self.findChild(QLineEdit, 'registerInput').text()
        if username:  # 简单的非空检查
            QMessageBox.information(self, 'Register', 'Registration Successful!')
        else:
            QMessageBox.warning(self, 'Register', 'Please enter a username!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginRegisterWindow()
    ex.show()
    sys.exit(app.exec_())