#
#  attempts at copying the reading csv
#
import csv

#--------------
'''
read csv file
'''

reader = csv.reader(file_obj)
for row in reader:
	print(" ".join(row))

#-------
if __name__ == '__main__':
	csv_path = "TB_burden_countries_2014-09-27.csv"
	with open(csv_path, "rb") as f_obj:
		csv_reader(f_obj)