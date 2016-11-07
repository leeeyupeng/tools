def FtpUpload(localPath, ftpPath, user="", pwd=""):
    """
    """
	dirs = str(ftpPath).split("/")
    if len(dirs) < 4:
        return False
    if str(dirs[2]).count(".") != 3:
        return False
    server = dirs[2]
    srcFile = ""
    for item in dirs[3:]:
        srcFile += "/" + str(item)
 
    try:
        f = FTP(server)
        try:
            f.login(user, pwd)
            localFile = open(localPath, "rb")
            f.storbinary("STOR %s" % srcFile, localFile)
            localFile.close()
            f.quit()
            return True
        except:
            f.quit()
            return False
    except:
        return False
 
def FtpDownLoad(ftpFile, savePath, user="", pwd=""):
    dirs = str(ftpFile).split("/")
    if len(dirs) < 4:
        return False
    server = dirs[2]
    srcFile = ""
    for item in dirs[3:]:
        srcFile += "/" + str(item)
    try:
        ftp = FTP()
        ftp.connect(server, '21')
        ftp.login(user, pwd)
        ftp.cwd(os.path.dirname(srcFile).lstrip("/")) #选择操作目录
        file_handler = open(savePath,'wb') #以写模式在本地打开文件
        ftp.retrbinary('RETR %s' % os.path.basename(srcFile),file_handler.write)#接收服务器上文件并写入本地文件
        file_handler.close()
        ftp.quit()
    except:
        print traceback.format_exc()
