#!/bin/bash

echo "as{$(openssl rand -hex 16)}" > /home/django/user.txt
chown django:www-data /home/django/user.txt
chmod 600 /home/django/user.txt

echo "as{$(openssl rand -hex 16)}" > /root/root.txt
chmod 600 /root/root.txt