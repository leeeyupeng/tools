import sys;
import os;
import commands;

import time;
import datetime

SVN_PATH=sys.argv[1];
Script = sys.argv[2];
PROJECT_PATH = sys.argv[3];

argv = sys.argv;
argv.pop(0);
print " ".join(sys.argv);

Version = 1;

while True:

	print datetime.datetime.now();

	lastVersion = Version;

	Path = os.getcwd();
	os.chdir(PROJECT_PATH);
	os.system("svn update");
	os.chdir(Path);
	os.chdir(SVN_PATH);
	os.system("svn update");
	strVersion = os.popen("svn info|grep 'Last Changed Rev': |sed 's/Last Changed Rev: //g'").read();
	Version = int(strVersion);
	#print "lastVersion : " + lastVersion + "  " + "current Version : " + Version;
	os.chdir(Path);
	print "LastVersion : "+str(lastVersion) + " Version: " + str(Version);
	if Version > lastVersion:
		os.system("python " + Script + " " + " ".join(argv) + " " + str(Version))
		Version = Version;
		# os.system("python subversion.py " + UNITY_PROJECT_PATH + " " + str(lastVersion) + " " + Script);

	time.sleep(3);
	
	#break;