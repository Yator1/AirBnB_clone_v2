#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from the
contents of the web_static folder
"""

from datetime import datetime
from fabric.api import *
import os


def do_pack():
    """
    A function generating the .tgz archive file and
    its path.
    """
    if not os.path.exists("versions"):
        os.makedirs("versions")

    time = datetime.now()
    timestamp = time.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)
    archive_path = "versions/{}".format(archive_name)

    tgz_archive = local("tar -cvzf {} web_static".format(archive_path))

    if tgz_archive is not None:
        return archive_path
    else:
        return None
