#! /bin/bash
last_output=""

while true; do
    # store output of the current state of file
    current_output=$(tail -n 1 /var/log/auth.log)

    if [ "$current_output" != "$last_output" ]; then
        # get the list of active SSH connections
        ssh_conn=$(ss | grep -i ssh)

        # get the list of samba connections
        samba_conn=$(sudo smbstatus)

        # send the output of both to the script
        python3 script.py "$current_output" "$ssh_conn" "$samba_conn"
        last_output=$current_output
    fi
    
    # Uncomment so it checks the log file every 30 seconds or adjust it to your timing
    # sleep 30
done
