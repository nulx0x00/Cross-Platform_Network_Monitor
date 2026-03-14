import subprocess
import platform

if platform.system().lower() == "windows":
    flag = "-n"
else:
    flag = "-c"

with open("target.txt", "r") as file:
    for line in file:
        try:
            command = f"ping {flag} 1  {line.strip()} "
            print(f"checking......  {line.strip()}")
            result = subprocess.run(command, shell = True, capture_output=True, text = True, timeout=2 )
            if result.returncode == 0:
                print(f" [+] {line.strip()} is up ")
            else :
                print (f" [-] {line.strip()} is down")
                print(f"DEBUG: {result.stderr}")
        except subprocess.TimeoutExpired:
            print(f" [-] {line.strip()} is down (Timed Out)")
