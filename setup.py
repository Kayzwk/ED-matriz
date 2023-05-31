import sys
from cx_Freeze import setup, Executable

# Configurações do executável
executables = [
    Executable("index.py", base=None)  # Substitua "index.py" pelo nome do seu arquivo principal
]

# Configurações do setup
setup(
    name="MeuPrograma",
    version="1.0",
    description="Descrição do meu programa",
    executables=executables
)
