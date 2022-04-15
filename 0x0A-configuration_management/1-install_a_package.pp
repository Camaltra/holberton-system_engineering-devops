#Install the puppet-link package

exec { 'sudo gem intall puppet-lint -v 2.5.0':
    path    => ['/usr/bin'],
}
