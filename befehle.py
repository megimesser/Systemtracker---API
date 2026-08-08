BEFEHLSKETTE = ["df -h","free -h","uptime","docker ps --format '{{json .}}'","vcgencmd measure_temp","hostnamectl"]
BEFEHLSKETTE_PIPE = ["ps aux --sort=-%mem | head -10","ps aux --sort=-%cpu | head -10"]
