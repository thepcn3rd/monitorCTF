#!/usr/bin/python

import socket
import time
import ConfigParser
import os
import datetime

# Monitor services that are up every 5 minutes
# Monitor the services on the 5th, 10th etc. minute of the hour
# Configure a start time for the monitoring
# Configure an end time for the monitoring
# Configure ports to monitor pulling from a configuration file
# Scroll with a current update of services that are up or down
# Record the score to a sqlite database
# Generate report from the database of downtime and final score
# Have a weighted score for which services are up


# Main Function
def main():
	# Read config.ini for the settings necessary
	config = ConfigParser.ConfigParser()
	config.read("config.ini")
	# Team Name that this is setup for
	teamName = config.get('Team', 'teamName')
	# Ports to monitor read from config.ini
	monitorPorts = config.get('Team', 'monitorPorts').split(',')
	# Time Interval to wait between monitoring the services
	timeInterval = int(config.get('Team', 'timeInterval'))
	# Log File Directory
	logFile = config.get('Team', 'logFile')
	if os.path.isfile(logFile):
		print "Log File Exists"
	else:
		print "Log Directory does not Exist. Creating " + logFile
		os.system("touch " + logFile)
	totalScore = 0
	while True:
		f = open(logFile, 'a')
		for hostAndPort in monitorPorts:
			items = hostAndPort.split(':')
			host = items[0]
			port = int(items[1])
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			result = s.connect_ex((host,port))
			s.close()
			if result == 0:
				now = datetime.datetime.now()
				csvString = '"1","' + host + '","' + str(port) + '","Up","' + now.strftime("%m-%d-%Y %H:%M:%S") + '"\r\n'
				print csvString.strip()
				f.write(csvString)
				totalScore += 1
			else:
				now = datetime.datetime.now()
				csvString = '"0","' + host + '","' + str(port) + '","Down","' + now.strftime("%m-%d-%Y %H:%M:%S") + '"\r\n'
				print csvString.strip()
				f.write(csvString)
		print 
		print "Team: " + teamName + " Total Score: " + str(totalScore)
		print
		time.sleep(timeInterval)
		f.close()


if __name__ == "__main__":
	main()
