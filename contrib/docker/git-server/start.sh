#!/bin/sh

# create an empty repository
rm -rf /srv/repo.git
git init --bare --shared /srv/repo.git
chown -R git /srv/repo.git

# for each daemon, we take care to ensure that all logging happens to
# stdout & stderr

# start the fcgi daemon
/usr/bin/spawn-fcgi \
    -u git -U git -n \
    -d /srv \
    -s /run/git.socket \
    /usr/bin/fcgiwrap &

# start the simple daemon
HOME=/home/git git daemon \
    --export-all \
    --user=git \
    --base-path=/srv \
    /srv &

# start nginx
/usr/sbin/nginx \
    -c /git-server/nginx.conf &

# finally, start ssh
# -D flag avoids executing sshd as a daemon
exec /usr/sbin/sshd -D
