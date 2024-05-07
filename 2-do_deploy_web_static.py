#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers,
extracts it, and sets up a new web static folder structure.
"""

from fabric.api import *
from os.path import exists

env.user = 'ubuntu'
env.hosts = ['54.152.5.96', '100.25.4.103']  # Replace with actual IPs
env.key_filename = 'path_to_my_ssh_private_key'  # Path to SSH private key

def do_deploy(archive_path):
    """
    Deploys the archive to web servers.
    :param archive_path: Path to the archive to be deployed
    :return: Boolean, True if all operations are done correctly, otherwise False
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Extract the archive filename without the extension
        file_name = archive_path.split("/")[-1]
        folder_name = file_name.split(".")[0]

        # Define the full remote path to the archive and release directory
        remote_path = "/data/web_static/releases/" + folder_name + '/'

        # Prepare release folder and unarchive the file there
        run("mkdir -p {}".format(remote_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, remote_path))

        # Remove the archive from the server after unarchiving
        run("rm /tmp/{}".format(file_name))

        # Move content from web_static subfolder to the parent folder
        run("mv {0}web_static/* {0}".format(remote_path))
        run("rm -rf {}web_static".format(remote_path))

        # Delete the current symbolic link and create a new one
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(remote_path))

        print("New version deployed!")
        return True
    except:
        return False
