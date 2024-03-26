# add stable version of nginx
exec {'nginx stable repo':
    command => 'sudo add-apt-repository ppa:nginx/stable',
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    }

# update packages
exec {'apt update':
    command => 'sudo apt-get update',
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    }

# install nginx and ufw firewall
package {'nginx': ensure    => 'installed'}
package {'ufw': ensure      => 'installed'}

# Allow nginx: full access
exec {'grant ufw access to http':
    command => 'sudo ufw allow "Nginx Full"',
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    }

# create index file
file {'/var/www/html/index.html':
    ensure  => 'present',
    content => 'Hello world!\n',
    }

# create custom 404 error page file
file {'/var/www/html/custom_404.html':
    ensure  => 'present',
    content => "Ceci n'est pas une page\n",
    }

# configure serve and save in default file in sites-enabled
file {'/etc/nginx/sites-enabled/default':
    ensure  => 'present',
    content => "server {
                    listen 80 default_server;
                    listen [::]:80 default_server;
                    root /var/www/html;
                    index index.html;
                    server_name _;
                    location / {
                        try_files \$uri \$uri/ =404;
                    }
                    error_page 404 /custom_404.html;
                    location /custom_404.html {
                        internal;
                    }
                    location ~ /redirect_me {
                        return 301 /www.google.com;
                    }
                }",
        }

# restart nginx
exec {'Restart nginx':
    command => 'service nginx restart',
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    }
