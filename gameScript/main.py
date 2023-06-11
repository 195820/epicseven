import sys
import time
import threading
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QGridLayout, QComboBox, QPushButton, QCheckBox, QTextEdit,QLineEdit,QLabel
from PyQt5.QtGui import QIcon
from connectionTest import connectionTest
import myThread
import PyQt5.QtWidgets

class Communicate(QObject):
    update_signal = pyqtSignal(str)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        #多线程
        self.allThreads=[]

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

        #子线程信号接收显示
        self.comm = Communicate()
        self.comm.update_signal.connect(self.update_text_edit)

    def update_text_edit(self, text):
        # update the GUI in the main thread
        #获取分页1
        for child in self.children():
            if isinstance(child, QTabWidget):
                tab_widget = child
                break
        page1 = tab_widget.widget(0)
        display_box=page1.findChildren(QTextEdit)[0]
        display_box.setText(text)

    def create_page_one(self):
        # 创建分页1布局
        page_one_layout = QGridLayout()

        # 创建下拉框和按钮
        combo_box = QComboBox()
        combo_box.addItems(["夜神模拟器","mumu模拟器","雷电模拟器","蓝叠模拟器"])
        combo_box_one = QComboBox()
        combo_box_one.addItems(["1","2","3","4"])

        button = QPushButton("测试连接")
        button_one= QPushButton("执行")
        button_two= QPushButton("停止")

        # 创建多选框和按钮
        check_box_one = QCheckBox("日常")
        check_box_two = QCheckBox("商店刷书签")
        check_box_three = QCheckBox("远征(默认20次执行):")
        check_box_four = QCheckBox("左上")
        check_box_five = QCheckBox("右上")
        check_box_six = QCheckBox("下")

        #创建标签
        label=QLabel('书签数量:')
        label1=QLabel('运行显示:')
        label2=QLabel('多开(仅夜神):')
        label3=QLabel('模拟器类型:')

        #创建输入框
        qline=QLineEdit()
        qline.setPlaceholderText("10")

        # 创建显示框
        result_edit = QTextEdit()
        result_edit.setReadOnly(True)

        # 添加下拉框、按钮和显示框到分页1布局
        page_one_layout.addWidget(label3,0,0,1,1)
        page_one_layout.addWidget(combo_box,0,1,1,2)
        page_one_layout.addWidget(label2,0,3,1,1)
        page_one_layout.addWidget(combo_box_one,0,4,1,1)
        page_one_layout.addWidget(check_box_one,1,0,1,2)
        page_one_layout.addWidget(label,2,2,1,1)
        page_one_layout.addWidget(qline,2,3,1,1)
        page_one_layout.addWidget(check_box_two,2,0,1,2)
        page_one_layout.addWidget(check_box_three,3,0,1,2)
        page_one_layout.addWidget(check_box_four,4,1,1,2)
        page_one_layout.addWidget(check_box_five,5,1,1,2)
        page_one_layout.addWidget(check_box_six,6,1,1,2)
        page_one_layout.addWidget(button,7,2,1,1)
        page_one_layout.addWidget(button_one,7,3,1,1)
        page_one_layout.addWidget(button_two,7,4,1,1)
        page_one_layout.addWidget(label1,8,0,1,5)
        page_one_layout.addWidget(result_edit,9,0,1,5)

        # 为按钮添加点击事件处理函数
        button.clicked.connect(lambda: self.on_click(combo_box,combo_box_one,result_edit))
        button_one.clicked.connect(self.on_click_one)
        button_two.clicked.connect(self.on_click_two)

        # 将分页1布局添加到QWidget中
        page_one = QWidget()
        page_one.setLayout(page_one_layout)

        return page_one

    #测试连接
    def on_click(self,name,num,display_box):
        name=name.currentText()
        num=int(num.currentText())
        a=connectionTest.connectionTest()
        a.test(name,num,display_box)


        for child in self.children():
            if isinstance(child, QTabWidget):
                tab_widget = child
                break
        page1 = tab_widget.widget(0)
        print(self.checkbox())
        #daily.daily()

    #脚本执行
    
    def on_click_one(self):
        #获取状态和连接
        status=self.checkbox()
        display_box=status[-1]
        device=status[-2]
        list=[device,display_box]
        #按钮判定
        if status[2]:   
            thread_one=myThread.MyThread("daily1",list)
            self.allThreads.append(thread_one)
            thread_one.start()
        elif status[4]:
            if status[3]=="":
                num=10
            num=int(status[3]) 
            if num<=0 :
                num=10
            list.append(num)
            thread_one=myThread.MyThread("key1",list)
            self.allThreads.append(thread_one)
            thread_one.start()    
        elif status[5]:
            list.extend([status[6],status[7],status[8]])
            thread_one=myThread.MyThread("expedition1",list)
            self.allThreads.append(thread_one)
            thread_one.start()    
        else :
            display_box.setText("未勾选执行操作")
        
    
    #停止执行
    def on_click_two(self):
        for t in self.allThreads:
            time.sleep(1) 
            t.raise_exception() 
            t.join() 

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
    
    #重新检测所有框的状态和内容
    def checkbox(self):
        #获取分页1
        for child in self.children():
            if isinstance(child, QTabWidget):
                tab_widget = child
                break
        page1 = tab_widget.widget(0)
        display_box=page1.findChildren(QTextEdit)[0]
        state=self.get_widget_values(page1)
        print(state)
        #获取device
        num=int(state[1])
        a=connectionTest.connectionTest()
        device=a.connection(state[0],num,display_box)
        state.append(device)
        #获取显示框，在子线程中使用
        state.append(self.comm)
        return state

    #遍历获取组件值
    def get_widget_values(self,widget):
        widget_list = []
        if isinstance(widget,PyQt5.QtWidgets.QLineEdit):
            widget_list.append(widget.text())
        elif isinstance(widget,PyQt5.QtWidgets.QComboBox):
            widget_list.append(widget.currentText())
        elif isinstance(widget,PyQt5.QtWidgets.QCheckBox):
            widget_list.append(widget.isChecked())
        elif isinstance(widget,PyQt5.QtWidgets.QRadioButton):
            widget_list.append(widget.isChecked())
        elif isinstance(widget,PyQt5.QtWidgets.QSpinBox) or isinstance(widget,PyQt5.QtWidgets.QDoubleSpinBox):
            widget_list.append(widget.value())

        for child in widget.children():
            if isinstance(child,PyQt5.QtWidgets.QWidget):
                widget_list.extend(self.get_widget_values(child))

        return widget_list

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
