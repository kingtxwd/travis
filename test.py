
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
                        
                        if not(cell == "" or cell == "UD" or cell == "NI" or cell == "NDOI" or cell == "NDOD" or cell == "NOD" or cell == "ID" or cell == "OD-Vic" or cell == "OD-Brit" or cell == "OD"):
                            return False
                    if j == 5:
                        if not (cell == "" or cell == "Blank" or cell == "Opened" or cell == "Accepted" or cell == "InspiredAFix" or cell == "DeveloperFixed" or cell == "Deleted" or cell == "Rejected" or cell == "Skipped") :
                            return False
                    j = j + 1
                if j > 10:
                    print("number")
                    return False
            i= i + 1
    return True

def assert_content(file_name):
    with open(file_name,'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        i = 0     
        for row in reader:
            if i != 0:
                j = 0
                sha = ""
                project = ""
                for cell in row:
                    if j == 0 :
                        project = cell
                    if j == 1 :
                        sha = cell
                    j = j + 1
                command = "wget "+ project + "/archive/" + sha + ".zip"
            i= i + 1
    return True

if assert_format("FlakyTestCharacteristics.csv"):
    if assert_content("FlakyTestCharacteristics.csv"):
        print(True)
else:
    print(False)