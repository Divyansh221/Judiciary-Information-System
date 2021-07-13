import mysql.connector		# Importing MySQL connector
from datetime import date 		# Importing datetime for getting todays date
import datetime

today = date.today()		# Today will denote todays date

class Database:		# Database Class

	def __init__(self):		# Initialization (init function)

		myDB = mysql.connector.connect(
		  host = "localhost",
		  user = "root",
		  password = "Divyansh221",		# MySQL server password
		)

		self.mycursor = myDB.cursor()

		self.myDB = mysql.connector.connect(
		  host = "localhost",
		  user = "root",
		  password = "Divyansh221",		# MySQL server password
		  database = "JIS_Database"		# Connecting to local MySQl server
		)

		self.mycursor = self.myDB.cursor()


	def checkUser(self, username_, password_):		# To check whether a user is present in the database or not

		sql = "SELECT * FROM users WHERE username = %s AND password = %s"
		val = (username_, password_)
		self.mycursor.execute(sql, val)
		myresult = self.mycursor.fetchall()		# To get all users required
		for x in myresult:
			return True				# Returns true or false depending on the output
		return False

	def getNameOfUser(self, username_):			# To get the name of the user from database

		sql = "SELECT * FROM users WHERE username = %s"
		val = (username_, )
		self.mycursor.execute(sql, val)
		myresult = self.mycursor.fetchall()		# To get all users required
		y = ()
		for x in myresult:
			y = x
			return y[2]

	def getTypeOfUser(self, username_):		# To get the type of the user from database

		sql = "SELECT * FROM users WHERE username = %s"
		val = (username_, )
		self.mycursor.execute(sql, val)
		myresult = self.mycursor.fetchall()		# To get all users required
		y = ()
		for x in myresult:
			y = x
			return y[3]


	def ifUserExists(self, username_):		# To check if a user exists in the database

		sql = "SELECT * FROM users WHERE username = %s"
		val = (username_, )
		self.mycursor.execute(sql, val)
		myresult = self.mycursor.fetchall()		# To get all users required
		for x in myresult:
			return True 			# Returns true or false depending on the output
		return False


	def getMoneyOfUser(self, username_):		# To get the money in the wallet of the user from database (Lawyer)

		sql = "SELECT * FROM users WHERE username = %s"
		val = (username_, )
		self.mycursor.execute(sql, val)
		myresult = self.mycursor.fetchall()		# To get all users required
		y = ()
		for x in myresult:
			y = x
			return y[4]

	def AddMoneyToUser(self, username_, money_):		# To add money to the wallet of user (Lawyer)

		myresult = self.mycursor.fetchall()		# To get all users required
		sql = "UPDATE users SET money = %s WHERE username = %s"
		currentMoney = int(self.getMoneyOfUser(username_))
		val = (str(money_ + currentMoney), username_)
		self.mycursor.execute(sql, val)			
		self.myDB.commit()

	def subtractMoney(self,username_):			# To subtract money from the wallet of user (Lawyer)
		
		myresult = self.mycursor.fetchall()		# To get all users required
		sql = "UPDATE users SET money = %s WHERE username = %s"
		currentMoney = int(self.getMoneyOfUser(username_))
		val = (str(currentMoney-5), username_)
		self.mycursor.execute(sql, val)			
		self.myDB.commit()

	def createUser(self, username_, password_, name_, type_, money_="-1"):		# To create new user

		sql = "INSERT INTO users (username, password, name, type, money) VALUES (%s, %s, %s, %s, %s)"
		val = [
		  (username_, password_, name_, type_, str(money_))
		]
		self.mycursor.executemany(sql, val)
		self.myDB.commit()

	def deleteUser(self, username_):		# To delete an existing user

		sql = "DELETE FROM users WHERE username = %s"
		val = (username_, )
		self.mycursor.execute(sql, val)
		self.myDB.commit()

	def deleteDatabase(self):

		self.mycursor.execute("DROP DATABASE JIS_Database")		# To delete the entire database

	def addCase(self, caseDetailsList):		# To add new case to the database

		CIN_ = caseDetailsList[0]
		defendentName_ = caseDetailsList[1]
		defendentAddress_ = caseDetailsList[2]
		crimeType_ = caseDetailsList[3]
		crimeDate_ = caseDetailsList[4]
		crimeLocation_ = caseDetailsList[5]
		officerName_ = caseDetailsList[6]
		arrestDate_ = caseDetailsList[7]
		judgeName_ = caseDetailsList[8]
		lawyerName_ = caseDetailsList[9]
		prosecutorName_ = caseDetailsList[10]
		startingDate_ = caseDetailsList[11]
		caseStatus_ = caseDetailsList[12]
		caseSummary_ = caseDetailsList[13]
		endDate_ = caseDetailsList[14]
		dateOfHearing_ = caseDetailsList[15]
		adjourments_ = ""
		hearings_ = ""
		caseJudgement_ = ""

		for x in caseDetailsList[16]:
			adjourments_ += x[0] + ":" + x[1] + "#"

		for x in caseDetailsList[17]:
			adjourments_ += x[0] + ":" + x[1] + "#"

		sql = "INSERT INTO cases (CIN, defendentName, defendentAddress, crimeType, crimeDate, crimeLocation, officerName, arrestDate, judgeName, lawyerName, prosecutorName, startingDate, caseStatus, caseSummary, endDate, dateOfHearing, adjourments, hearings, caseJudgement) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
		val = (CIN_, defendentName_, defendentAddress_, crimeType_, crimeDate_, crimeLocation_, officerName_, arrestDate_, judgeName_, lawyerName_, prosecutorName_, startingDate_, caseStatus_, caseSummary_, endDate_, dateOfHearing_, adjourments_, hearings_, caseJudgement_, )
		self.mycursor.execute(sql, val)
		self.myDB.commit()

	def getNextCIN(self):		# To get the next CIN, for the new case

		self.mycursor.execute("SELECT * FROM cases ORDER BY CIN DESC LIMIT 1;")
		myresult = self.mycursor.fetchall()		# To get all cases required
		CIN_ = 0
		y = []
		for x in myresult:
			y = list(x)
			CIN_ = y[0]
		return (CIN_ + 1)

	def getCaseStatus(self, CIN_):		# To get status of an existing case

		sql = "SELECT * FROM cases WHERE CIN = %s"
		val = (CIN_, )
		self.mycursor.execute(sql, val)
		myresult = self.mycursor.fetchall()		# To get all cases required
		y = []
		for x in myresult:
			y = list(x)
			return y[12]

	def getproperFormat(self,date_):		# To get proper format of dates
		print(date_)
		day, month, year = date_.split('/')
		day = int(day)
		month = int(month)
		year = int(year)

		temp = ""
		temp = str(day)+"/"+str(month)+"/"+str(year)
		return temp

	def updateCase(self, updatedCaseDetailsList):		# To update an existing case

		adjourments_ = ""
		hearings_ = ""

		for x in updatedCaseDetailsList[16]:
			adjourments_ += x[0] + ":" + x[1] + "#"

		for x in updatedCaseDetailsList[17]:
			hearings_ += x[0] + ":" + x[1] + "#"

		sql = """UPDATE cases SET defendentName = %s, defendentAddress = %s, crimeType = %s, crimeDate = %s, crimeLocation = %s, officerName = %s, arrestDate = %s, judgeName = %s, lawyerName = %s, prosecutorName = %s, startingDate = %s, caseStatus = %s, caseSummary = %s, endDate = %s, dateOfHearing = %s, adjourments = %s, hearings = %s, caseJudgement = %s WHERE CIN = %s;"""
		val = (updatedCaseDetailsList[1], updatedCaseDetailsList[2], updatedCaseDetailsList[3], updatedCaseDetailsList[4], updatedCaseDetailsList[5], updatedCaseDetailsList[6], updatedCaseDetailsList[7], updatedCaseDetailsList[8], updatedCaseDetailsList[9], updatedCaseDetailsList[10], updatedCaseDetailsList[11], updatedCaseDetailsList[12], updatedCaseDetailsList[13], updatedCaseDetailsList[14], updatedCaseDetailsList[15], adjourments_, hearings_, updatedCaseDetailsList[18], updatedCaseDetailsList[0])
		self.mycursor.execute(sql, val)
		self.myDB.commit()

	def transformCases(self, myCase):		# Involving transformations of hearings and adjourments b/w list and string

		adjourments_ = []
		hearings_ = []
		myString = ""
		y = []
		for ch in myCase[16]:
			if ch == ':':
				y.append(myString)
				myString = ""
				continue
			if ch == '#':
				y.append(myString)
				adjourments_.append(y)
				y = []
				myString = ""
				continue
			myString += ch

		y = []
		for ch in myCase[17]:
			if ch == ':':
				y.append(myString)
				myString = ""
			if ch == '#':
				y.append(myString)
				hearings_.append(y)
				y = []
				myString = ""
			myString += ch

		return adjourments_, hearings_

	def getCaseByCIN(self, CIN_):		# Get all cases identified by CIN

		sql = "SELECT * FROM cases WHERE CIN = %s"
		val = (CIN_, )
		self.mycursor.execute(sql, val)
		myresult = self.mycursor.fetchall()		# To get all cases required
		requiredCase = []
		for x in myresult:
			requiredCase = list(x)
		requiredCase[16], requiredCase[17] = self.transformCases(requiredCase)
		return requiredCase

	def getCaseByStatus(self, status_):		# Get all cases identified by status

		sql = "SELECT * FROM cases WHERE caseStatus = %s"
		val = (status_, )
		self.mycursor.execute(sql, val)
		myresult = self.mycursor.fetchall()		# To get all cases required
		requiredCases = []
		for x in myresult:
			y = list(x)
			y[16], y[17] = self.transformCases(y)
			requiredCases.append(y)
		return requiredCases

	def getCaseByCrimeType(self, crimeType_):			# Get all cases identified by crime type

		sql = "SELECT * FROM cases WHERE crimeType = %s"
		val = (crimeType_, )
		self.mycursor.execute(sql, val)
		myresult = self.mycursor.fetchall()		# To get all cases required
		requiredCases = []
		for x in myresult:
			y = list(x)
			y[16], y[17] = self.transformCases(y)
			requiredCases.append(y)
		return requiredCases

	def getCaseByKeyword(self, keyword):		# Get all cases identified by keyword matching from any detail in any cases

		sql = "SELECT * FROM cases WHERE defendentName LIKE %s OR defendentAddress LIKE %s OR crimeType LIKE %s OR crimeDate LIKE %s OR crimeLocation LIKE %s OR officerName LIKE %s OR arrestDate LIKE %s OR judgeName LIKE %s OR lawyerName LIKE %s OR prosecutorName LIKE %s OR startingDate LIKE %s OR caseStatus LIKE %s OR caseSummary LIKE %s OR endDate LIKE %s OR dateOfHearing LIKE %s OR adjourments LIKE %s OR hearings LIKE %s OR caseJudgement LIKE %s"
		val = ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', )
		self.mycursor.execute(sql, val)
		myresult = self.mycursor.fetchall()		# To get all cases required
		requiredCases = []
		for x in myresult:
			y = list(x)
			y[16], y[17] = self.transformCases(y)
			requiredCases.append(y)
		return requiredCases

	def getCaseByDateOfHearing(self, dateOfHearing_):		# Get all cases identified by date of hearing

		day2, month2, year2 = dateOfHearing_.split('/')
		day2 = int(day2)
		month2 = int(month2)
		year2 = int(year2)

		requiredCases = []

		sql = "SELECT * FROM cases"
		self.mycursor.execute(sql)
		myresult = self.mycursor.fetchall()		# To get all cases required

		y = []
		for x in myresult:
			y = list(x)
			try:
				day, month, year = y[15].split('/')
			except ValueError:
				continue
			day = int(day)
			month = int(month)
			year = int(year)
			if day == day2 and year == year2 and month == month2:
				requiredCases.append(y)

		return requiredCases

	def verifyDatefromToday(self, dateOfHearing_):		

		try:
			day, month, year = dateOfHearing_.split('/')
		except ValueError:	
			return False 		# Returns true or false depending on the output

		try :
		    datetime.datetime(int(year),int(month),int(day))
		except ValueError :
		    return False 		# Returns true or false depending on the output

		day_ = int(today.strftime("%d"))
		month_ = int(today.strftime("%m"))
		year_ = int(today.strftime("%Y"))
		
		if int(day) < day_ or int(month) < month_ or int(year) < year_:
			return False 		# Returns true or false depending on the output
		return True

	def verifyDatebeforeToday(self, dateOfHearing_):

		try:
			day, month, year = dateOfHearing_.split('/')
		except ValueError:
			return False 		# Returns true or false depending on the output

		try :
		    datetime.datetime(int(year),int(month),int(day))
		except ValueError :
		    return False

		day_ = int(today.strftime("%d"))
		month_ = int(today.strftime("%m"))
		year_ = int(today.strftime("%Y"))
		
		if int(day) > day_ and int(month) > month_ and int(year) > year_:
			return False 		# Returns true or false depending on the output
		return True

	def verifyDate(self, dateOfHearing_):

		try:
			day, month, year = dateOfHearing_.split('/')
		except ValueError:
			return False

		try :
		    datetime.datetime(int(year),int(month),int(day))
		except ValueError :
		    return False 		# Returns true or false depending on the output

		return True

	def getEmptySlots(self, dateOfHearing_):		# Get Empty slots on a given date

		dateOfHearing_ = self.getproperFormat(dateOfHearing_)
		sql = "SELECT * FROM slots WHERE date = %s"
		val = (dateOfHearing_, )
		self.mycursor.execute(sql, val)
		myresult = self.mycursor.fetchall()
		requiredSlots = []
		count = 0
		for x in myresult:
			count += 1
		if count == 0:
			sql = "INSERT INTO slots (date) VALUES (%s)"
			val = (dateOfHearing_, )
			self.mycursor.execute(sql, val)
			self.myDB.commit()

		sql = "SELECT * FROM slots WHERE date = %s"
		val = (dateOfHearing_, )
		self.mycursor.execute(sql, val)
		myresult = self.mycursor.fetchall()		# To get all slots required
		y = []
		for x in myresult:
			y = list(x)
			if y[1] == 0:
				requiredSlots.append(0)
			if y[2] == 0:
				requiredSlots.append(1)
			if y[3] == 0:
				requiredSlots.append(2)
			if y[4] == 0:
				requiredSlots.append(3)
			if y[5] == 0:
				requiredSlots.append(4)
			if y[6] == 0:
				requiredSlots.append(5)

		return requiredSlots		

	def updateSlots(self, dateOfHearing_, slotUsed):		# update slots in the database

		dateOfHearing_ = self.getproperFormat(dateOfHearing_)
		if slotUsed == 0:
			sql = "UPDATE slots SET slot1 = 1 WHERE date = %s"
		if slotUsed == 1:
			sql = "UPDATE slots SET slot2 = 1 WHERE date = %s"
		if slotUsed == 2:
			sql = "UPDATE slots SET slot3 = 1 WHERE date = %s"
		if slotUsed == 3:
			sql = "UPDATE slots SET slot4 = 1 WHERE date = %s"
		if slotUsed == 4:
			sql = "UPDATE slots SET slot5 = 1 WHERE date = %s"
		if slotUsed == 5:
			sql = "UPDATE slots SET slot6 = 1 WHERE date = %s"
		val = (dateOfHearing_, )
		self.mycursor.execute(sql, val)
		self.myDB.commit()

	def getAllCasesBetweenTwoDates(self, date1, date2):		# Get all cases between two dates

		day1, month1, year1 = date1.split('/')
		day1 = int(day1)
		month1 = int(month1)
		year1 = int(year1)

		day2, month2, year2 = date2.split('/')
		day2 = int(day2)
		month2 = int(month2)
		year2 = int(year2)

		requiredCases = []

		sql = "SELECT * FROM cases"
		self.mycursor.execute(sql)
		myresult = self.mycursor.fetchall()		# To get all cases required

		y = []
		for x in myresult:
			y = list(x)
			try:
				day, month, year = y[14].split('/')
			except ValueError:
				continue
			day = int(day)
			month = int(month)
			year = int(year)
			if year >= year1 and year <= year2:
				if month >= month1 and month <= month2:
					if day >= day1 and day <= day2:
						y[16], y[17] = self.transformCases(y)
						requiredCases.append(y)

		return requiredCases