#!/usr/bin/python3
"""distributes an archive to your web servers, using the function do_deploy:"""
from fabric.api import env, run, put, local, sudo
from os.path import isfile

# Define the servers to deploy to
env.hosts = ['54.152.5.96', '100.25.4.103']  # Replace with the actual IPs or hostnames
env.user = 'ubuntu'  # Replace with your SSH user
env.key = '/path/to/my_ssh_private_key'  # Replace with your actual SSH private key path

def do_deploy(archive_path):
    # Check if the archive exists locally
    if not isfile(archive_path):
        return False

    try:
        # Extract the file name and the base directory name from the archive path
        file_name = archive_path.split('/')[-1]
        base_dir = file_name.replace('.tgz', '').replace('.gz', '')

        # Upload the archive to the /tmp/ directory on the web server
        remote_tmp_path = f"/tmp/{file_name}"
        put(archive_path, remote_tmp_path)

        # Create the target directory where we will uncompress the archive
        release_dir = f"/data/web_static/releases/{base_dir}/"
        run(f"mkdir -p {release_dir}")

        # Uncompress the archive to the folder on the web server and then delete the archive
        run(f"tar -xzf {remote_tmp_path} -C {release_dir}")
        run(f"rm {remote_tmp_path}")

        # Move contents out of the web_static folder to the base directory
        run(f"mv {release_dir}web_static/* {release_dir}")
        run(f"rm -rf {release_dir}web_static")

        # Delete the current symbolic link and create a new one
        sudo("rm -rf /data/web_static/current")
        sudo(f"ln -s {release_dir} /data/web_static/current")

        print("New version deployed!")
        return True
    except:
        return False
