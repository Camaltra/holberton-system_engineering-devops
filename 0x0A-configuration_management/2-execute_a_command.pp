#Kill a process

exec { 'pkill -f killmenow':
    provider => 'shell'
}
