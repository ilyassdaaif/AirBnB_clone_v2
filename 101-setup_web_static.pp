file { '/data':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

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

file { '/data/web_static/releases/test':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => '<html>
                <head>
                </head>
                <body>
                  Holberton School
                </body>
              </html>',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

file { '/data/web_static/shared':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  owner  => 'root',
  group  => 'root',
}

# Configure Nginx to serve the content
exec { 'nginx_config':
  command => "/usr/sbin/nginx -s reload",
  refreshonly => true,
  subscribe => File['/data/web_static/releases/test/index.html'],
}

# Ensure nginx is installed and running
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => File['/data/web_static/releases/test/index.html'],
}

