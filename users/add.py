from communication.remote import open

def userByName(host, userName, comments, publicKey):

    #New User's home directory
    userHome = "/home/" + userName
    userSSHDir = userHome + "/.ssh"
    userAuthorizedKeys = userSSHDir + "/authorized_keys"

    # Prepare create user and home directory commands
    createUser = "sudo useradd -m -d " + userHome + " -s /bin/bash -c " + comments + " " + userName 

    #Create user's .ssh and .ssh/authorized_keys directories and authorized_keys file
    createUserDirectories = "sudo mkdir % s && sudo touch % s" % (userSSHDir, userAuthorizedKeys)

    # Write public ssh key out to file
    createUsersSSHPublicKeyFile = "sudo bash -c 'echo \"% s\" >> % s'" % (publicKey, userAuthorizedKeys)

    # Update Permissions for user directories
    # chown -R username:username userHome
    # chmod 700 userHome
    # chmod 600 userAuthorizedKeys
    updateUserSSHDirectoryPermissions = "sudo chown -R % s:% s % s && sudo chmod 700 % s && sudo chmod 600 % s" % (userName, userName, userSSHDir, userSSHDir, userAuthorizedKeys)

    # fullCreateUserCommand = createUser + " && " + createUserDirectories + " && " + createUsersSSHPublicKeyFile + " && " + updateUserSSHDirectoryPermissions
    fullCreateUserCommand = "% s && % s && % s && % s" % (createUser, createUserDirectories, createUsersSSHPublicKeyFile, updateUserSSHDirectoryPermissions)

    # Specify connection type (ssh), pem key location, remote, command to be passed 
    connectionContext = ["ssh", host, fullCreateUserCommand]

    open(connectionContext)