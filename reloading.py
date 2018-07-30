#!/usr/bin/env python
from livereload import Server, shell
server = Server()
server.watch('source/', shell('make html'))
server.serve(root='build/html', host="0.0.0.0", debug=True)