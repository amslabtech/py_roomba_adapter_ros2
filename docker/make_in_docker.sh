echo '====================================================='
echo 'move to /root/centernet/src/lib/models/networks/DCNv2'
echo '====================================================='
cd /root/CenterNet/src/lib/models/networks/DCNv2
./make.sh

echo '========================================'
echo 'move to /root/centernet/src/lib/external'
echo '========================================'
cd /root/CenterNet/src/lib/external
make
