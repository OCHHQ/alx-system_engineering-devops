#!/usr/bin/env bash
# 2-puppet_custom_http_response_header.pp

# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Configure custom HTTP header in Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $hostname;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    
    error_page 404 /404.html;
    location = /404.html {
        internal;
        root /var/www/html;
        default_type text/html;
        return 404 'Ceci n\'est pas une page';
    }
    
    location / {
        try_files $uri $uri/ =404;
    }
}
",
  require => Package['nginx'],
}

# Restart Nginx service to apply changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
