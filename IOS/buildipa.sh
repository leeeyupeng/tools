# #!/bin/bash  
 
#参数判断  
if [ $# != 2 ];then  
    echo "Params error!"  
    echo "Need two params: 1.path of project 2.name of ipa file"  
    exit  
elif [ ! -d $1 ];then  
    echo "The first param is not a dictionary."  
    exit      
 
fi

code_sign_identity="iPhone Developer: luo kai "
app_profile_uuid="/Users/YH/Downloads/comYHKOL.mobileprovision"
#工程路径  
project_path=$1  
 
#IPA名称  
ipa_name=$2
 
#build文件夹路径  
build_path=${project_path}/build  
 
#清理#
#xcodebuild  clean
 
#编译工程  
cd $project_path
#xcodebuild -configuration Debug ENABLE_BITCODE=NO
#xcodebuild ENABLE_BITCODE=NO CODE_SIGN_IDENTITY="$code_sign_identity" APP_PROFILE="$app_profile_uuid"
#xcodebuild ENABLE_BITCODE=NO|| exit
#xcodebuild DEVELOPMENT_TEAM=863KK7F4EQ ENABLE_BITCODE=NO CODE_SIGN_IDENTITY="${code_sign_identity}" APP_PROFILE="${app_profile_uuid}"|| exit

#xcodebuild DEVELOPMENT_TEAM=863KK7F4EQ ENABLE_BITCODE=NO 
#xcodebuild DEVELOPMENT_TEAM=863KK7F4EQ ENABLE_BITCODE=NO archive -scheme "Unity-iPhone" -archivePath kol.xcarchive
#打包 下面代码我是新加的#
xcodebuild -exportArchive -archivePath kol.xcarchive -exportPath ${build_path}/${ipa_name}.ipa -exportFormat IPA  -exportProvisioningProfile "com.YH.KOL"
#xcrun -sdk iphoneos PackageApplication -v ${build_path}/${ipa_name}.app -o ${build_path}/${ipa_name}.ipa --sign "$code_sign_identity" --embed "$app_profile_uuid"