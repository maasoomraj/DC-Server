import socket
import sys
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def releaseAll():
    time.sleep(0.1)
    keyboard.release(Key.up)
    keyboard.release(Key.down)
    keyboard.release(Key.left)
    keyboard.release(Key.right)

def pressKeyboard(str):
    if(str == "U"):
        keyboard.press(Key.up)
    elif(str == "D"):
        keyboard.press(Key.down)
    elif(str == "L"):
        keyboard.press(Key.left)
    elif(str == "R"):
        keyboard.press(Key.right)
    releaseAll()

# Create a TCP/IP socket for server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# name = socket.gethostname()
# print(name)
# ip = socket.gethostbyname(name)
# print(ip)

# Bind the socket to the port
serverAddress = ('192.168.0.104', 10000)
server.bind(serverAddress)

print("Server successfully created...")
print("Server listening at localhost at port 10000")

# Listen for incoming connections
server.listen(1)

while True:
    # Wait for a connection
    print("No clients connected with server.\nWaiting for client to connect...")
    connection, client_address = server.accept()
    print("Client requested to connect...")

    try:
        print("Client", client_address, "successfully connected...")

        # Receive 1 byte data "L", "U", "R", "D"
        while True:
            dataByte = connection.recv(1)
            if not dataByte:
                break
            dataChar = dataByte.decode('utf-8')
            if dataChar == 'Q':
                continue
            print(dataChar)
            pressKeyboard(dataChar)      
    finally:
        # Close the connection
        connection.close()
        print("Connection lost from", client_address)