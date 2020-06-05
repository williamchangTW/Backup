import sys
import os
from PyQt5.QtWidgets import *
    

class Console(QWidget):
    def __init__(self, name = 'Main'):
        super(Console,self).__init__()
        self.setWindowTitle(name)
        self.cwd = os.getcwd() 
        self.resize(300, 200)  

        # Test Button to new a frame
        self.btn_newWindow = QPushButton(self)
        self.btn_newWindow.setObjectName("btn_newWindow")
        self.btn_newWindow.setText("New Window")

        # Select Input File
        self.btn_chooseInputFile = QPushButton(self)  
        self.btn_chooseInputFile.setObjectName("btn_chooseInputFile")  
        self.btn_chooseInputFile.setText("Input CSV File")

        # Select Model Input
        self.btn_chooseModelFile = QPushButton(self)  
        self.btn_chooseModelFile.setObjectName("btn_chooseModelFile")  
        self.btn_chooseModelFile.setText("Input Model File")

        # Show connected devices
        self.btn_connectedDevices = QPushButton(self)
        self.btn_connectedDevices.setObjectName("btn_connectedDevices")
        self.btn_connectedDevices.setText("Show Connected Devices")
        
        # Execute the process
        self.btn_execute = QPushButton(self)  
        self.btn_execute.setObjectName("btn_execute")  
        self.btn_execute.setText("Execute")
        
        # 设置布局
        layout = QVBoxLayout()
        # Buttons 
        layout.addWidget(self.btn_chooseInputFile)
        layout.addWidget(self.btn_chooseModelFile)
        layout.addWidget(self.btn_connectedDevices)
        layout.addWidget(self.btn_execute)
        # test new window
        layout.addWidget(self.btn_newWindow)        

        # construct
        self.setLayout(layout)


        # 设置信号
        self.btn_chooseInputFile.clicked.connect(self.slot_btn_chooseInputFile)
        self.btn_chooseModelFile.clicked.connect(self.slot_btn_chooseModelFile)
        self.btn_connectedDevices.clicked.connect(self.slot_btn_connectedDevices)
        self.btn_execute.clicked.connect(self.slot_btn_execute)
	# test new window
        self.btn_newWindow.clicked.connect(self.slot_btn_newWindow)
    
    def slot_btn_newWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.title = "New Frame"
            self.top = 200
            self.left = 500
            self.width = 400
            self.height = 300
            self.setWindowTitle(self.title)
            self.setGeometry(self.left, self.width, self.height, self.top)		        

    def slot_btn_chooseInputFile(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,  
                                    "Select",  
                                    self.cwd, # 起始路径 
                                    "CSV Files (*.csv)")   # 设置文件扩展名过滤,用双分号间隔

        if fileName_choose == "":
            print("\nCancel")
            return

        print("\nFile Name:")
        print(fileName_choose)
        print("File Filter: ",filetype)
        global inputData
        inputData = fileName_choose
        
    def slot_btn_chooseModelFile(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,  
                                    "Select",  
                                    self.cwd, # 起始路径 
                                    "Python File(*.py)")   # 设置文件扩展名过滤,用双分号间隔

        if fileName_choose == "":
            print("\nCancel")
            return

        print("\nFile Name:")
        print(fileName_choose)
        print("File Filter: ",filetype)
        global inputModel
        inputModel = fileName_choose
    
    def slot_btn_connectedDevices(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,  
                                    "Select",  
                                    self.cwd, # 起始路径 
                                    "Python File(*.py)")   # 设置文件扩展名过滤,用双分号间隔

        if fileName_choose == "":
            print("\nCancel")
            return

        print("\nFile Name:")
        print(fileName_choose)
        print("File Filter: ",filetype)
        
    def slot_btn_execute(self):
        #cmd = "gnome-terminal -e 'bash -c \"ls *;exec b}ash\"'"
        #cmd = "gnome-terminal -e 'bash -c \"ls *; exec bash\"'"
        
        temp = inputModel
        command = '"/usr/bin/python3.6 ' + temp 
        cmd = "gnome-terminal -e 'bash -c " + command + ";exec bash\"'" 
        #cmd = "gnome-terminal -e '/usr/bin/python3.6 test.py'"
        
        os.system(cmd)
        #os.system("gnome-terminal -e 'bash -c \"ls *; exec bash\"'")


if __name__=="__main__":
    # Auto reboot
    inputData = ""
    inputModel = ""
    temp = os.getpid()
    with open("processpid.txt",  "w") as df:
        df.write(str(temp))
        df.close()
    # Turn on Console
    app = QApplication(sys.argv)
    console = Console('Console')
    console.show()
    sys.exit(app.exec_())

