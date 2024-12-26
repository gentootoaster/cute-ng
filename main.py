import subprocess

network = "TAPOCHEK"
password = "limp0p0269"

subprocess.run(["nmcli", "device", "wifi", "connect", network, "password", password]) 