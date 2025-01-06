# Copyright (c) 2025 Rafael Schmetcka <rafael.schmetcka@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import struct
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from templates.tela_recebendo_imagem import Ui_Recebendo_Imagem
import socket
import threading
from cryptography.fernet import Fernet
from PIL import Image
import io
import time


class MouseTrackingLabel(QLabel):
    mouse_position_signal = Signal(int, int)  # Sinal para transmitir as coordenadas (x, y)
    mouse_click_signal = Signal(int, int, str)
    key_press_signal = Signal(int, str)
    key_release_signal = Signal(int, str)

    def __init__(self, parent=None):
        super(MouseTrackingLabel, self).__init__(parent)
        self.setMouseTracking(True)  # Ativa o rastreamento do mouse
        # self.setFocusPolicy(Qt.StrongFocus) # Permite que o widget capture eventos de teclado

    def enterEvent(self, event):
        """Captura o foco quando o mouse entra na label."""
        self.setFocus()
        super(MouseTrackingLabel, self).enterEvent(event)

    def leaveEvent(self, event):
        """Libera o foco quando o mouse sai da label."""
        self.clearFocus()
        super(MouseTrackingLabel, self).leaveEvent(event)

    def mouseMoveEvent(self, event):
        # Captura a posição do mouse e emite o sinal
        x, y = event.x(), event.y()
        self.mouse_position_signal.emit(x, y)
        super(MouseTrackingLabel, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):
        # Captura a posição do clique e emite o sinal com tipo de clique 'press'
        x, y = event.x(), event.y()
        if event.button() == Qt.LeftButton:
            self.mouse_click_signal.emit(x, y, "press")
        elif event.button() == Qt.RightButton:
            self.mouse_click_signal.emit(x, y, "right_press")
        super(MouseTrackingLabel, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        # Captura a posição do clique e emite o sinal com tipo de clique 'release'
        x, y = event.x(), event.y()
        if event.button() == Qt.LeftButton:
            self.mouse_click_signal.emit(x, y, "release")
        elif event.button() == Qt.RightButton:
            self.mouse_click_signal.emit(x, y, "right_release")
        super(MouseTrackingLabel, self).mouseReleaseEvent(event)

    def mouseDoubleClickEvent(self, event):
        # Detecta o clique duplo e emite um sinal
        x, y = event.x(), event.y()
        self.mouse_click_signal.emit(x, y, "double_click")
        super(MouseTrackingLabel, self).mouseDoubleClickEvent(event)

    def keyPressEvent(self, event):
        if isinstance(event, QKeyEvent):
            vk_code = self.get_vk_code(event.key())  # Converte para VK code
            self.key_press_signal.emit(vk_code, "press")

    def keyReleaseEvent(self, event):
        if isinstance(event, QKeyEvent):
            vk_code = self.get_vk_code(event.key())
            self.key_release_signal.emit(vk_code, "release")

    def get_vk_code(self, qt_key):
        """Mapeia QKeyEvent key_code para Virtual-Key Codes (VK codes) do Windows."""
        qt_to_vk_map = {
            Qt.Key_Backspace: 0x08,  # VK_BACK
            Qt.Key_Return: 0x0D,  # VK_RETURN (Enter)
            Qt.Key_Enter: 0x0D,
            Qt.Key_Shift: 0x10,  # VK_SHIFT
            Qt.Key_Control: 0x11,  # VK_CONTROL
            Qt.Key_Alt: 0x12,  # VK_MENU
            Qt.Key_CapsLock: 0x14,  # VK_CAPITAL
            Qt.Key_Escape: 0x1B,  # VK_ESCAPE
            Qt.Key_Space: 0x20,  # VK_SPACE
            Qt.Key_Left: 0x25,  # VK_LEFT
            Qt.Key_Up: 0x26,  # VK_UP
            Qt.Key_Right: 0x27,  # VK_RIGHT
            Qt.Key_Down: 0x28,  # VK_DOWN
            Qt.Key_Exclam: 0x31,  # Shift + 1 = !
            Qt.Key_At: 0x32,  # Shift + 2 = @
            Qt.Key_NumberSign: 0x33,  # Shift + 3 = #
            Qt.Key_Dollar: 0x34,  # Shift + 4 = $
            Qt.Key_Percent: 0x35,  # Shift + 5 = %
            Qt.Key_AsciiCircum: 0x36,  # Shift + 6 = ^
            Qt.Key_Ampersand: 0x37,  # Shift + 7 = &
            Qt.Key_Asterisk: 0x38,  # Shift + 8 = *
            Qt.Key_ParenLeft: 0x39,  # Shift + 9 = (
            Qt.Key_ParenRight: 0x30,  # Shift + 0 = )
            Qt.Key_Minus: 0xBD,  # VK_OEM_MINUS (-)
            Qt.Key_Equal: 0xBB,  # VK_OEM_PLUS (=)
            Qt.Key_Plus: 0xBB,  # Shift + = = +
            Qt.Key_Period: 0xBE,  # VK_OEM_PERIOD (Ponto .)
            Qt.Key_Comma: 0xBC,  # VK_OEM_COMMA (Vírgula ,)
            Qt.Key_Semicolon: 0xBA,  # VK_OEM_1 (Ponto e vírgula ;)
            Qt.Key_Colon: 0xBA,  # Shift + ; = :
            Qt.Key_Slash: 0xBF,  # VK_OEM_2 (Barra /)
            Qt.Key_Question: 0xBF,  # Shift + / = ?
            Qt.Key_Backslash: 0xDC,  # VK_OEM_5 (Barra invertida \)
            Qt.Key_Bar: 0xDC,  # Shift + \ = |
            Qt.Key_QuoteLeft: 0xC0,  # VK_OEM_3 (Acento grave `)
            Qt.Key_AsciiTilde: 0xC0,  # Shift + ` = ~
            Qt.Key_Apostrophe: 0xDE,  # VK_OEM_7 (Aspas simples ')
            Qt.Key_QuoteDbl: 0xDE,  # Shift + ' = "
            Qt.Key_BraceLeft: 0xDB,  # VK_OEM_4 (Chave esquerda {)
            Qt.Key_BraceRight: 0xDD,  # VK_OEM_6 (Chave direita })
            Qt.Key_BracketLeft: 0xDB,  # VK_OEM_4 (Colchete esquerdo [)
            Qt.Key_BracketRight: 0xDD,  # VK_OEM_6 (Colchete direito ])
        }
        # Retorna o VK code mapeado ou o próprio código caso seja uma tecla regular
        return qt_to_vk_map.get(qt_key, qt_key)

class Recebendo_Imagem(QMainWindow):

    def __init__(self, HOST, senha,  *args, **argvs):
        super(Recebendo_Imagem, self).__init__(*args, **argvs)
        self.ui = Ui_Recebendo_Imagem()
        self.ui.setupUi(self)
        self.host = HOST
        self.senha = senha
        self.setWindowTitle(f"Ajudesk - Acessando {self.host}")
        self.setWindowIcon(QIcon(":Icone/icon.ico"))
        self.ui.textEdit.setReadOnly(True)
        self.ui.label_tela.setScaledContents(True)
        # Mantém as configurações de layout da label original
        original_label = self.ui.label_tela

        # Substitui QLabel por MouseTrackingLabel, mantendo o layout e o redimensionamento
        self.ui.label_tela = MouseTrackingLabel(self)
        self.ui.label_tela.setGeometry(original_label.geometry())
        self.ui.label_tela.setScaledContents(True)

        # Conectando os sinais de movimento e clique
        self.ui.label_tela.mouse_position_signal.connect(self.on_mouse_move)
        self.ui.label_tela.mouse_click_signal.connect(self.on_mouse_click)
        self.ui.label_tela.key_press_signal.connect(self.on_key_event)
        self.ui.label_tela.key_release_signal.connect(self.on_key_event)

        # Insere a nova label no layout da interface
        layout = original_label.parentWidget().layout()
        layout.replaceWidget(original_label, self.ui.label_tela)
        original_label.deleteLater()  # Remove a QLabel antiga

        self.flag_fechar_thread = False

        self.ui.btn_enviar.clicked.connect(self.enviar_comando)
        self.ui.btn_encerrar.clicked.connect(self.encerrar)

        self.ui.lineEdit_comando.returnPressed.connect(self.enviar_comando)

        self.ui.checkBox.stateChanged.connect(self.exec_mostrar_comandos)

        self.ui.checkBox.setChecked(True)

        self.ui.label_endereco_acessado.setText(f"  {self.host}")

        QTimer.singleShot(100, self.conectar)

    def on_mouse_move(self, x, y):
        try:
            # Concatena o cabeçalho e as coordenadas em um único pacote binário
            pacote = b"MOU " + struct.pack("!ii", x, y)  # '!ii' formata x e y como inteiros
            self.cliente_socket.sendall(pacote)
        except Exception as e:
            print(f"Erro ao enviar posição do mouse: {e}")

    def on_mouse_click(self, x, y, tipo_clique):
        """Envia comando de clique do mouse para o servidor."""

        tipo_clique_map = {
            'press': 1,
            'release': 2,
            'right_press': 3,
            'right_release': 4
        }
        tipo_clique_num = tipo_clique_map.get(tipo_clique, 0)

        try:
            pacote = b"CLK " + struct.pack("!iii", x, y, tipo_clique_num)
            self.cliente_socket.sendall(pacote)
        except Exception as e:
            print(f"Erro ao enviar clique do mouse: {e}")

    def on_key_event(self, key_code, event_type):
        # Caracteres especiais que requerem Shift
        shift_needed_keys = {
            33: (0x10, 0x31),  # Shift + 1 = !
            64: (0x10, 0x32),  # Shift + 2 = @
            35: (0x10, 0x33),  # Shift + 3 = #
            36: (0x10, 0x34),  # Shift + 4 = $
            37: (0x10, 0x35),  # Shift + 5 = %
            94: (0x10, 0x36),  # Shift + 6 = ^
            38: (0x10, 0x37),  # Shift + 7 = &
            42: (0x10, 0x38),  # Shift + 8 = *
            40: (0x10, 0x39),  # Shift + 9 = (
            41: (0x10, 0x30),  # Shift + 0 = )
            95: (0x10, 0xBD),  # Shift + - = _
            43: (0x10, 0xBB),  # Shift + = = +
        }

        if key_code in shift_needed_keys:
            shift_code, main_key_code = shift_needed_keys[key_code]
            if event_type == "press":
                self.cliente_socket.sendall(b"KEY " + struct.pack("!i", shift_code) + event_type.encode('utf-8'))
                self.cliente_socket.sendall(b"KEY " + struct.pack("!i", main_key_code) + event_type.encode('utf-8'))
            elif event_type == "release":
                self.cliente_socket.sendall(b"KEY " + struct.pack("!i", main_key_code) + event_type.encode('utf-8'))
                self.cliente_socket.sendall(b"KEY " + struct.pack("!i", shift_code) + event_type.encode('utf-8'))
        else:
            try:
                pacote = b"KEY " + struct.pack("!i", key_code) + event_type.encode('utf-8')
                self.cliente_socket.sendall(pacote)
            except Exception as e:
                print(f"Erro ao enviar evento de teclado: {e}")

    def mostar_comandos(self):

        if self.ui.checkBox.isChecked():
            self.ui.frame_geral_comando.show()
        else:
            self.ui.frame_geral_comando.hide()

    def exec_mostrar_comandos(self):
        threading.Thread(target=self.mostar_comandos).start()

    def enviar_comando(self):
        """Envia o comando no lineEdit_comando para o servidor e recebe o resultado."""
        CHAVE = b'4xrm5t5yv3mn6V7l0h7C31G1ueQrsF-5ok36cnoMKm8='
        fernet = Fernet(CHAVE)

        try:
            comando = self.ui.lineEdit_comando.text().strip()
            if comando:

                comando_criptografado = fernet.encrypt(comando.encode('utf-8'))

                # Envia o comando ao servidor com o cabeçalho CMD
                mensagem = b"CMD " + comando_criptografado

                self.cliente_socket.sendall(mensagem)

                self.ui.textEdit.append(f"Comando Enviado:\n{comando}\n\n")

                self.ui.lineEdit_comando.setText("")

        except Exception as e:
            print(f"Erro ao enviar comando: {e}")


    def receber_dados(self, cliente_socket):

        while True:

            if self.flag_fechar_thread == True:
                break

            try:
                cabecalho = cliente_socket.recv(4)
                if cabecalho == b"IMG ":

                    # Recebe o tamanho da imagem
                    img_size_data = cliente_socket.recv(4)
                    img_size = int.from_bytes(img_size_data, 'big')

                    # Recebe a imagem completa
                    img_data = b""
                    while len(img_data) < img_size:
                        packet = cliente_socket.recv(img_size - len(img_data))
                        if not packet:
                            break
                        img_data += packet

                    # Converte os dados recebidos para uma imagem e exibe na QLabel
                    img = Image.open(io.BytesIO(img_data)).convert("RGB")

                    # Converte a imagem Pillow para QImage e depois para QPixmap
                    img_bytes = img.tobytes("raw", "RGB")
                    qimg = QImage(img_bytes, img.width, img.height, QImage.Format_RGB888)
                    pixmap = QPixmap.fromImage(qimg)

                    # Redimensiona o QPixmap exatamente para o tamanho da QLabel
                    pixmap = pixmap.scaled(self.ui.label_tela.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

                    # Exibe o QPixmap redimensionado na QLabel
                    self.ui.label_tela.setPixmap(pixmap)

                    self.label_size = self.ui.label_tela.size()
                    self.ui.label_tela.setFixedSize(self.label_size)

                elif cabecalho == b"CMD ":

                    # Recebe o tamanho do conteúdo
                    tamanho_data = cliente_socket.recv(4)
                    tamanho = int.from_bytes(tamanho_data, 'big')

                    # Recebe os dados completos com base no tamanho especificado
                    dados = b""
                    while len(dados) < tamanho:
                        parte = cliente_socket.recv(tamanho - len(dados))
                        if not parte:
                            break
                        dados += parte

                    # Decodifica e exibe o resultado do comando
                    try:
                        resultado = dados.decode('utf-8')
                    except UnicodeDecodeError:
                        resultado = dados.decode('cp850', errors='ignore')

                    print("Resultado do comando:", resultado)
                    self.ui.textEdit.append(resultado + '\n')

            except Exception as e:
                print(f"Erro ao receber: {e}")
                time.sleep(1)
                pass

    def conectar(self):
        # Configurações do cliente
        HOST = self.host  # IP do servidor
        PORT = 50000

        try:
            # Criação do socket
            self.cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            self.cliente_socket.settimeout(1)

            self.cliente_socket.connect((HOST, PORT))

            if self.senha == "":
                self.senha = "embranco"

            # Envia a senha para autenticação
            self.cliente_socket.sendall(self.senha.encode('utf-8'))

            # Recebe a resposta de autenticação
            resposta = self.cliente_socket.recv(1024).decode('utf-8')

            if resposta == "ACESSO_PERMITIDO":
                largura_label = self.ui.label_tela.width()
                altura_label = self.ui.label_tela.height()

                self.cliente_socket.sendall(struct.pack("!ii", largura_label, altura_label))

                threading.Thread(target=self.receber_dados, args=(self.cliente_socket,), daemon=True).start()

            else:
                self.cliente_socket.close()
                QMessageBox.warning(self, "Acesso Negado", "Acesso negado ou senha incorreta.")
                self.close()
                return

        except (socket.timeout, ConnectionRefusedError):
            print("Servidor indisponível ou inacessível.")
            QMessageBox.warning(self, "Servidor Indisponível", "Não foi possível conectar ao servidor.")
            self.close()

        except Exception as e:
            print(f"Erro ao conectar ao servidor: {e}")
            QMessageBox.warning(self, "Erro de Conexão", f"Erro ao conectar: {e}")
            self.close()

    def encerrar(self):
        self.close()

    def closeEvent(self, event):
        self.flag_fechar_thread = True
        event.accept()
