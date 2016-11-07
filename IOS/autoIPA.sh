#!/bin/sh
 
#参数判断  
if [ $# != 1 ];then  
    echo "需要一个参数。 参数是游戏包的名子"  
    exit     
fi  
 
#UNITY程序的路径#
UNITY_PATH=/Applications/Unity/Unity.app/Contents/MacOS/Unity
 
#游戏程序路径#
PROJECT_PATH=/Users/YH/Desktop/AutoMate/youhao_game/client/Develop/KnightOfLight

#ipa存放路径
OUT_PATH=/Users/YH/Desktop/ipa
 
#IOS打包脚本路径#
BUILD_IOS_PATH=${PROJECT_PATH}/tools/IOS/buildipa.sh
 
#生成的Xcode工程路径#
XCODE_PATH=${PROJECT_PATH}/$1
 
#将unity导出成xcode工程#
$UNITY_PATH -projectPath $PROJECT_PATH -executeMethod ProjectBuildIOS.BuildForIPhone project-$1 -quit
 
echo "XCODE工程生成完毕"
 
#开始生成ipa#
cd $XCODE_PATH
sh $BUILD_IOS_PATH $XCODE_PATH $1
  
echo "ipa生成完毕"

python upload.py ${XCODE_PATH}/build/$1.ipa $1v$2t$(date +%Y%m%d%H%M%S).ipa
mv ${XCODE_PATH}/build/$1.ipa ${OUT_PATH}/$1$(date +%Y%m%d%H%M).ipa

