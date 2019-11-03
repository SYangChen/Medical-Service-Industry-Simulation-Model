#!/bin/bash
# by Sophie Chen

exec python3 main.py &

CPU_usage = 97.0

for i in {1..10};
do
	current_usage = 0.0

	while ["$current_usage" -le $CPU_usage]
	do
		current_usage=$(top -bn2 | grep "python3" | awk '{print $9}' | python3 -c "print(input())")
		echo ${current_usage}
	done

	sudo kill -9 $(ps -ef | grep "python3 main.py" | awk  '{print $2}' | python3 -c "print(input())")
	echo "Kill main.py"
	exec python3 main.py &
done