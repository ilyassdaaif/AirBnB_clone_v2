#!/usr/bin/python3
"""distributes an archive to your web servers, using the function do_deploy:"""
from fabric.api import env, run, put, local
from os.path import exists

env.hosts = ['54.152.5.96-web-01', '100.25.4.103-web-02']  # Replace with actual IPs
env.user = "ubuntu"  # Set as needed, or define in command line
env.key_filename = "my_ssh_private_key"  # Set path to your SSH key, or define in command line

def do_deploy(archive_path):
    # Check if the archive_path exists locally
    if not exists(archive_path):
        return False

    # Extract the file name from the archive_path
    file_name = archive_path.split("/")[-1]
    # Remove the extension to get the base directory name
    base_dir = file_name.split(".")[0]

    # Upload the archive to the /tmp/ directory on the server
    remote_path = f"/tmp/{file_name}"
    put(archive_path, remote_path)

    # Create the directory where we will uncompress the archive
    release_dir = f"/data/web_static/releases/{base_dir}/"
    run(f"mkdir -p {release_dir}")

    # Uncompress the archive to the folder on the web server and then delete the archive
    run(f"tar -xzf {remote_path} -C {release_dir}")
    run(f"rm {remote_path}")

    # Move contents out of the web_static folder to the base directory and remove web_static directory
    run(f"mv {release_dir}web_static/* {release_dir}")
    run(f"rm -rf {release_dir}web_static")

    # Delete the current symbolic link and create a new one
    run("rm -rf /data/web_static/current")
    run(f"ln -s {release_dir} /data/web_static/current")

    print("New version deployed!")
    return True
