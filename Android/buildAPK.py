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

# if os.path.exists(PROJECT_TARGET):
	# print "exits";
# else:
	# print "not exits";
	# os.makedirs(PROJECT_TARGET)
	
print "gen eclipse project";
print os.getcwd();
print PROJECT_TARGET
#quit();
os.system(UNITY_PATH + " -quit -batchmode -projectPath " + os.getcwd() + " -executeMethod ProjectBuildAndroid.BuildForEclipse project-" + PROJECT_TARGET)
os.chdir(Path);

print "gen ipa";
Path = os.getcwd();
print os.getcwd()
os.chdir( ECLIPSE_PROJECT_PATH)
print os.getcwd()
	
os.chdir( PROJECT_TARGET)
print os.getcwd()

# if os.path.exists(PROJECT_NAME):
	# print "exits";
# else:
	# print "not exits";
	# os.makedirs(PROJECT_NAME)
	
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



