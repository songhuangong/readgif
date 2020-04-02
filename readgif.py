import pyglet
import os


class ReadGif:
    def __init__(self):
        pass

    def read(self,ag_file):
        self.animation = pyglet.resource.animation(ag_file)
        print(len(self.animation.frames)) # gif的帧数
        self.sprite = pyglet.sprite.Sprite(self.animation)
        # 创建一个窗口并将其设置为图像大小
        self.win = pyglet.window.Window(width=self.sprite.width, height=self.sprite.height)
        self.cnt = len(self.animation.frames)
        self.num = len(self.animation.frames)


        @self.win.event
        def on_draw():
            self.win.clear()
            self.sprite.draw()          # 播放一帧
            # print(len(self.sprite))
            if self.cnt == 0:
                print('播放一次完成')
                self.cnt = self.num
            else:
                self.cnt -= 1

    def run(self):
        pyglet.app.run()

    def exit(self):
        pyglet.app.exit()


r = ReadGif()

# path = r'F:\娱乐\图'
path = r'F:\娱乐\福利GIF压缩文件'
# 由于图片所在的目录不在当前目录，因此我们需要告诉pyglet去哪里找到它们：
pyglet.resource.path=[path]
pyglet.resource.reindex()

for file in os.listdir(path):
    if file.endswith(".gif"):
        r.read(file)
        r.run()
        print('---------')
