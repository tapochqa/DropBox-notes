import dropbox

with open ('token', 'r') as token:
    oauth_token = token.readlines()

print oauth_token