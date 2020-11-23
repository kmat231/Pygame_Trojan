import platform
import socket

def RunSystemScan():
    file = open("SystemInfo.txt", "w+")
    file.write("System: " + platform.system() + "\n")
    file.write("System Machine: " + platform.machine() + "\n")
    file.write("System Version: " + platform.version() + "\n" )
    file.write("System Processor: " + platform.processor() + "\n" + "\n")

    for x in range(65535):
        port = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = port.connect_ex(('127.0.0.1',x))
        if result == 0:
            file.write("Port " + str(x) + " is open" + "\n")
        port.close()
    file.close()
    printFile()

def printFile():
    file = open("SystemInfo.txt", "r+")
    print (file.read())