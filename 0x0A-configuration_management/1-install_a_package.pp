#Install the puppet-link package

package { 'puppet-lint':
    ensure   => '2.5.0',
    provider => 'gem'
}
