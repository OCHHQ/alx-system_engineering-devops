# Ensure the Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the Nginx service is running and enabled to start on boot
service { 'nginx':
  ensure     => running,
  enable     => true,
  require    => Package['nginx'],
}

# Create the index.html file with "Hello World!" content
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Create the custom 404 page with the required content
file { '/var/www/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
  require => Package['nginx'],
}

# Manage the Nginx default site configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Create the template directory if it doesn't exist
file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates':
  ensure => directory,
}

# Template for the Nginx default site configuration
file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates/default.erb':
  ensure  => file,
  content => @(END),
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files $uri $uri/ =404;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/@camprollcollins.tech;
    }

    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
}
| END
}
