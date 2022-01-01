from pms_a003 import Sensor
import csv


air_mon = Sensor()
air_mon.connect_hat(port="/dev/ttyS0", baudrate=9600)


values = air_mon.read()
print("PMS 1 value is {}".format(values.pm10_cf1))
print("PMS 2.5 value is {}".format(values.pm25_cf1))
print("PMS 10 value is {}".format(values.pm100_cf1))

pm10val = values.pm10_cf1
pm25val = values.pm25_cf1
pm100val = values.pm100_cf1

air_mon.disconnect_hat()
  
# exporting a list variable into the csv file
  
# Example.csv gets created in the current working directory 
with open('exported_vals.csv', 'w', newline = '') as csvfile:
    my_writer = csv.writer(csvfile, delimiter = ' ')
    my_writer.writerow("PM 1.0 : {1}, PM 2.5 : {2}, PM 10 : {3}".format(pm10val,pm25val,pm100val))
