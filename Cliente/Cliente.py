import socket

# Porta do socket
porta = int(input("Digite a porta do socket (5 primeiros números do TIA): "))

# Criação do socket TCP
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
cliente_socket.connect(('localhost', porta))

while True:
    # Envia uma mensagem para o servidor
    mensagem = input("Cliente: ")
    cliente_socket.send(mensagem.encode())
    
    # Verifica se a mensagem é 'QUIT' para encerrar a conexão
    if mensagem.upper() == 'QUIT':
        break
    
    # Recebe a resposta do servidor
    resposta = cliente_socket.recv(1024).decode()
    print("Servidor:", resposta)

# Fecha o socket
cliente_socket.close()
