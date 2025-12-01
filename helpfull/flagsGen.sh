#!/bin/bash

echo "ssi{$(openssl rand -hex 8)}" > /home/www-data/user.txt
chown www-data:www-data /home/www-data/user.txt
chmod 600 /home/www-data/user.txt

echo "ssi{$(openssl rand -hex 8)}" > /root/root.txt
chmod 600 /root/root.txt

gcc -fno-stack-protector -z execstack -o /home/www-data/rootAuth /home/www-data/rootAuth.c
chmod u+s /home/www-data/rootAuth