'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members
    
    This function should remove all rows from currentMem containing 'no' 
    in the 'Active' column and appends them to exMem.
    '''
def cleanFiles(currentMem, exMem):
    
    # TODO: Open the currentMem file as in r+ mode
    with open(currentMem,'r+') as writefile:
        #TODO: Open the exMem file in a+ mode
        with open(exMem,'a+') as appendfile:
            #get the data
            #return the pointer to the beginning
            writeFile.seek(0)
            members = writeFile.readlines()
            #remove header
            header = members[0]
          
            members.pop(0)
            #check in member if is active or not
            inactive = [member for member in members if ('no' in member)]
            #again return the pointer to the beginning
            writeFile.seek(0) 
            #add the header again
            writeFile.write(header)
            #move the members where belong
            for member in members:
                if (member in inactive):
                    appendFile.write(member)
                else:
                    writeFile.write(member)    
            #remove any leftover data
            writeFile.truncate()

# The code below is to help you view the files.
# Do not modify this code for this exercise.
memReg = '/members.txt'
exReg = '/inactive.txt'
cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
