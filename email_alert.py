import os
import glob
import time
import subprocess

#os.system("echo "this is a test" | ssmtp -s Subject projas@utexas.edu")
subprocess.call(" ./email.sh", shell=True)
