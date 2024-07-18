#!/usr/bin/python3
"""
Fabric script that distributes an
archive file to web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['18.210.14.120', '54.90.8.146']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        # Extracting the file name and name
        arch_file = archive_path.split("/")[-1]
        archive_name = arch_file.split(".")[0]
        path = "/data/web_static/releases/"

        # Upload the archive to /tmp/ directory
        put(archive_path, '/tmp/')

        # Creating target directory
        run('mkdir -p {}{}/'.format(path, archive_name))

        # Uncompressing the archive to target directory
        run('tar -xzf /tmp/{} -C {}{}/'.format(arch_file, path, archive_name))

        # Deleting archive from the web server
        run('rm /tmp/{}'.format(arch_file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, archive_name))
        run('rm -rf {}{}/web_static'.format(path, archive_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, archive_name))
        return True
    except:
        return False
