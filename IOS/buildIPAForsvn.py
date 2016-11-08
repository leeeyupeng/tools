import os;
import sys;
PROJECT_NAME=sys.argv[4];
PROJECT_PATH=sys.argv[3];
SVN_VERSION = sys.argv[5];

print "sh autoIPA.sh "+PROJECT_NAME+ " " + SVN_VERSION; 
os.system("sh autoIPA.sh " + PROJECT_NAME + " " + SVN_VERSION);
