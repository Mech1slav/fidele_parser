import subprocess

file_names = ["simf.py", "sev.py", "yalta.py", "feo.py", "kerch.py", "evp.py"]

for file_name in file_names:
    subprocess.run(["python", file_name])

subprocess.run(["python", 'delite_999_categoryID.py'])
