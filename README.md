# LOCUST - An open source load testing tool.

Uruchomienie SimpleHTTPServer

    $ python -m SimpleHTTPServer 8000
    
    # http://localhost:8000/
    
Generowanie plików testowych

    $ dd if=/dev/zero of=small.txt count=100 bs=100
    $ dd if=/dev/zero of=medium.txt count=10000 bs=100
    $ dd if=/dev/zero of=large.txt count=1000000 bs=100
    
Instalacja i uruchomienie Locust

    $ python -m pip install locustio
    $ locust --host=http://localhost:8000
    
    # http://localhost:8089/