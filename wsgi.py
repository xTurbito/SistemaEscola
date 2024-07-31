import sys
import os

# Asegúrate de que sys.path apunte a la raíz del proyecto
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Importa la aplicación desde app
from app import create_app

# Crea la aplicación
application = create_app()
