import subprocess

#  
ERROR_PRE_MESSAGE = "Error: \n"

def open(connectionContext):

    connection = subprocess.Popen(connectionContext, shell=False, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # 
    try:
        response, err = connection.communicate(timeout=10)
        if err:
            print(ERROR_PRE_MESSAGE, err)
        else:
            print(response)
    except:
        connection.kill()
        response, err = connection.communicate()
        print(ERROR_PRE_MESSAGE, err)