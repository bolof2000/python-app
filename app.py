import socket
import datetime
import os


def get_ip_address():
    h_name = socket.gethostname()
    IP_addres = socket.gethostbyname(h_name)

    return IP_addres


def get_nodes_current_date_and_time():
    todays_date = datetime.datetime.now()
    return todays_date


import platform


def get_nodes_os_version():
    os_details = {
        "systems": platform.system(),
        "version": platform.version()
    }
    return os_details


def print_to_users():
    data_to_user = {
        "os_version": get_nodes_os_version(),
        "time_date": get_nodes_current_date_and_time(),
        "ip_address": get_ip_address()
    }

    return data_to_user


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return print_to_users()


if __name__ == "__main__":
    app.run("127.0.0.1", port=8283)
