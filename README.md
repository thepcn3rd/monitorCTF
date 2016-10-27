# monitorCTF
Monitor Ports on Hosts and Score for a Simple CTF Scoring Engine.

Place the monitor.py and the config.ini file in a directory respective to each team.
Change the permissions on monitor.py as the root user by running 'chmod 700 monitor.py'
Then execute the monitor.py for each respective team and let it run in its own terminal window.
To execute change to the directory cd /home/temp/teamA and then execute ./monitor.py &
The & will send it to the background in the event the terminal window closes it will continue to run
From another terminal window in you can do tail -f runningScore.csv to see it in close to real-time if the terminal window dies

Copy or email runningScore.csv to a device that can process a csv file and then you can tally or adjust scores based on what you see in the csv and you can use Excel formulas to sum the columns.  You could also provide the teams with the log if they requested it.
