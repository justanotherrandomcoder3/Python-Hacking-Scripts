import socket 
import os





while True:
    socket.socket(os.__file__("C:","\Windows","\Users","\mm341307@aldine-isd.org","\MyFiles","\DLLInjections","\main.py"))
socket.socket(os.__file__("C:","\Windows","\Users","\mm341307@aldine-isd.org","\Myfiles","\Downloads","\crackme.txt"))
dll = memoryview(os.__file__("C:","\Windows","\Users","\mm341307@aldine-isd.org","\MyFiles","\DLLInjections","\main.py"))
target = memoryview(os.__file__("C:","\Windows","\Users","\mm341307@aldine-isd.org","\Myfiles","\Downloads","\crackme.txt"))

socket.socket(dll, target)
socket.send(os.__file__("C:","\Windows","\Users","\mm341307@aldine-isd.org","\Myfiles","\DLLInjections","\injector.py")) *[target]

