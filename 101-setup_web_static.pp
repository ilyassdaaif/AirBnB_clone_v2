# Puppet manifest to set up web static content for Holberton School project
node '89-web-01' {

  # Ensure the /data directory exists
  file { '/data':
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  # Ensure subdirectories /releases and /shared exist under /data/web_static
  file { '/data/web_static':
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { '/data/web_static/releases':
    ensure => 'directory',
    owner  => 'root',
    group  => 'root',
  }

  file { '/data/web_static/shared':
    ensure => 'directory',
    owner  => 'root',
    group  => 'root',
  }

  # Create a test release directory and an index.html within it
  file { '/data/web_static/releases/test':
    ensure => 'directory',
    owner  => 'root',
    group  => 'root',
  }

  file { '/data/web_static/releases/test/index.html':
    ensure  => 'file',
    content => '<html><head></head><body>Holberton School</body></html>',
    owner   => 'root',
    group   => 'root',
  }

  # Create a symbolic link to the test release
  file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test',
    owner  => 'root',
    group  => 'root',
  }

  # Install and configure Nginx if not already present
  package { 'nginx':
    ensure => installed,
  }

  # Configure Nginx to serve the static files
  file { '/etc/nginx/sites-available/default':
    content => template('path/to/your/nginx_default.erb'),
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }

}

# You need to provide the 'nginx_default.erb' template file for Nginx configuration
# Ensure it is configured to serve the '/data/web_static/current' directory under an alias like '/hbnb_static'
