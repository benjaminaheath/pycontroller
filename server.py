import network
import socket
import colours
import mode as controller_mode
from main import LED as m

ssid = 'Heathfamilywifi'
password = 'Heath123'

serv_sock_IP = '192.168.1.137'
serv_sock_PORT = 81

html = """<!DOCTYPE html>
<html>
    <head> <title>Pico W</title> </head>
    <body> <h1>Pico W</h1>
        <p>Mode: {}</p>
        <p>Primary Colour: {}</p>
        <p>Secondary Colour: {}</p>
        <p>Period_ms: {}</p>
    </body>
</html>
"""


def connect_wlan():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    print(f'IP: {wlan.ifconfig()[0]}')


def serv_handle():
    # TODO: make global variable main.LED pycontroller instance accessible in server.py
    global m
    # Accept new connections in an infinite loop
    serv_addr = socket.getaddrinfo(serv_sock_IP, serv_sock_PORT)[0][-1]
    serv_sock = socket.socket()
    serv_sock.bind(serv_addr)
    serv_sock.listen(1)
    while True:
        try:
            # Wait for client HTTP GET request on server TCP socket
            client_sock, client_addr = serv_sock.accept()
            data = str(client_sock.recv(2048))
            print(f"Request Received from:{client_addr}\r\n")

            # Search for URI in HTTP GET request, if hit, update Controller Model
            for mo in controller_mode.modes.keys():
                uri = f'/mode/{mo}'
                if data.find(uri) == 6:
                    mode = m
                    m.mode = mode
            for c1 in colours.index.keys():
                uri = f'/primary_colour/{c1}'
                if data.find(uri) == 6:
                    primary_colour = c1
                    m.primary_colour = primary_colour
            for c2 in colours.index.keys():
                uri = f'/secondary_colour/{c2}'
                if data.find(uri) == 6:
                    secondary_colour = c2
                    m.secondary_colour = secondary_colour
            if data.find('/period_ms/') == 6:
                period_ms = int(data[17:data.find(' ', 17)])
                m.period_ms = period_ms

            # Generate HTTP Response
            response = html.format(m.mode, m.primary_colour, m.secondary_colour, m.period_ms)
            client_sock.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
            client_sock.send(response)
            client_sock.close()
        except OSError as e:
            print(e)
            client_sock.close()


def init_server():
    connect_wlan()
    serv_handle()
