#   52. ftplib
#   again with server

from ftplib import FTP

#ftp = FTP('domainname.com')
#ftp.login(user='username',passwd='password')
#ftp.cwd('/location/')

def downloadFile():
    fileName = 'fileName.txt'
    localFile = open(fileName,'wb')
    ftp.retrbinary('RETR '+fileName, localFile.write, 1024)
    ftp.quit()
    localFile.close()

def uploadFile():
    fileName = 'fileName.txt'
    ftp.storbinary('STOR '+fileName, open(fileName,'rb'))
