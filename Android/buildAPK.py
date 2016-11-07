import sys;
import os;
import commands;
import ftp;
import datetime;
import time;
import os.path;

print sys.argv;
PROJECT_NAME=sys.argv[4];

PROJECT_PATH=sys.argv[3];

SVN_VERSION = sys.argv[5];

PROJECT_TARGET="Android/Debug"
 
UNITY_PATH='"C:\Program Files\Unity5.4\Editor\Unity.exe"'; 
 
ECLIPSE_PROJECT_PATH=PROJECT_PATH

Path = os.getcwd();
os.chdir( PROJECT_PATH)
print "gen eclipse project";
print PROJECT_NAME;
#os.system(UNITY_PATH + " -quit -batchmode -executeMethod ProjectBuildAndroid.BuildForEclipse project-" + PROJECT_TARGET)
os.chdir(Path);

print "gen ipa";
Path = os.getcwd();
print os.getcwd()
os.chdir( ECLIPSE_PROJECT_PATH)
print os.getcwd()
os.chdir( PROJECT_TARGET)
print os.getcwd()
os.chdir( PROJECT_NAME)
print os.getcwd()

os.system("android.bat update project --name " + PROJECT_NAME + ' --path ""')

os.system("ant debug");
print os.getcwd()
os.chdir("bin");
print os.getcwd()
apkName = "KOLv%st%s.apk"%(SVN_VERSION, time.strftime("%Y%m%d%H%M%S", time.localtime()) );
print apkName
os.rename("KOL-debug.apk",apkName);
ftp.ftp_up(apkName,"liyupeng/Android/" + apkName);

os.chdir(Path);



