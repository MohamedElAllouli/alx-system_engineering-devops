# Installs a package

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install flask==2.1.0',
  path        => ['/usr/bin'],
  environment => ['PATH=/usr/bin'],
  unless      => '/usr/bin/flask --version | grep "2.1.0"',
}
