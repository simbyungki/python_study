import mysql.connector

dbconn = mysql.connector.connect(host='220.118.169.9', user='aptest', passwd='xptmxm1024#', database='APDB', port='1433')

dbconn.close()


def select (query, bufferd=True) : 
	global dbconn
	cursor = dbconn.cursor(buffered=bufferd)
	cursor.execute(query)


