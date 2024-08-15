# 0-strace_is_your_friend.pp
file { '/etc/wordpress/config-127.0.0.1.php':
  ensure  => file,
  content => template('wordpress/config.erb'),
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}
