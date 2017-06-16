import dropbox
from dropbox.files import WriteMode
import sys


with open ('token', 'r') as token:
    oauth_token = token.readline()

dbx = dropbox.Dropbox(oauth_token)

with open ('check.txt', 'rb') as ofile:
    dbx.files_upload(ofile.read(), '/check.txt', mode = WriteMode('overwrite'))
