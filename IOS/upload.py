import sys;
import os;
import commands;
import ftp;
import datetime;
import time;
import os.path;


sourceFile=sys.argv[1];
targetFile=sys.argv[2];
ftp.ftp_up(sourceFile,"liyupeng/iPhone/" + targetFile);