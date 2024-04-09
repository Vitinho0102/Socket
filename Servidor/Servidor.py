import socket

# Porta do socket
porta = int(input("Digite a porta do socket (5 primeiros números do TIA): "))

# Criação do socket TCP
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket ao endereço local e à porta
servidor_socket.bind(('localhost', porta))

# Habilita o servidor a aceitar conexões
servidor_socket.listen(1)

print("Aguardando conexão do cliente...")

# Aceita uma conexão
conexao, endereco_cliente = servidor_socket.accept()
print("Conexão estabelecida com", endereco_cliente)

while True:
    # Recebe a mensagem do cliente
    mensagem = conexao.recv(1024).decode()
    print("Cliente:", mensagem)
    
    # Verifica se a mensagem é 'QUIT' para encerrar a conexão
    if mensagem.upper() == 'QUIT':
        break
    
    # Envia uma mensagem de volta para o cliente
    resposta = input("Servidor: ")
    conexao.send(resposta.encode())

# Fecha a conexão
conexao.close()