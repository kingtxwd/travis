
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
                        
                        if not(cell in ["", "UD", "NI", "NDOI", "NDOD", "NOD", "ID", "OD-Vic", "OD-Brit", "OD"]):
                            return False
                    if j == 5:
                        if not (cell in ["", "Blank", "Opened", "Accepted", "InspiredAFix", "DeveloperFixed", "Deleted", "Rejected", "Skipped"]) :
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
        downloaded = {}
        for row in reader:
            if i != 0:
                j = 0
                sha = row[1]
                project = row[0]
                module = row [2]
                testname = row[3]
                projectname = row[0].split('/')[-1]
                """
                for cell in row:
                    if j == 0 :
                        project = cell
                    if j == 1 :
                        sha = cell
                    if j == 2 :
                        module = cell
                    if j == 3 : 
                    j = j + 1
                """
                key = project + sha
                dir = sha + "/" + projectname + "-" + sha
                if key not in downloaded:
                    command = "wget -N "+ project + "/archive/" + sha + ".zip -O  "+sha+".zip"
                    zip = os.system(command)
                    file = os.system("unzip -o "+sha+".zip -d "+sha+"/")
                    downloaded[key] = 1
                    # with open(dir + "/pom.xml") as f:
                    #     s = f.read()
                    #     if "</plugins>" not in s:
                    #         pass
                    #     else:
                    #         with open(dir + "/pom.xml", 'w') as f:
                    #             s = s.replace("</plugins>", " <plugin> <groupId>edu.illinois</groupId> <artifactId>nondex-maven-plugin</artifactId> <version>1.1.2</version>  </plugin>  </plugins>")
                    #             f.write(s)
                os.system("pwd && cd " + dir + " && mvn install -DskipTests -am " + ("-pl " + module if module != "" else ""))
                return_value = os.system("mvn edu.illinois:nondex-maven-plugin:1.1.2:nondex -Dtest=" + testname + " -f " + dir  + "/pom.xml")
                os.system("cd ../../")
                print(return_value)
            i= i + 1
    return True

if assert_format("FlakyTestCharacteristics.csv"):
    if assert_content("FlakyTestCharacteristics.csv"):
        print(True)
else:
    print(False)