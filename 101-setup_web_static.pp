# Ensure the 'data' directory exists
file { '/data':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Ensure the 'web_static' directory exists under '/data'
file { '/data/web_static':
  ensure => directory,
  owner  => 'root',
  group  => 'root',
}

# Ensure 'releases' and 'shared' directories exist under '/data/web_static'
file { ['/data/web_static/releases', '/data/web_static/shared']:
  ensure => directory,
  owner  => 'root',
  group  => 'root',
}

# Ensure a test release directory exists and has an 'index.html' file
file { '/data/web_static/releases/test':
  ensure => directory,
  owner  => 'root',
  group  => 'root',
  require => File['/data/web_static/releases'],
} ->
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => '<html>
                <head>
                </head>
                <body>
                  Holberton School
                </body>
              </html>',
  owner   => 'root',
  group   => 'root',
}

# Create a symbolic link from 'current' to the test release
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  owner  => 'root',
  group  => 'root',
  require => File['/data/web_static/releases/test'],
}

# Configure nginx to serve the static files
class { 'nginx':
  manage_repo => true,
}

nginx::resource::vhost { 'hbnb_static':
  www_root => '/data/web_static/current',
  index_files => ['index.html'],
  server_name => ['localhost'],
  locations => {
    '/' => {
      location_cfg_append => {
        rewrite => '^/hbnb_static/(.*)$ /$1 break',
      },
    },
  },
}

