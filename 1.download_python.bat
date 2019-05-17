md tmp
powershell -Command "Invoke-WebRequest https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe -OutFile ./tmp/python-3.7.2.exe"
powershell -Command "Invoke-WebRequest https://bootstrap.pypa.io/get-pip.py -OutFile ./tmp/get-pip.py"
pause;

