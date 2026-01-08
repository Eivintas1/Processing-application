
# define Functions
def welcomeMessage():
    print("Welcome to the Student Certification Processing Application!")
    print("------------------------------------------------------------")

def exitMessage():
    print("Thank you for using the Student Certification Processing Application. Goodbye!")   

def calcGrade(score):
    if score >= 70:
        return 'A'
    elif score >= 60:
        return 'B'
    elif score >= 50:
        return 'C'
    elif score >= 40:
        return 'D'
    else:
        return 'E'     
    
def result(score):
    if score >= 50:
        return 'Pass'
    else:
        return 'Fail'
    
def overallAverage(totalModuleScores, numberOfmodules):
    return totalModuleScores / numberOfmodules

#main program
modules = ["System Design", "Programming", "Databases", "Testing", "Theory"]

welcomeMessage()

runAgain = 'Y'

while runAgain == 'Y':
    
#inputs
    candidatesName = input("Enter candidate's name: ")
    certificationName = input("Enter certification name: ")

    totalModuleScores = 0
    moduleScores = [0, 0, 0, 0, 0]

    #get 5 module scores
    for i in range(len(modules)):
        scores = int(input(f"Enter score for {modules[i]}: "))
        moduleScores[i] = scores
        totalModuleScores = totalModuleScores + scores

        avg = overallAverage(totalModuleScores, len(modules))

    #output results
    print("")
    print("Candidate Name:", candidatesName)
    print("Certification Name:", certificationName)
    print("--------------------------------------------")

    #print module details
    for i in range(len(modules)):
        score = moduleScores[i]    
        grade = calcGrade(score)
        res = result(score)
        print(modules[i], "- Score:", score, "Grade:", grade, "Result:", res)

    print("--------------------------------------------")
    print("Overall Average Score:", avg)

    if avg >= 50:
        overall = "Pass"
    else:
        overall = "Fail"

    print("")
    print("----------------Result Sheet------------------------")    
    print("Candidate Name:", candidatesName)
    print("Certification Name:", certificationName)
    print("")
    print("Module\t\tResult\tGrade\tOutcome")

    for i in range(len(modules)):
        score = moduleScores[i]
        grade = calcGrade(score)
        outcome = result(score)
        print(f"{modules[i]}\t{score}\t{grade}\t{outcome}")

    print("")
    print("Overall Average Score:", avg)
    print("Overall Result:", overall)
    print("")
    print("Candidates must achieve an overall average of at least 50 to pass the certification.")
    print("------------------------------------------------------------")    

    csvFile = open("results.csv", "a")

    csvLine = candidatesName + "," + certificationName

    for i in range(len(modules)):
        csvLine = csvLine + "," + modules[i] + "," + str(moduleScores[i])

    csvFile.write(csvLine + "\n")
    csvFile.close()

    logFile = open("processingLog.txt", "a")
    logFile.write(candidatesName + "," + certificationName + "," + overall + "\n")    
    logFile.close()

    print("--------------------------------------------")
    runAgain = input("Do you want to process another candidate? (Y/N): ").upper()
exitMessage()