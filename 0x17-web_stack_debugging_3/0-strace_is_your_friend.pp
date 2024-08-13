# This Puppet manifest automates the fix for Apache 500 Internal Server Error

# Ensure the required directories and files have the correct permissions
exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
