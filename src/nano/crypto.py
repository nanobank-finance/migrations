
import subprocess

def generate_private_key():
    command = "LC_ALL=C cat /dev/urandom | LC_ALL=C tr -dc '0-9A-F' | LC_ALL=C head -c${1:-64}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    return process.stdout.read()
