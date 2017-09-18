



- sudo chmod 777 /dev/ttyACM0

- rosrun nmea_gps_driver nmea_gps_driver.py  _port:=/dev/ttyACM0 _baud:=9600

- rostopic echo /fix
- rostopic echo /fix/latitude

- screen /dev/ttyACM0 9600