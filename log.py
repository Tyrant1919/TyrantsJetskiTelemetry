from __future__ import print_function #allows printing of just the string when printing the split
import serial
import sqlite3

serialport = serial.Serial("/dev/ttyUSB0", 115200) #\\used to be ttyAMA0

try:
        line = (serialport.readline())
        while True:
                sum,x,y,z = (serialport.readline()).split('|')
                conn = sqlite3.connect('/var/www/html/testski.db')
                conn.execute('INSERT INTO ski VALUES(?,?,?,?)',(sum,x,y,z))
                conn.commit()
except KeyboardInterrupt:
        conn.close()
