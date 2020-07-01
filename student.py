import os
import platform

global listStd 
listStd = ["Akash", "Ashwin", "Muthu", "Gowtham","Deena"]

def manageStudent(): 
	print(""" 

 ********************************************************
 */\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\* 
 *        WELCOME TO STUDENT MANAGEMENT SYSTEM	        *
 */\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\*
 ********************************************************

Enter 1 : To View Student's List 
Enter 2 : To Add New Student 
Enter 3 : To Search Student 
Enter 4 : To Remove Student 
		""")

	try: 
		userInput = int(input("Please Select An Above Option: ")) 
	except ValueError:
		exit("\nHy! That's Not A Number") 
	else:
		print("\n") 

        
	if(userInput == 1): 
		print("List of Students\n")
		i=1
		for students in listStd:
			print("{} => {}".format(i,students))
			i+=1

	elif(userInput == 2): 
		newStd = input("Enter New Student: ")
		newStd = newStd.title()
		i=1
		if(newStd in listStd): 
			print("\nThis Student {} Already In The Database".format(newStd))  
		else:	
			listStd.append(newStd)
			print("\n=> New Student {} Successfully Added \n".format(newStd))
			for students in listStd:
				print("{} => {}".format(i,students))
				i+=1

	elif(userInput == 3): 
		srcStd = input("Enter Student Name To Search: ")
		srcStd = srcStd.title()
		if(srcStd in listStd): 
			print("\n=> {} - Record Found".format(srcStd))
		else:
			print("\n=> {} - No Record Found".format(srcStd)) 

	elif(userInput == 4): 
		rmStd = input("Enter Student Name To Remove: ")
		rmStd = rmStd.title()
		i=1
		if(rmStd in listStd): 
			listStd.remove(rmStd)
			print("\n=> Student {} Successfully Deleted \n".format(rmStd))
			for students in listStd:
				print("{} => {}".format(i,students))
				i+=1
		else:
			print("\n=> No Record Found of This Student {}".format(rmStd)) 
	 
	elif(userInput < 1 or userInput > 4): 
		print("Please Enter Valid Option")	
						
def runAgain(): 
	runAgn = input("\nDo you Want To Run Again Y/n: ")
	if(runAgn.lower() == 'y'):
		if(platform.system() == "Windows"): 
			print(os.system('cls')) 
		else:
			print(os.system('clear'))
		manageStudent()
		runAgain()

manageStudent()
runAgain()		
