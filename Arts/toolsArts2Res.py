import sys;
import os;

SVN_PATH="..\..\Assets\Arts";
Script = "Arts2Res.py";
UNITY_PROJECT_PATH="..\..";
os.system("python ..\subversion\subversion.py " + SVN_PATH + " " + Script + " " + UNITY_PROJECT_PATH);