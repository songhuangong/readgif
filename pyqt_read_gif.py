import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
import os
import shutil
from datetime import datetime


class LoadingGifWin(QWidget):
    def __init__(self, parent=None):
        super(LoadingGifWin, self).__init__(parent)
        self.btn_del = QPushButton('删除')
        self.label = QLabel('', self)
        self.btn_next = QPushButton('下一张')
        self.btn_pre = QPushButton('上一张')
        self.btn_save = QPushButton('save')
        self.btn_chooseDir = QPushButton('选择文件夹')

        self.layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        self.setFixedSize(700, 900)
        # self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)
        self.movie = None
        self.now_path = ""
        self.ui_set()
        # 关键变量初始化
        self.root_path = r'F:\娱乐\图'
        self.files = []
        self.file_num = 0
        self.set()

    def ui_set(self):
        self.layout.addWidget(self.btn_del)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.btn_pre)
        self.layout.addWidget(self.btn_next)
        # self.layout.addChildLayout(self.h_layout)
        self.layout.addWidget(self.btn_save)
        self.layout.addWidget(self.btn_chooseDir)
        self.setLayout(self.layout)

    def set(self):
        # 链接槽
        self.btn_next.clicked.connect(self.next_onclick)
        self.btn_pre.clicked.connect(self.pre_onclick)
        self.btn_save.clicked.connect(self.onclick_save)
        self.btn_chooseDir.clicked.connect(self.slot_btn_choose_dir)
        self.btn_del.clicked.connect(self.slot_btn_del)
        self.read_file2list()

    def slot_btn_choose_dir(self):
        dir_choose = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      self.root_path)  # 起始路径

        if dir_choose == "":
            print("\n取消选择")
            return
        print("\n你选择的文件夹为:")
        print(dir_choose)
        self.root_path = dir_choose
        self.read_file2list()

    def slot_btn_del(self):
        """
        基本实现
        :return:
        """
        try:
            temp = self.now_path
            self.next_onclick()
            os.remove(temp)
        except Exception as e:
            print(e)

    def start(self, gif_path):
        self.now_path = gif_path
        self.movie = QMovie(gif_path)
        self.label.setMovie(self.movie)
        self.movie.start()

    # def read_file(self):
    #     for file in os.listdir(self.root_path):
    #         if file.endswith(".gif"):
    #             yield file

    def read_file2list(self):
        self.file_num = 0
        self.files.clear()
        for file in os.listdir(self.root_path):
            if file.endswith(".gif"):
                self.files.append(file)
            elif file.endswith(".jpg"):
                j2g = file[0:-4] + '.gif'
                old = os.path.join(self.root_path, file)
                new = os.path.join(self.root_path, j2g)
                shutil.move(old, new)
                self.files.append(j2g)
        self.show_pic(self.file_num)

    def next_onclick(self):
        self.file_num += 1
        self.show_pic(self.file_num)

    def pre_onclick(self):
        self.file_num -= 1
        self.show_pic(self.file_num)

    def onclick_save(self):
        d = datetime.utcnow().strftime('%Y%m%d_%H%M%S%f')[:-3]
        new_name = os.path.join(r'F:\娱乐\图', d) + '.gif'
        print(self.now_path, new_name)
        shutil.copyfile(self.now_path, new_name)

    def show_pic(self, num):
        try:
            print(num)
            f = os.path.join(self.root_path, self.files[num])
            self.start(f)
        except Exception as e:
            self.file_num = 0
            print('重新播放', e)
            try:
                self.start(f)
            except Exception as e:
                pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loadingGitWin = LoadingGifWin()
    loadingGitWin.show()
    sys.exit(app.exec_())

