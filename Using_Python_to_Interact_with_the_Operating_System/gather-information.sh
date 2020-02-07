
line="--------------------------------------"

echo "Starting at $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE -MB"; free --mega; echo $line

echo "Finishing at: $(date)"
