from threading import Thread
from pathlib import Path
import shutil
import sys

files_copied = 0
source = 0
dist = Path("dist")

def exits(str):
    print(str)
    exit()

def create_thread(func, args: tuple):
    thread = Thread(target=func, args=args)
    thread.run()

def process_file(file: Path):
    if(file.is_file()):
        dest = dist / file.suffix.replace('.', "", 1)
        dest.mkdir(exist_ok=True)
        shutil.copy(str(file), dest)
        files_copied += 1
    elif(file.is_dir()):
        for path in file.iterdir():
            create_thread(process_file, (path,))

if(len(sys.argv) == 1):
    exits("No arguments entered!")
elif(len(sys.argv) == 3):
    dist = Path(sys.argv[2])    
    if(not dist.is_dir()):
        exits("Destination is not a directory!")
dist.mkdir(exist_ok=True)

try:
    source = Path(sys.argv[1])
    if(not source.is_dir()):
        exits("Source is not a directory!")
    if(not source.exists()):
        exits("Source does not exist!")
    process_file(source)


except Exception as e:
    print(e)

print(f"Done!\nFiles processed:{files_copied}")