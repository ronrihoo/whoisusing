#! /bin/sh

echo 'Setting up whoisusing...'

mkdir /usr/local/bin/whoisusing-1.0
cp ./* /usr/local/bin/whoisusing-1.0/
cp /usr/local/bin/whoisusing-1.0/whoisusing.py /usr/local/bin/whoisusing-1.0/whoisusing
chmod +x /usr/local/bin/whoisusing-1.0/remove.sh /usr/local/bin/whoisusing-1.0/whoisusing
ln -s /usr/local/bin/whoisusing-1.0/whoisusing /usr/local/bin/whoisusing

echo 'Setup is complete.'
echo 'You may now delete this directory and all of its contents.'