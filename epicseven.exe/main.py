import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QGridLayout, QComboBox, QPushButton, QCheckBox, QTextEdit,QLineEdit,QLabel
from PyQt5.QtGui import QIcon
from daily import daily

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 创建主界面布局
        main_layout = QVBoxLayout()

        # 创建分页组件
        tab_widget = QTabWidget()
        tab_widget.addTab(self.create_page_one(), "epic seven")
        tab_widget.addTab(self.create_page_two(), "blue archive")

        # 添加分页组件到主界面
        main_layout.addWidget(tab_widget)

        self.setGeometry(600, 300, 450, 600)
        self.setLayout(main_layout)
        self.setWindowTitle("游戏脚本")
        self.setWindowIcon(QIcon('1.ico'))

    def create_page_one(self):
        # 创建分页1布局
        page_one_layout = QGridLayout()

        # 创建下拉框和按钮
        combo_box = QComboBox()
        combo_box.addItems(["夜神模拟器","mumu模拟器","雷神模拟器"])

        button = QPushButton("测试连接")
        button1= QPushButton("执行")

        # 创建多选框和按钮
        check_box_one = QCheckBox("日常")
        check_box_two = QCheckBox("商店刷书签")
        check_box_three = QCheckBox("远征(默认20次执行):")
        check_box_four = QCheckBox("左上")
        check_box_five = QCheckBox("右上")
        check_box_six = QCheckBox("下")

        #创建标签
        label=QLabel('数量:')
        label1=QLabel('运行显示:')

        #创建输入框
        qline=QLineEdit()
        qline.setPlaceholderText("10")

        # 创建显示框
        result_edit = QTextEdit()
        result_edit.setReadOnly(True)

        # 添加下拉框、按钮和显示框到分页1布局
        page_one_layout.addWidget(combo_box,0,0,1,3)
        page_one_layout.addWidget(button,0,4,1,1)
        page_one_layout.addWidget(check_box_one,1,0,1,2)
        page_one_layout.addWidget(label,2,2,1,1)
        page_one_layout.addWidget(qline,2,3,1,2)
        page_one_layout.addWidget(check_box_two,2,0,1,2)
        page_one_layout.addWidget(check_box_three,3,0,1,2)
        page_one_layout.addWidget(check_box_four,4,1,1,2)
        page_one_layout.addWidget(check_box_five,5,1,1,2)
        page_one_layout.addWidget(check_box_six,6,1,1,2)
        page_one_layout.addWidget(button1,7,4,1,1)
        page_one_layout.addWidget(label1,8,0,1,5)
        page_one_layout.addWidget(result_edit,9,0,1,5)

        # 为按钮添加点击事件处理函数
        button.clicked.connect(lambda: self.on_click(result_edit))
        button1.clicked.connect(self.on_click1)
        

        # 将分页1布局添加到QWidget中
        page_one = QWidget()
        page_one.setLayout(page_one_layout)

        return page_one

    def on_click(self,display_box):
        display_box.setText("1111")
        daily.daily()

    def on_click1():
        pass

    def create_page_two(self):
        # 创建分页2布局
        page_two_layout = QVBoxLayout()

        # 创建多选框和按钮
        check_box_one = QCheckBox("Checkbox 1")
        check_box_two = QCheckBox("Checkbox 2")
        check_box_three = QCheckBox("Checkbox 3")

        button = QPushButton("Get Result")

        # 创建显示框
        result_edit = QTextEdit()
        result_edit.setReadOnly(True)

        # 添加多选框、按钮和显示框到分页2布局
        page_two_layout.addWidget(check_box_one)
        page_two_layout.addWidget(check_box_two)
        page_two_layout.addWidget(check_box_three)
        page_two_layout.addWidget(button)
        page_two_layout.addWidget(result_edit)

        # 将分页2布局添加到QWidget中
        page_two = QWidget()
        page_two.setLayout(page_two_layout)

        return page_two

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
