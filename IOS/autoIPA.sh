#!/bin/sh


#UNITY程序的路径#
UNITY_PATH="/Applications/Unity/Unity.app/Contents/MacOS/Unity"
 
#游戏程序路径#
PROJECT_PATH="../.."

#ipa存放路径
OUT_PATH=/Users/YH/Desktop/ipa
 
#IOS打包脚本路径#
BUILD_IOS_PATH=${PROJECT_PATH}/tools/IOS/buildipa.sh
 
#生成的Xcode工程路径#
XCODE_PATH=${PROJECT_PATH}/IOS/$1

curdir=$PWD 
#将unity导出成xcode工�

echo "xcode project build start"
cd $PROJECT_PATH
$UNITY_PATH  -batchmode -quit -projectPath "" -executeMethod ProjectBuildIOS.BuildForIPhone project-IOS/$1

cd $curdir
echo "XCODE工程生成完毕"

curdir=$PWD 
#开始生成ipa#

sh $BUILD_IOS_PATH $XCODE_PATH $1
  
echo "ipa生成完毕"
#cd $curdir
ipaName=$1v$2t$(date +%Y%m%d%H%M%S).ipa
mv ${XCODE_PATH}/build/$1.ipa ${XCODE_PATH}/build/$ipaName
python upload.py ${XCODE_PATH}/build/$ipaName $ipaName.ipa
#mv ${XCODE_PATH}/build/$1.ipa ${OUT_PATH}/$1$(date +%Y%m%d%H%M).ipa

