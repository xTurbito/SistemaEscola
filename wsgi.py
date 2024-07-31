import sys
import os

# Agrega el directorio del proyecto al sys.path
sys.path.insert(0, '/home/malcocer/mysite')

# Importa la aplicación desde app
from app import create_app

# Crea la aplicación
application = create_app()
