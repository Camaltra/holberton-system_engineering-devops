#Install the puppet-link package

package { 'puppet-link':
    ensure   => 2.5.0,
    provider => gem
}
