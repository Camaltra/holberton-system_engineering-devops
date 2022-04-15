#Install the puppet-link package

exec {'Install puppet-lint':
    command => 'sudo gem install puppet-lint -v 2.5.0'
    path    => ['/usr/bin'],
}