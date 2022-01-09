import io
import subprocess
import paramiko

cmd = "vagrant ssh-config vagrant2"
p = subprocess.Popen(cmd.split(), stdin=None,
                     stdout=subprocess.PIPE, stderr=None)
config = paramiko.SSHConfig()
config.parse(io.StringIO(p.stdout.read().decode('UTF-8')))
config.lookup("vagrant2")
# print(config.lookup("vagrant2"))
