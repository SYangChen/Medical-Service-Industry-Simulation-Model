exec python3 main.py
ps -ef | grep "python3 main.py" | awk  '{print $2}' | python3 -c "print(input())"
kill -9 $(!!)
respawn