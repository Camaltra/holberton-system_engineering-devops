#Create the good ssh config thank to puppet
#(Need the same result as the last task)

exec {'ssh ubuntu@34.148.245.248; echo "    PasswordAuthentication no\n    IdentityFile ~/.ssh/school" > /etc/ssh/ssh_config':}