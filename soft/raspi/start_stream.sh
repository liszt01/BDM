## This example shows how to invoke mjpg-streamer from the command line
 
#インストール先のパスを設定
export LD_LIBRARY_PATH="$HOME/mjpg-streamer/mjpg-streamer-experimental"
STREAMER="$LD_LIBRARY_PATH/mjpg_streamer"
 
# 表示する画像サイズとフレームレートを設定
SIZE="1280x720"
FPS="30"
 
# Webサーバーの設定
WWWDOC="$LD_LIBRARY_PATH/www"
PORT="8080"
 
#ベーシック認証の設定
# ID="AAA" #ベーシック認証用のID
# PW="BBB" #ベーシック認証用のパスワード
 
# 起動用のコマンド
#for USB Camera
$STREAMER -i "input_uvc.so -y -n -f $FPS -r $SIZE -d /dev/video0" \
          -o "output_http.so -w $WWWDOC -p $PORT"
 
#for Raspberry Pi Camera Module
#$STREAMER -i "input_raspicam.so -x $XRES -y $YRES -fps $FPS" \
#          -o "output_http.so -w $WWWDOC -p $PORT -c $ID:$PW"