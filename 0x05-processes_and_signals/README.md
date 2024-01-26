In this project, We take a look at  handling process ID's and signals in Bash with ps, pgrep, pkill, pkill, exit, and trap.

0-what-is-my-pid: Bash script that displays its own PID.

1-list_your_processes: Bash script that displays a list of currently running processes.

2-show_your_bash_pid: Bash script that displays lines containing the bash keyword based on the script defined in 1-list_your_processes.

3-show_your_bash_pid_made_easy: Bash script that displays the PID along with the process name of processes who name contains the word bash.

4-to_infinity_and_beyond: Bash script that displays To infinity and beyond indefinitely with a sleep 2 in between each iteration.

5-dont_stop_me_now: Bash script that kills the 4-to_infinity_and_beyond process using kill.

6-stop_me_if_you_can: Bash script that kills the 4-to_infinity_and_beyond process using pkill.

7-highlander: Bash script that displays To infinity and beyond indefinitely with a sleep 2 in between each iteration.

8-beheaded_process: Bash script that kills the process 7-highlander.

manage_my_process: Bash script that writes I am alive! to the file /tmp/my_process indefinitely.
Sleeps two seconds in between each write.

101-manage_my_process: Bash script that manages the manage_my_process script.
When passed the argument start:
Starts manage_my_process.
Creates a file containing its PID in /var/run/my_process.pid.
Displays manage_my_process started.
When passed the argument stop:
Stops manage_my_process.
Deletes the file /var/run/my_process.pid.
Displays manage_my_process stopped.
When passed the argument restart:
Stops manage_my_process.
Deletes the file /var/run/my_process.pid.
Starts manage_my_process.
Creates a file containing its PID in /var/run/my_process.pid.
Displays manage_my_process started.
Otherwise, displays Usage: manage_my_process {start|stop|restart}.

102-zombie.c: C program that creates five zombie processes.

