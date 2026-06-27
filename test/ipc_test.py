from PySide6.QtCore import QCoreApplication, QByteArray
from PySide6.QtNetwork import QLocalSocket
import sys

# ========== 配置，改成你程序的管道名称 ==========
PIPE_NAME = "LittleCLock"

class MockThirdMod:
    def __init__(self):
        self.app = QCoreApplication(sys.argv)
        self.sock = QLocalSocket()
        self.sock.connected.connect(self.on_connected)
        self.sock.disconnected.connect(self.on_disconnected)
        self.sock.errorOccurred.connect(self.on_error)

    def connect_server(self):
        print(f"尝试连接管道: {PIPE_NAME}")
        self.sock.connectToServer(PIPE_NAME)

    def send_command(self, cmd: bytes):
        """组装标准数据包：outside: + 指令二进制"""
        packet = cmd
        ba = QByteArray(packet)
        self.sock.write(ba)
        self.sock.flush()
        print(f"已发送数据包 hex: {packet.hex()} | 原始: {packet}")

    def on_connected(self):
        print("✅ 成功连接IPC服务端，可发送指令")
        # 示例1：正常合法指令 show-window
        self.send_command(b"show-window\n")

        # 示例2：测试多余空格，服务端strip后可识别
        self.send_command(b"  show-window  \n")

        # 示例3：测试非法数据包
        self.send_command(b"giaogiaogiao!!!\n")

    def on_disconnected(self):
        print("❌ 与服务端管道断开连接")
        self.app.quit()

    def on_error(self, err):
        print(f"❌ 管道连接异常: {self.sock.errorString()}")
        self.app.quit()

    def run(self):
        self.connect_server()
        return self.app.exec()

if __name__ == "__main__":
    mock = MockThirdMod()
    mock.run()