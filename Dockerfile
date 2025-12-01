FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

# ---------------------------
# INSTALAR PAQUETES NECESARIOS
# ---------------------------
RUN apt-get update && apt-get install -y \
    openssh-server openssl \
    apache2 \
    python3 python3-pip python3-venv \
    postgresql postgresql-contrib \
    supervisor \
    && mkdir /var/run/sshd

# ---------------------------
# CREACIÓN DE FLAGS
# ---------------------------
RUN mkdir -p /home/www-data && \
    echo "ssi{$(openssl rand -hex 8)}" > /home/www-data/user.txt && \
    chown www-data:www-data /home/www-data/user.txt && \
    chmod 600 /home/www-data/user.txt && \
    echo "ssi{$(openssl rand -hex 8)}" > /root/root.txt && \
    chmod 600 /root/root.txt && \
    rm -rf /home/ubuntu

# ---------------------------
# POSTGRESQL
# ---------------------------
RUN service postgresql start && \
    su - postgres -c "psql -c \"CREATE USER admin WITH PASSWORD 'admin';\"" && \
    su - postgres -c "psql -c \"CREATE DATABASE mydb OWNER admin;\""

# ---------------------------
# APACHE2 FRONTEND
# ---------------------------
RUN echo "<h1>Frontend en Apache2 funcionando</h1>" > /var/www/html/index.html

# ---------------------------
# DJANGO BACKEND
# ---------------------------
RUN mkdir -p /opt/backend

VOLUME ["/opt/backend"]

# ---------------------------
# CONFIGURAR SSH
# ---------------------------
RUN echo "root:root" | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# ---------------------------
# CONFIGURAR SUPERVISOR
# ---------------------------
RUN mkdir -p /etc/supervisor/conf.d

RUN cat > /etc/supervisor/conf.d/services.conf <<EOF
[supervisord]
nodaemon=true

[program:ssh]
command=/usr/sbin/sshd -D

[program:postgres]
command=/usr/lib/postgresql/14/bin/postgres -D /var/lib/postgresql/14/main
user=postgres
autorestart=true

[program:apache2]
command=/usr/sbin/apachectl -D FOREGROUND
autorestart=true

[program:django]
directory=/opt/backend
command=bash -c "source venv/bin/activate && python manage.py runserver 0.0.0.0:8000"
autorestart=true
EOF

# ---------------------------
# PUERTOS EXPUESTOS
# ---------------------------
EXPOSE 22 80

# ---------------------------
# ENTRYPOINT
# ---------------------------
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/services.conf"]
