from typing import Callable

from PySide6.QtCore import QObject, Slot, QCoreApplication, Signal
from PySide6.QtNetwork import QLocalServer, QLocalSocket

from src.logger import Logger

PIPE_NAME = "LittleClock"


class IPCServer(QObject):
    '''进程通信接收类'''
    
    _signal = Signal(bytes, bytes)

    def __init__(self):
        super().__init__()
        self._init_server()
        Logger.info("IPC管道服务启动，管道名:{}", PIPE_NAME)


    def _init_server(self):
        '''服务端初始化'''
        self._server = QLocalServer()
        QLocalServer.removeServer(PIPE_NAME)
        self._server.newConnection.connect(self.on_connect)
        self._server.listen(PIPE_NAME)

    
    @Slot()
    def on_connect(self):
        '''有客户端连接时触发'''
        client_sock = self._server.nextPendingConnection()
        client_sock.readyRead.connect(lambda sock = client_sock: self.on_received(sock))
        client_sock.disconnected.connect(lambda sock = client_sock: sock.deleteLater())
        Logger.info("有外部进程与本进程建立连接")


    @Slot(QLocalSocket)
    def on_received(self, sock:QLocalSocket):
        '''读取外部进程的信号'''
        sig_bytes_list = sock.readAll().data().split(b"\n")
        for sig in sig_bytes_list:      #要求外部按照换行符拆分连续信号（否则会被合并成一串信号）
            if not sig:
                return
            Logger.info("来自外部进程的信息, hex：{}", sig.hex())
            self._signal.emit(self._property(sig), str(None))



    def connect(self, func):
        '''建立信号连接对象'''
        self._signal.connect(func)

        
    def _property(self, sig:bytes) -> bytes:
        '''修饰外部信号'''
        return b"outside:" + sig.strip()

    def shutdown(self):
        '''关闭服务端'''
        self._server.close()
        Logger.info("IPC管道服务已关闭")
        

class IPCSocket:
    '''进程通信发送类（一次性）'''
    def __init__(self):
        self._socket = QLocalSocket()
        self._socket.connectToServer(PIPE_NAME)
        self._socket.waitForConnected()
        Logger.info("IPC客户端管道已创建，连接至：{}", PIPE_NAME)

    def send(self):
        '''发送信息'''
        self._socket.write(b"show-window")
        self._socket.flush()
        Logger.info("多开进程：向主进程发送弹出窗口信息")

    def shutdown(self):
        '''关闭客户端'''
        self._socket.disconnectFromServer()
        self._socket.waitForDisconnected()
        Logger.info("IPC客户端管道已关闭")



if __name__ == "__main__":
    app = QCoreApplication([])
    #ipc_server = IPCServer()
    while True:
        ipc_socket = IPCSocket()
    app.exec()