# using puppet to make changes to the default ssh config file
# so that one can connect to a server without typing a password.
# Ensure SSH client configuration file exists
file { '/home/ubuntu/.ssh/config':
  ensure => present,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0644',
}

# Configure SSH client to use private key and disable password authentication
file_line { 'Turn off passwd auth':
  path   => '/home/ubuntu/.ssh/config',
  line   => 'PasswordAuthentication no',
  match  => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
  path   => '/home/ubuntu/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^#?IdentityFile',
}

