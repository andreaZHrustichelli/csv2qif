import sys
import csv
import configparser
from datetime import datetime

#prompt the input file
IN_FILE = input("Enter the input file name: ")
if (IN_FILE.endswith(".csv")):
    print("Input file -> OK!")
else:
    sys.exit("Input file -> KO!!!")

#prompt the output file
OUT_FILE = input("Enter the output file name: ")
if (OUT_FILE.endswith(".qif")):
    print("Output file -> OK!")
else:
    sys.exit("Output file -> KO!!!")

#READ FROM CONFIGURATION FILE
config = configparser.ConfigParser()
config.read("csv2qif.config")
#read section [CSV-FILE] and initialize variables
CSV_HAS_TITLE = config['CSV-FILE']['Title']
CSV_COLUMN_D = config['CSV-FILE']['IndexColumnDate']
CSV_COLUMN_M = config['CSV-FILE']['IndexColumnDescription']
CSV_COLUMN_T = config['CSV-FILE']['IndexColumnAmount']
CSV_COLUMN_L = config['CSV-FILE']['IndexColumnGnuCashCategory']
CSV_COLUMN_N = config['CSV-FILE']['IndexColumnCode']
#read section [QIF-HEADER] and initialize variables
QIF_TYPE = config['QIF-HEADER']['Type']
QIF_ACCOUNT_NAME = config['QIF-HEADER']['AccountName']
QIF_ACCOUNT_DESCRIPTION = config['QIF-HEADER']['AccountDescription']

out_file = open(OUT_FILE,"w")
out_file.write("!Account")
out_file.write("\n")
out_file.write("N"+QIF_ACCOUNT_NAME)
out_file.write("\n")
out_file.write("D"+QIF_ACCOUNT_DESCRIPTION)
out_file.write("\n")
out_file.write("^")
out_file.write("\n")
out_file.write(QIF_TYPE)
out_file.write("\n")

with open(IN_FILE) as csv_file:
    reader=csv.reader(csv_file,delimiter=';')
    #IF file has title, go to next row
    if (CSV_HAS_TITLE == "yes"):
        next(csv_file)

    for row in reader:
        QIF_D_VALUE=row[int(CSV_COLUMN_D)]
        out_file.write("D"+QIF_D_VALUE)
        out_file.write("\n")

        QIF_M_VALUE=row[int(CSV_COLUMN_M)]
        out_file.write("M"+QIF_M_VALUE)
        out_file.write("\n")

        QIF_T_VALUE=row[int(CSV_COLUMN_T)]
        out_file.write("T"+QIF_T_VALUE)
        out_file.write("\n")

        if (int(CSV_COLUMN_L) == -1):
            out_file.write("L")
            out_file.write("\n")
        else:
            QIF_L_VALUE=row[int(CSV_COLUMN_L)]
            out_file.write("L"+QIF_L_VALUE)
            out_file.write("\n")

        if (int(CSV_COLUMN_N) == -1):
            out_file.write("N")
            out_file.write("\n")
        else:
            QIF_N_VALUE=row[int(CSV_COLUMN_N)]
            out_file.write("N"+QIF_N_VALUE)
            out_file.write("\n")

        out_file.write("^")
        out_file.write("\n")

out_file.close()
