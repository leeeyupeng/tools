import sys
import os;
import commands;


print "Arts2Res"
#UNITY_PROJECT_PATH="..";
UNITY_PROJECT_PATH=sys.argv[1];

UNITY='"C:\Program Files\Unity5.4\Editor\Unity.exe"';

Path = os.getcwd();
os.chdir(UNITY_PROJECT_PATH);

# os.system("ls")
print UNITY+" -quit -batchmode -executeMethod ActorEditor.AutoGen Start";
os.system(UNITY+" -quit -batchmode -executeMethod ActorEditor.AutoGen");
print UNITY+" -quit -batchmode -executeMethod ActorEditor.AutoGen  End";
os.system('cd Assets/Resources/Arts && svn add * --force && svn ci -m "KOL ArtsRes"');
os.system('cd Assets/Project/Arts && svn add * --force && svn ci -m "KOL ArtsRes"');
os.chdir(Path);