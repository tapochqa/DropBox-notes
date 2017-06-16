# -*- coding: utf-8 -*-
import dropbox
import glob
from dropbox.files import WriteMode
import sys


with open ('token', 'r') as token:
    oauth_token = token.readline()

dbx = dropbox.Dropbox(oauth_token)



def upload():
    all_files = glob.glob('.\Notes\*.txt')
    for every_file in all_files:
        with open (every_file, 'rb') as each_file:
            fpath = every_file.replace('.', '', 1)
            fpath = fpath.replace('\l'[0], '/')
            dbx.files_upload(each_file.read(), fpath, mode=WriteMode('overwrite'))
        


#def download():
    