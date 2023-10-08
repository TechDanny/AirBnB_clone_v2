#!/usr/bin/python3
"""
generate a .tgz archive from the content of web static
"""


from datetime import datetime
from fabric.api import local


def do_pack():
    """
    creates a tgz file
    """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date)
    local("mkdir -p versions")
    arch_file = local("tar -cvzf {} web_static".format(file_name))
    if arch_file.return_code != 0:
        return None
    else:
        return file_name
