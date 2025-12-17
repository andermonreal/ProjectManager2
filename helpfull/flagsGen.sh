#!/bin/bash

echo "ssi{$(openssl rand -hex 8)}" > /home/django/user.txt
chown django:www-data /home/django/user.txt
chmod 600 /home/django/user.txt

echo "ssi{$(openssl rand -hex 8)}" > /root/root.txt
chmod 600 /root/root.txt