"""Waitress (Web Server Gateway Interface)
"""

from waitress import serve
import hello_world
serve(hello_world.app,host='0.0.0.0',port=8000)


