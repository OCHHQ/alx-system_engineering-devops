# This manifest installs the Flask package version 2.1.0 using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# This manifest installs the Werkzeug package version 2.0.3 using pip3
package { 'Werkzeug':
  ensure   => '2.0.3',
  provider => 'pip3',
}
