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
from templates.tela_home import Ui_Home
import socket
import subprocess
import threading
import datetime
from cryptography.fernet import Fernet
from PIL import ImageGrab
import io
import time
import secrets
import string
import modules.recebendo_imagem
import os
import ctypes

class Home(QMainWindow):

    def __init__(self,  *args, **argvs):
        super(Home, self).__init__(*args, **argvs)
        self.ui = Ui_Home()
        self.ui.setupUi(self)
        self.setWindowTitle('Ajudesk')
        self.setWindowIcon(QIcon(":Icone/icon.ico"))
        self.server_running = False
        self.server_socket = None
        self.get_ipv4_address()
        self.ui.lineEdit_ip_local.setReadOnly(True)
        self.ui.lineEdit_ip_local.setAlignment(Qt.AlignCenter)
        self.ui.btn_copiar.clicked.connect(self.copy_text_to_clipboard)
        self.ui.btn_conectar.clicked.connect(self.abrir_recebendo_imagem)
        self.ui.btn_salvar.clicked.connect(self.salvar_senha)
        self.ui.lineEdit_ip_destino.returnPressed.connect(self.abrir_recebendo_imagem)
        self.ui.lineEdit_senha_destino.returnPressed.connect(self.abrir_recebendo_imagem)
        self.ui.lineEdit_senha_local.returnPressed.connect(self.salvar_senha)
        self.verifica_senha()
        self.start_server_thread()

        # Definindo a expressão regular para validar IP
        ip_regex = QRegExp(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        ip_validator = QRegExpValidator(ip_regex)
        self.ui.lineEdit_ip_destino.setValidator(ip_validator)
    def salvar_senha(self):

        arquivo_senha = 'password'

        CHAVE = b'4xrm5t5yv3mn6V7l0h7C31G1ueQrsF-5ok36cnoMKm8='
        fernet = Fernet(CHAVE)

        senha_criptografada = fernet.encrypt(self.ui.lineEdit_senha_local.text().encode())

        with open(arquivo_senha, 'wb') as f:
            f.write(senha_criptografada)

        QMessageBox.information(self, "Senha Salva", "Senha salva com sucesso")

    def gerar_senha(self, tamanho=8):
        caracteres = string.ascii_letters + string.digits
        senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
        return senha

    def verifica_senha(self):
        """Verifica se o arquivo de senha existe e gerencia a criação ou leitura da senha."""

        arquivo_senha = 'password'

        CHAVE = b'4xrm5t5yv3mn6V7l0h7C31G1ueQrsF-5ok36cnoMKm8='
        fernet = Fernet(CHAVE)

        # Verifica se o arquivo de senha existe
        if not os.path.exists(arquivo_senha):
            # Gera uma nova senha e criptografa
            senha = self.gerar_senha()
            senha_criptografada = fernet.encrypt(senha.encode())

            # Salva a senha criptografada no arquivo
            with open(arquivo_senha, 'wb') as f:
                f.write(senha_criptografada)

        else:
            # Lê e descriptografa a senha do arquivo
            with open(arquivo_senha, 'rb') as f:
                senha_criptografada = f.read()

            senha = fernet.decrypt(senha_criptografada).decode()

        self.ui.lineEdit_senha_local.setText(senha)

    def validar_ip(self):
        ip = self.ui.lineEdit_ip_destino.text()
        partes = ip.split('.')
        if len(partes) == 4 and all(0 <= int(parte) <= 255 for parte in partes if parte.isdigit()):
            return True
        else:
            return False

    def abrir_recebendo_imagem(self):

        if self.validar_ip() == False:
            QMessageBox.information(self, "IP Inválido", "O endereço IP digitado é inválido.")
            return

        self.tela_recebendo_imagem = modules.recebendo_imagem.Recebendo_Imagem(self.ui.lineEdit_ip_destino.text(), self.ui.lineEdit_senha_destino.text())
        self.tela_recebendo_imagem.showMaximized()

    def copy_text_to_clipboard(self):
        # Obtém o texto do QLineEdit
        text = self.ui.lineEdit_ip_local.text()

        # Acessa a área de transferência
        clipboard = QApplication.clipboard()

        # Define o texto na área de transferência
        clipboard.setText(text)

    def get_ipv4_address(self):
        try:
            # Cria um socket de conexão para determinar o IP real
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # Conecta a um servidor externo (não envia dados reais)
            s.connect(('8.8.8.8', 80))  # 8.8.8.8 é o DNS público do Google
            ipv4_address = s.getsockname()[0]  # Obtém o IP da interface LAN
            s.close()

            # Exibe o IPv4 na interface gráfica
            self.ui.lineEdit_ip_local.setText(ipv4_address)

        except Exception as e:
            QMessageBox.warning(self, "Erro", f"Erro ao obter o endereço IPv4 LAN: {e}")

    def start_server_thread(self):
        """Inicia o servidor em uma nova thread"""
        if not self.server_running:
            self.server_running = True
            server_thread = threading.Thread(target=self.open_server)
            server_thread.daemon = True  # Para que o servidor pare quando a interface fechar
            server_thread.start()
        else:
            QMessageBox.warning(self, "Servidor em Execução", f"O servidor já está sendo executado.")

    def open_server(self):
        """Metodo que contém a lógica do servidor"""

        # Configurações do servidor
        HOST = '0.0.0.0'  # Aceita conexões de qualquer IP
        PORT = 50000

        # Criação do socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((HOST, PORT))
        self.server_socket.listen(5)

        print(f"Servidor ouvindo na porta {PORT}...")

        while self.server_running:
            try:
                cliente_socket, endereco_cliente = self.server_socket.accept()
                print(f"Conexão estabelecida com {endereco_cliente}")
                # Criar uma nova thread para lidar com o cliente
                client_thread = threading.Thread(target=self.handle_client, args=(cliente_socket, endereco_cliente))
                client_thread.daemon = True
                client_thread.start()

            except Exception as e:
                print(f"Erro ao aceitar a conexão: {e}")
                break

    def capturar_tela_com_cursor(self):
        # Captura a tela
        screenshot = ImageGrab.grab()

        # # Obtém a posição do cursor usando ctypes
        # cursor_pos = ctypes.wintypes.POINT()
        # ctypes.windll.user32.GetCursorPos(ctypes.byref(cursor_pos))
        # cursor_x, cursor_y = cursor_pos.x, cursor_pos.y
        #
        # # Carrega a imagem do cursor
        # cursor_img = Image.open("images/cursor.png").convert("RGBA")
        #
        # # Ajuste o cursor para a posição correta na captura de tela
        # cursor_offset_x, cursor_offset_y = 0, 0  # Ajuste a posição do cursor se necessário
        # screenshot.paste(cursor_img, (cursor_x + cursor_offset_x, cursor_y + cursor_offset_y), cursor_img)

        return screenshot

    def transmitir_tela(self, cliente_socket):
        """Captura e envia a tela em um único pacote contendo cabeçalho, tamanho e dados da imagem."""
        try:
            while True:
                screenshot = self.capturar_tela_com_cursor()
                img_bytes = io.BytesIO()
                screenshot.save(img_bytes, format='JPEG', quality=50)
                img_data = img_bytes.getvalue()

                # Cria o pacote completo com o cabeçalho "IMG ", o tamanho e os dados da imagem
                pacote = b"IMG " + len(img_data).to_bytes(4, 'big') + img_data

                cliente_socket.sendall(pacote)

                time.sleep(0.01)  # Intervalo para controle de taxa de envio

        except Exception as e:
            print(f"Erro na transmissão de tela: {e}")
            cliente_socket.close()


    def handle_client(self, cliente_socket, endereco_cliente):
        """Função para lidar com o cliente conectado e executar comandos."""

        senha_cliente = cliente_socket.recv(1024).decode('utf-8').strip()

        if senha_cliente == "embranco":
            senha_cliente = ""

        # Verifica se a senha está correta
        if senha_cliente != self.ui.lineEdit_senha_local.text():
            cliente_socket.sendall(b"ACESSO_NEGADO")
            cliente_socket.close()
            return

        else:

            cliente_socket.sendall(b"ACESSO_PERMITIDO")


        def log_command(event_type, info):
            with open('command_log.txt', 'a') as log_file:
                log_file.write(f"Data e Hora: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                log_file.write(f"{event_type}: {info}\n")
                log_file.write("=" * 50 + "\n")

        log_command("Entrada do Cliente", f"Cliente {endereco_cliente} conectou-se")


        largura_label, altura_label = struct.unpack("!ii", cliente_socket.recv(8))

        largura_tela, altura_tela = self.get_screen_size()

        escala_x = largura_tela / largura_label
        escala_y = altura_tela / altura_label


        threading.Thread(target=self.transmitir_tela, args=(cliente_socket,), daemon=True).start()

        CHAVE = b'4xrm5t5yv3mn6V7l0h7C31G1ueQrsF-5ok36cnoMKm8='
        fernet = Fernet(CHAVE)

        while True:
            try:
                # Recebe o cabeçalho da mensagem para identificar o tipo de dado
                cabecalho = cliente_socket.recv(4)

                # Se for um comando (CMD), executa-o em uma nova thread
                if cabecalho == b"CMD ":

                    # Recebe o comando criptografado
                    comando_criptografado = cliente_socket.recv(1024)

                    # Descriptografa o comando
                    comando = fernet.decrypt(comando_criptografado).decode('utf-8').strip()

                    log_command("Comando Recebido", f"Executando comando: {comando}")
                    print(f"Executando comando cmd: {comando}")

                    # Executa o comando em uma thread separada para evitar bloqueio
                    threading.Thread(target=self.executar_comando, args=(cliente_socket, comando), daemon=True).start()

                # Caso contrário
                elif cabecalho == b"MOU ":
                    coordenadas = cliente_socket.recv(8)
                    if len(coordenadas) == 8:
                        x_label, y_label = struct.unpack("!ii", coordenadas)

                        # Ajusta as coordenadas usando a escala
                        x_tela = int(x_label * escala_x)
                        y_tela = int(y_label * escala_y)

                        # Move o cursor do servidor para a posição ajustada
                        ctypes.windll.user32.SetCursorPos(x_tela, y_tela)

                elif cabecalho == b"CLK ":
                    dados_clique = cliente_socket.recv(12)
                    if len(dados_clique) == 12:
                        x_label, y_label, tipo_clique = struct.unpack("!iii", dados_clique)
                        x_tela = int(x_label * escala_x)
                        y_tela = int(y_label * escala_y)
                        self.executar_clique(x_tela, y_tela, tipo_clique)

                # Processa o evento de teclado
                elif cabecalho == b"KEY ":

                    key_data = cliente_socket.recv(8)  # 4 bytes para key_code e 4 para event_type
                    key_code, event_type_code = struct.unpack("!ii", key_data)

                    print(key_code, event_type_code)

                    if event_type_code == 1886545267:
                        self.executar_tecla(key_code, "press")

                    elif event_type_code == 1919249509:
                        self.executar_tecla(key_code, "release")

            except Exception as e:
                print(f"Erro ao lidar com o cliente: {e}")
                log_command("Erro", str(e))
                cliente_socket.close()
                break


    def executar_comando(self, cliente_socket, comando):
        """Executa o comando em segundo plano e envia a saída de volta ao cliente em um único pacote."""
        try:
            # Executa o comando e captura a saída
            process = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            stdout, stderr = process.communicate()

            # Constrói a saída combinando stdout e stderr
            output = ""
            if stdout:
                output += stdout.decode('cp850', errors='ignore')
            if stderr:
                output += stderr.decode('cp850', errors='ignore')

            # Envia uma mensagem padrão se não houver saída
            if not output.strip():
                output = "(Nenhum resultado do comando)"

            # Codifica o output para enviar como bytes
            output_data = output.encode('utf-8', errors='ignore')

            # Cria o pacote com o cabeçalho, tamanho e dados do comando
            pacote = b"CMD " + len(output_data).to_bytes(4, 'big') + output_data

            # Envia o pacote completo
            cliente_socket.sendall(pacote)

        except Exception as e:
            error_message = f"Erro ao executar comando: {e}"
            print(error_message)
            error_data = error_message.encode('utf-8', errors='ignore')
            pacote_erro = b"CMD " + len(error_data).to_bytes(4, 'big') + error_data
            cliente_socket.sendall(pacote_erro)

    def get_screen_size(self):
        user32 = ctypes.windll.user32
        largura = user32.GetSystemMetrics(0)  # Largura da tela
        altura = user32.GetSystemMetrics(1)  # Altura da tela
        return largura, altura

    def executar_clique(self, x, y, tipo_clique):
        """Executa um clique nas coordenadas (x, y) com o tipo de clique especificado."""

        ctypes.windll.user32.SetCursorPos(x, y)  # Move o cursor para a posição antes de qualquer ação

        # Define os eventos de clique
        MOUSEEVENTF_LEFTDOWN = 0x0002
        MOUSEEVENTF_LEFTUP = 0x0004
        MOUSEEVENTF_RIGHTDOWN = 0x0008
        MOUSEEVENTF_RIGHTUP = 0x0010

        if tipo_clique == 1:  # Pressionar botão esquerdo
            ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        elif tipo_clique == 2:  # Soltar botão esquerdo
            ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        elif tipo_clique == 3:  # Pressionar botão direito
            ctypes.windll.user32.mouse_event(MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
        elif tipo_clique == 4:  # Soltar botão direito
            ctypes.windll.user32.mouse_event(MOUSEEVENTF_RIGHTUP, x, y, 0, 0)

    def executar_tecla(self, key_code, event_type):
        """Executa uma ação de tecla no servidor usando ctypes."""
        KEYEVENTF_KEYUP = 0x0002  # Constante para evento de liberação de tecla
        if event_type == "press":
            ctypes.windll.user32.keybd_event(key_code, 0, 0, 0)  # Pressiona a tecla
        elif event_type == "release":
            ctypes.windll.user32.keybd_event(key_code, 0, KEYEVENTF_KEYUP, 0)  # Solta a tecla
