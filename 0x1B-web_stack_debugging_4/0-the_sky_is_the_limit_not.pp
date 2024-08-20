# This Puppet manifest optimizes Nginx to handle more requests under load

exec { 'optimize_nginx':
  command => '/usr/sbin/nginx -s reload',
  path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
  require => File['/etc/nginx/nginx.conf'],
}

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
  notify  => Exec['optimize_nginx'],
}

package { 'nginx':
  ensure => installed,
}

