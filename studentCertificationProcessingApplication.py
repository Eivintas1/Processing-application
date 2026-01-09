
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
    if numberOfmodules == 0:
        return 0
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
        validInput = False
        while validInput == False:
            try:
                scores = int(input(f"Enter score for {modules[i]}: "))
                validInput = True
            except ValueError:
                print("Invalid input. Please enter a Number.")

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

    allmodulesPassed = True

    for i in range(len(modules)):
        if result(moduleScores[i]) == 'Fail':
            allmodulesPassed = False
            break

    if allmodulesPassed ==True:
        overall = 'Pass'
    else:
        overall = 'Fail'

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

    try:
        csvFile = open("results.csv", "a")

        csvLine = candidatesName + "," + certificationName

        for i in range(len(modules)):
            csvLine = csvLine + "," + modules[i] + "," + str(moduleScores[i])

        csvFile.write(csvLine + "\n")
        csvFile.close()
    except:
        print("Error: Could not write to results.csv file.")

    try:
        logFile = open("processingLog.txt", "a")
        logFile.write(candidatesName + "," + certificationName + "," + overall + "\n")    
        logFile.close()
    except:
        print("Error: Could not write to processingLog.txt file.")

    print("--------------------------------------------")
    validChoice = False
    while validChoice == False:
        runAgain = input("Do you want to process another candidate? (Y/N): ").upper()
        if runAgain == 'Y' or runAgain == 'N':
            validChoice = True
        else:
            print("Invalid choice. Please enter Y or N.")

exitMessage()