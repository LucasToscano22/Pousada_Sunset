
import socket
import json
from datetime import datetime
import threading
import sys

# Configurações do servidor
HOST = ''  # Endereço IP do servidor
PORT = 5000 # Porta que será utilizada

# Variáveis globais para manter o estado dos usuários ativos e outra para garantir a consistência dos dados em multi-threaded
active_users = {}
lock_active_users = threading.Lock()

# Armazenar reservas no formato: { "quarto1": [(data_inicio1, data_fim1), (data_inicio2, data_fim2)] }
reservas = {}

# Função para verificar se o quarto está disponível nas datas solicitadas
def verificar_disponibilidade(quarto, data_inicio, data_fim):
    if quarto in reservas:
        for reserva in reservas[quarto]:
            inicio_reservado, fim_reservado = reserva
            # Verifica se há sobreposição de datas
            if (data_inicio <= fim_reservado and data_fim >= inicio_reservado):
                return False  # Se há sobreposição, a data não está disponível
    return True

# Função para adicionar uma nova reserva
def adicionar_reserva(quarto, data_inicio, data_fim):
    if quarto not in reservas:
        reservas[quarto] = []
    reservas[quarto].append((data_inicio, data_fim))

# Função para tratar cada cliente
def handle_client(conn, addr):
    print(f"Conectado a {addr}")
    
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break

            # Decodificar os dados recebidos
            dados_reserva = json.loads(data.decode())
            

            print("Dados da reserva recebidos:")
            print(f"Nome: {dados_reserva['nome']}")
            print(f"E-mail: {dados_reserva['email']}")
            print(f"Quarto: {dados_reserva['quarto']}")
            print(f"Pagamento: {dados_reserva['pagamento']}")
            print(f"Data de Início: {dados_reserva['data_inicio']}")
            print(f"Data de Fim: {dados_reserva['data_fim']}")
            


            

            # Conversão das datas recebidas
            formato_data = "%d/%m/%Y"
            data_inicio = datetime.strptime(dados_reserva['data_inicio'], formato_data)
            data_fim = datetime.strptime(dados_reserva['data_fim'], formato_data)

            # Verificar se as datas estão disponíveis
            if verificar_disponibilidade(dados_reserva['quarto'], data_inicio, data_fim):
                adicionar_reserva(dados_reserva['quarto'], data_inicio, data_fim)
                res = 'RESERVA-215'  # Código de sucesso
                conn.sendall(res.encode())
            else:
                res = 'ERRO-802'  # Código de erro de data indisponível
                conn.sendall(res.encode())  # Enviar apenas o código
            print("Data não disponível.")
        except Exception as e:
            print(f"Erro: {e}")
            break

    conn.close()
    print(f"Conexão encerrada com {addr}")

# Configuração de inicialização do servidor, aceitando conexões e criando as threads para tratar cada cliente
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print('Servidor iniciado.')
    
    while True:
        client_socket, address = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_socket, address)).start()
        print(f'Cliente {address} conectado!')

if __name__ == '__main__':
    main()