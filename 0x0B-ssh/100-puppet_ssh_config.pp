#Create the good ssh config thank to puppet
#(Need the same result as the last task)

file_line {'Add PasswordAuthentication no':
    path => '/etc/ssh/ssh_config',
    line => '    PasswordAuthentication no'
}

file_line {'Add IdentityFile with the right key':
    path => '/etc/ssh/ssh_config',
    line => '    IdentityFile ~/.ssh/school'
}