# -*- coding: utf-8 -*-
import dropbox
import glob
from dropbox.files import WriteMode
import sys
import os
from datetime import datetime


with open ('token', 'r') as token:
    oauth_token = token.readline()

print 'Connecting to DB...'
dbx = dropbox.Dropbox(oauth_token)
print 'Done.'

def clean_db_folder():
    dbx.files_delete('/Notes')
    
def clean_local_folder():
    for note in glob.glob('.\Notes\*'):
        os.remove(note)

def create_new_note(title):
    all_files = glob.glob('.\Notes\*.txt')
    for every_file in all_files:
        path = every_file.replace('.\Notes\kek'[0:8], '')
        if path == title+'.txt':
            raise Exception, 'OSHbIBKA, TAKAR ZAMETKA YZHE EST!'
    
    with open ('Notes/'+title+'.txt', 'w') as note:
                date = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
                note.write(date)

def delete_note(title):
    os.remove(title+'.txt')


def upload():
    try:
        clean_db_folder()
    except dropbox.exceptions.ApiError:
        dbx.files_create_folder('/Notes')
        
    all_files = glob.glob('.\Notes\*.txt')
    for every_file in all_files:
        with open (every_file, 'rb') as each_file:
            fpath = every_file.replace('.', '', 1)
            fpath = fpath.replace('\l'[0], '/')
            dbx.files_upload(each_file.read(), fpath, mode=WriteMode('overwrite'))
        


def download():
    clean_local_folder()
    folder_list = dbx.files_list_folder('/Notes')
    ent = folder_list.entries
    for entrie in ent:
        spath = '.\Notes\kek'[0:8]+entrie.name
        print spath
        dbx.files_download_to_file(download_path = spath, path = spath.replace('\k'[0], '/').replace('.', '', 1))
