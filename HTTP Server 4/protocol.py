def chck_HTTP_request(data):

    request = data.split(" ")

    if request[0] == "GET":
        if request[1] != "":
            if request[2][0:10] == "HTTP/1.1\r\n":
                return True
    else:
        return False
