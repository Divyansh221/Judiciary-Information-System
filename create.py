from Databases import Database 		# Importing Database class from Database folder

# passwo = input("Enter the password for you SQL database: ")
database = Database()			# Database type object creation

database.createUser("Sharma","Sharma1234","Sharma","jud")			# Creating a Judge
database.createUser("jeff","community","Jeff Winger","law","100")	# Creating a Laywer

# myfile = [database.getNextCIN(),"John Doe","America","Sexual Assault","22/3/2021",
# "India","Esha Manideep","22/3/2021","Sharma","Jeff Winger","Amartya Mandal","5/4/2021","Pending",
# "","","15/04/2021",[["11/4/2021","Suck it sorangshu"]],[["12/4/2021","Fuck you deep"]],""]
# database.addCase(myfile)