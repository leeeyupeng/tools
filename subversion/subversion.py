import sys;
import os;
import commands;

import time;
import datetime

PROJECT_PATH=sys.argv[1];
Script = sys.argv[2];

Version = 1;

while True:

	print datetime.datetime.now()

	lastVersion = Version;

	Path = os.getcwd();
	os.chdir(PROJECT_PATH);
	os.system("svn update");
	strVersion = os.popen("svn info|grep 'Last Changed Rev': |sed 's/Last Changed Rev: //g'").read();
	#print strVersion;
	Version = int(strVersion);
	os.chdir(Path);
	print "LastVersion : "+str(lastVersion) + " Version: " + str(Version);
	if Version > lastVersion:
		os.system("python " + Script + " " + PROJECT_PATH);
		Version = Version;
		# os.system("python subversion.py " + UNITY_PROJECT_PATH + " " + str(lastVersion) + " " + Script);

	time.sleep(3);