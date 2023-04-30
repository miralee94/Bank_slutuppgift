import socket
import pickle
from class_bankkonto import Account
from threading import Thread
from time import sleep


def menu_loop(MAIN_MENU_TEXT, conn:socket.socket):
    while True:
        sleep(1)
        user_choice = input(f"{MAIN_MENU_TEXT} ")
        if user_choice == "1":
            try:
                account_details = input("Write owner, account name, account type, account number: ").split(" ")
                account_details = Account(*account_details)
                send_data(account_details, conn)
            except TypeError:
                print("You have to write owner, account name, account type, account number")
        elif user_choice == "2":
            send_data(user_choice, conn)
        elif user_choice == "3":
            account_nr = input("Account number: ")
            send_data(f"{user_choice}#{account_nr}", conn)
        elif user_choice == "9":
            conn.close()
            break
        else:
            user_choice = "Invalid choice"
            print(user_choice)


def recv_and_print(conn:socket.socket):
    try:
        while True:
            received_data = conn.recv(4096)
            message_from_server = pickle.loads(received_data)
            if type(message_from_server) is list and len(message_from_server) > 0:
                for account in message_from_server:
                    print(account)
            else:
                print(f"{message_from_server}")
    except ConnectionAbortedError:
        print("Connection closed")


def send_data(message, conn: socket.socket):
    data = pickle.dumps(message)
    conn.sendall(data)


def main():
    addr = "127.0.0.1", 50008              # The same port as used by the server
    MAIN_MENU_TEXT = """
    '-------------------------'
    '------- Main Menu -------'
    '-------------------------'
    1: 'Add an account to register',
    2: 'List all accounts',
    3: 'Choose one account for more information',

    'To quit press 9'
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        conn.connect(addr)
        Thread(target = recv_and_print, args=(conn,)).start() # make possible to send och recv data at the same time without blocking input from client
        menu_loop(MAIN_MENU_TEXT, conn)


if __name__ == '__main__':
    main()
