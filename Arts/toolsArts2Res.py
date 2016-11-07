import sys;
import os;

Script = "Arts2Res.py";
UNITY_PROJECT_PATH="..\..";
os.system("python ..\subversion\subversion.py " + UNITY_PROJECT_PATH + " " + Script);