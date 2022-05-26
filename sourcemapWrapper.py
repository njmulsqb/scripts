import sys
import subprocess
import os

print(sys.argv[1])
parentDir = 'sourceMapsToJS'
sourceMapURL = sys.argv[1]
dirName = sourceMapURL.strip(
    'https://').strip('http://').strip('www.').replace('/', '-').replace('.', '-')
print(dirName)
if not os.path.exists(parentDir):
    os.mkdir(parentDir)
os.chdir(parentDir)
subprocess.call(['sourcemapper', '-url', sourceMapURL, '-output', dirName])
