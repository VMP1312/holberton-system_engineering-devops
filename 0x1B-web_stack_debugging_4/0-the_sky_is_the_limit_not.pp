#Fixed

exec{ 'fix_nginx':
      command  => 'sed -i "s/-n 15/-n 4100/g" /etc/default/nginx',
      provider => 'shell'
}
exec{'restart_nginx':
  command  => 'sudo service nginx restart',
  provider => 'shell',
  require  => Exec['fix_nginx']
}
