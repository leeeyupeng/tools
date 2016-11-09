import sys;
import os;

PROJECT_NAME="KOL";
SVN_PATH="../..";
Script = "buildIPAForsvn.py";
UNITY_PROJECT_PATH="../..";
os.system("python ..\subversion\subversion.py " + SVN_PATH + " " + Script + " " + UNITY_PROJECT_PATH + " " + PROJECT_NAME);
