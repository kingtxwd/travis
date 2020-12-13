
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
                            return "Project URL Error: Not a github opensource project"
                    if j == 3 :
                        if "#" in cell :
                            return "TestName error: use '.' instead of'#' before methodName"
                    if j == 4:
                        
                        if not(cell in ["", "UD", "NI", "NDOI", "NDOD", "NOD", "ID", "OD-Vic", "OD-Brit", "OD"]):
                            return "Category Error: not a valid category type"
                    if j == 5:
                        if not (cell in ["", "Blank", "Opened", "Accepted", "InspiredAFix", "DeveloperFixed", "Deleted", "Rejected", "Skipped"]) :
                            return "Status Error: not a valid status type"
                    j = j + 1
                if j > 10:
                    return ("Format error: might include more info than needed")
            i= i + 1
    return "True"

def assert_content(file_name):
    with open(file_name,'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        i = 0     
        downloaded = {}
        for row in reader:
            if i != 0:
                j = 0
                sha = row[1]
                project = row[0]
                module = row [2]
                testname = row[3]
                projectname = row[0].split('/')[-1]
                key = project + sha
                dir = sha + "/" + projectname + "-" + sha
                if key not in downloaded:
                    command = "wget -N "+ project + "/archive/" + sha + ".zip -O  "+sha+".zip"
                    zip = os.system(command)
                    file = os.system("unzip -o "+sha+".zip -d "+sha+"/")
                    downloaded[key] = 1
                os.system("pwd && cd " + dir + " && mvn install -DskipTests -am " + ("-pl " + module if module != "" else ""))
                return_value = os.system("mvn edu.illinois:nondex-maven-plugin:1.1.2:nondex -Dtest=" + testname)
                os.system("cd ../../")
                if return_value == 0 :
                    return project + " of " + sha + " on " + testname + "is not flaky"
            i= i + 1
    return "All tests are flaky"

result = assert_format("FlakyTestCharacteristics.csv") 
if result == "True":
    print(assert_content("FlakyTestCharacteristics.csv"))
else:
    print(result)