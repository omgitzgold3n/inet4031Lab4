import os
import re
import sys

def main():
	for line in sys.stdin:
		match = line.split(':') #This will be used to split the line into parts --> an array called match
		if re.search("^#", match[0]):
			print(match[0][1:6], "is skipped because it starts with a hashtag (is commented out)") #This will print out the error message for the user with a # in the front
		fields = line.strip().split(':')
		if match or len(fields) != 5: #this checks if the match was found or there aren't 5 sperate parts in the user's list, then the continue causes the loop to go back to the beginning of the loop to continue checking for those errors in the beginning if statement
			continue
		username = fields[0]
		password = fields[1]
		
		gecos = "%s %s,,," % (fields[3],fields[2])
		groups = fields[4].split(',') #this creates an array with the fourth index at the colon

		print("==> Creating account for %s..." % (username))
		cmd = "/usr/sbin/adduser --disabled-password --gecos 's%' %s" % (gecos,username)

		#print cmd
		os.system(cmd) #Uses cmd as the argument for using os, which tells the program to execute cmd. 

		print("==> Setting the password for %s..." % (username))
		cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
		#print(cmd)
		os.system(cmd)
		for group in groups: #this for loop is iterating though the groups at each group at a time
			if group != '-':
				print("==> Assigning %s to the %s group..." % (username,group))
				cmd = "/usr/sbin/adduser %s %s" % (username,group)
				#print cmd
				os.system(cmd)

if __name__ == '__main__':
	main()
