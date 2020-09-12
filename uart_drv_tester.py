#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import threading
import serial, serial.threaded, serial.serialutil
import serial.tools.list_ports


class PrintLines(serial.threaded.Protocol):
    def set_serial(self, serial_instance):
#         print("set receive")
        self.serial = serial_instance
    
    def connection_made(self, transport):
        super(PrintLines, self).connection_made(transport)
        print('Connection established')
        self.buf = []
        self.buf_cnt = 0
        
        # TODO: start pinger here

    def data_received(self, data):
        print('Received:', data)
        
        for byte in data:
            self.buf.append(byte)
            
        if 0 in data:
            if bytearray(self.buf) == b'@BAUDRATE: 9600\x00':
                self.serial.baudrate = 9600
                print(f'Baudrate changed to: {self.serial.baudrate}')
            elif bytearray(self.buf) == b'@BAUDRATE: 115200\x00':
                self.serial.baudrate = 115200
                print(f'Baudrate changed to: {self.serial.baudrate}')
            elif bytearray(self.buf) == b'@BAUDRATE: 460800\x00':
                self.serial.baudrate = 460800
                print(f'Baudrate changed to: {self.serial.baudrate}')
            elif bytearray(self.buf) == b'@BAUDRATE: 1000000\x00':
                self.serial.baudrate = 1000000
                print(f'Baudrate changed to: {self.serial.baudrate}')
            else:
                self.buf[len(self.buf) - 2] += 1
                print('Send rsp:', bytearray(self.buf))
                self.serial.write(bytearray(self.buf))
                
            self.buf.clear()
        
    def connection_lost(self, exc):
        print('Connection lost...')
    

class Host:
    def __init__(self, port, baudrate):
        self.ser = serial.Serial(port, baudrate)
        transport = serial.threaded.ReaderThread(self.ser, PrintLines)
        transport.start()
        self.transport, self.protocol = transport.connect()
        self.protocol.set_serial(self.ser)
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.transport.close()

    def send(self, data):
        self.ser.write(data)
        

    def close(self):
        self.ser.close()


# DEVICE_NAME = 'STM32 Virtual ComPort'
DEVICE_NAME = 'JLink CDC UART Port'


def check_device(exit_event, disconnect_event):
    # check if device com port and generate device dscn evt when not
    
    while not exit_event.wait(0.1):
        is_device_found = False
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if DEVICE_NAME in port.description:
                is_device_found = True

        if not is_device_found:
            print('Device disconnected')
            disconnect_event.set()


# TODO: use condition to build event handler
# TODO: try to remove recursion

def connect(exit_event):
    disconnect_event = threading.Event()
    device_status_worker = threading.Thread(target=check_device, args=(exit_event, disconnect_event))
    
    ports = serial.tools.list_ports.comports()
    port = ''
    for item in ports:
        if DEVICE_NAME in item.description:
            port = item.device
            
    try:
        with Host(port, 115200) as host:
            print(f'Connected with device "{DEVICE_NAME}"')
            disconnect_event.clear()
            device_status_worker.start()
    #         host.send(b'some data')
    
    #         time.sleep(5)
    
    #         for x in range(3):
            while not exit_event.wait(0.1) and not disconnect_event.wait(0.1):
                pass
            
    #             for p in serial.tools.list_ports.comports():
    #                 print(p)
                    
            # try connect in loop if was dscn event
    
    #         ar = bytearray(b'@BAUDRATE: 9600\x00')
    #         if ar == b'@BAUDRATE: 9600\x00':
    #             print('yeah')
    
    except serial.serialutil.SerialException:
        print('Device not found')
        
    if disconnect_event.is_set():
        print('Trying to reconnect...')
        exit_event.set()
        device_status_worker.join()
        exit_event.clear()

    if not exit_event.is_set():
        time.sleep(0.5)        
        connect(exit_event)


if __name__ == '__main__':
    exit_event = threading.Event()
    
    connection_worker = threading.Thread(target=connect, args=(exit_event, ))
#     connection_worker.setDaemon(True)
    connection_worker.start()
    
    input('Press Enter to exit...\n')
    print('Connection terminated.')
    exit_event.set()
    
    connection_worker.join()

