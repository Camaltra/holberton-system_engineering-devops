#Create Nginx configuratio server via puppet

package { 'nginx':
  ensure   => present,
  provider => 'apt'
}

file {'Adding the first content':
  ensure  => present,
  path    => '/var/www/html/index.html',
  content => 'Hello World!\n',
}

file_line { 'redirect_me page':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => '        rewrite ^/redirect_me https://www.youtube.com/watch?v=dQw4w9WgXcQ permanent;',
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => Package['nginx'],
  subscribe  => File_line['redirect_me page'],
}
