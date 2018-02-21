from __future__ import print_function #allows printing of just the string when printing the split
import serial
import sqlite3

serialport = serial.Serial("/dev/ttyUSB0", 115200) #\\used to be ttyAMA0

try:
        while True:
                line = (serialport.readline())
                print (line)
                if "Range" not in line:
                        sum,x,y,z = line.split('|')
                        print (sum,x,y,z)
                        conn = sqlite3.connect('/var/www/html/testski.db')
                        conn.execute('INSERT INTO ski VALUES(?,?,?,?)',(sum,x,y,z))
                        conn.commit()
except KeyboardInterrupt:
        conn.close()
        sys.exit()
