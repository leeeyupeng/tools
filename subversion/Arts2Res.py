import sys
import os;
import commands;


print "Arts2Res"
UNITY_PROJECT_PATH="E:\DevArts\KnightOfLight";

UNITY='"C:\Program Files\Unity5.4\Editor\Unity.exe"';

Path = os.getcwd();
os.chdir(UNITY_PROJECT_PATH);

# os.system("ls")
print UNITY+" -quit -batchmode -executeMethod ActorEditor.AutoGen Start";
os.system(UNITY+" -quit -batchmode -executeMethod ActorEditor.AutoGen");
print UNITY+" -quit -batchmode -executeMethod ActorEditor.AutoGen  End";
os.system('cd Assets/Resources/Arts && svn add * --force && svn ci -m "KOLArtsRes"');
os.system('cd Assets/Project/Arts && svn add * --force && svn ci -m "KOLArtsRes"');
os.chdir(Path);