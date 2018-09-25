name=$(netstat -tulpn |grep -Po '[0-9a-z.*]+([0-9]+)(?=\/python)'|tr '\n' ' ')
kill ${name}
