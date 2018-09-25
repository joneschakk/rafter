name=$(netstat -tulpn |grep -Po '[0-9a-z.*]+(?=\/python)'|tr '\n' ' ')
kill ${name}
