import socket
import pickle
from class_bankkonto import Account


def commands(message, register: list):
    if type(message) is Account: # if type(message) is list
        register.append(message)
        return "Account added in register"
    elif message == "2": # 2 -> list all accounts
        return register
    elif message[0] == "3": # index 0 i str
        _,user_acc = message.split("#")
        for account in register:
            if account.account_number == user_acc:
                return f"Requested account: {account}"
        else:
            return f"There's no account with account number: {user_acc}"
    return "Se Main Menu options and try again"


def send_data(message, conn: socket.socket): # pragma: no cover
    data = pickle.dumps(message)
    conn.sendall(data)


def accept_conn(sock: socket.socket, register: list):
    conn, addr = sock.accept() #conn och addr skapas här
    with conn:
        print('Connected by', addr)
        recv_and_print_msg(conn, register)


def recv_and_print_msg(conn: socket.socket, register: list):
    try:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            message = pickle.loads(data) #to str
            print(f"Received {message}")
            message = commands(message, register)
            send_data(message, conn)
    except ConnectionResetError:
        print("Connection closed")


def main():
    addr = "127.0.0.1", 50008
    register = []
    with socket.socket() as sock:
        sock.bind(addr)
        sock.listen(1)
        print("Server is listening")
        accept_conn(sock, register)


if __name__ == '__main__':
    main()
