import sys
import subprocess
import os

parentDir = 'sourceMapsToJS'
sourceMapURL = sys.argv[1]
dirName = sourceMapURL.strip(
    'https://').strip('http://').strip('www.').replace('/', '-').replace('.', '-')
if not os.path.exists(parentDir):
    os.mkdir(parentDir)
os.chdir(parentDir)
subprocess.call(['sourcemapper', '-url', sourceMapURL, '-output', dirName])
