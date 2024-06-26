#!/usr/bin/python3
"""
Fabric script  that distributes an archive to your web servers
"""

from fabric.api import put, run, env, local
from os.path import exists
from datetime import datetime
env.hosts = ['54.157.184.104', '54.157.186.151']


def do_pack():
    """
    return the archive path if archive has generated
    """
    local("mkdir -p version")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(date)
    tgz_archive = local("tar -cvzf {} web_static".format(path))

    if tgz_archive.succeeded:
        return path
    else:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.
    """
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file,
                                             newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("Deployment succesful")
        return True

    return False
