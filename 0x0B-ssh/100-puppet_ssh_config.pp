#Create the good ssh config thank to puppet
#(Need the same result as the last task)

exec {sed -i "s/#   PasswordAuthentication yes/    PasswordAuthentication no/" /etc/ssh/ssh_config:
    path => '/usr/bin',
}

exec {sed -i "s/#   IdentityFile\s~\/.ssh\/id_rsa/    IdentityFile ~\/.ssh\/school/" /etc/ssh/ssh_config:
    path => '/usr/bin',
}