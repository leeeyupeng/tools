#!/bin/sh
 
#�����ж�  
if [ $# != 1 ];then  
    echo "��Ҫһ�������� ��������Ϸ��������"  
    exit     
fi  
 
#UNITY�����·��#
UNITY_PATH=/Applications/Unity/Unity.app/Contents/MacOS/Unity
 
#��Ϸ����·��#
PROJECT_PATH=/Users/MOMO/commond
 
#IOS����ű�·��#
BUILD_IOS_PATH=${PROJECT_PATH}/Assets/buildios.sh
 
#���ɵ�Xcode����·��#
XCODE_PATH=${PROJECT_PATH}/$1
 
#��unity������xcode����#
$UNITY_PATH -projectPath $PROJECT_PATH -executeMethod ProjectBuild.BuildForIPhone project-$1 -quit
 
echo "XCODE�����������"
 
#��ʼ����ipa#
$BUILD_IOS_PATH $PROJECT_PATH/$1 $1
 
echo "ipa�������"