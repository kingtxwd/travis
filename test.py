
import sys
import csv
import os


def assert_format(file_name):
    with open(file_name,'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        i = 0
        for row in reader:
            if i != 0:
                j = 0
                for cell in row:
                    if j == 0 :
                        if not cell.startswith("https://github.com/"): 
                            return False
                    if j == 3:
                        if "#" in cell :
                            return False
                    if j == 4:
                        if cell == "" or cell == "UD" or cell == "NI" or cell == "NDOI" or cell == "NDOD" or cell == "NOD" or cell == "ID" or cell == "OD-Vic" or cell == "OD-Brit" or cell == "OD":
                            continue
                        else :
                            print(4)
                            return False
                    if j == 5:
                        if cell == "" or cell == "Blank" or cell == "Opened" or cell == "Accepted" or cell == "InspiredAFix" or cell == "DeveloperFixed" or cell == "Deleted" or cell == "Rejected" or cell == "Skipped":
                            continue
                        else :
                            print(5)
                            return False
                    j = j + 1
                if j > 10:
                    print("number")
                    return False
            i= i + 1
    return True



if assert_format("FlakyTestCharacteristics.csv"):
    print(True)

else:
    print(False)