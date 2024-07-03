# This manifest kills a process named killmenow using the pkill command
exec { 'kill_killmenow':
  command => '/usr/bin/pkill killmenow',
  path    => ['/bin', '/usr/bin'],
}
