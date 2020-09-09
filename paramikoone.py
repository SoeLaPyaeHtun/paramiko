import paramiko



p = paramiko.SSHClient()
p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
p.connect("192.168.1.12", port=22, username="root", password="   ")
stdin, stdout, stderr = p.exec_command("ls -al")

out = stdout.readlines()
out = "".join(out)
print(out)