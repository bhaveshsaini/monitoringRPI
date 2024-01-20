<b>Script to send an email everytime there's a new connection to your RPI such as SSH or NAS server. </b>

- Create a file in the same directory as the script named "config.py" with the following values:<br> 
sender(your email)<br> receiver(your email)<br> username(email)<br> password(email password)

- Run the script using<br>
*nohup ./tail.sh &*

- It will run in the background. It will send an email if there's a new SSH connection or a new Samba server connection to your PI.
- To terminate the script, find the process ID for the script using the following command:<br>
*ps aux | grep tail.sh*<br>
Then use the following command to terminate the process:<br>
*kill -15 <process_id>*
