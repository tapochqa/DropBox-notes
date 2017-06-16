import dropbox
import glob
from dropbox.files import WriteMode
import sys


with open ('token', 'r') as token:
    oauth_token = token.readline()

dbx = dropbox.Dropbox(oauth_token)

def upload():
    all_files = glob.glob('./Notes/*.txt')
    for every_file in all_files:
        with open (every_file, 'rb') as each_file:
            k = each_file.read()
            print k
        
upload()
#def download():
    