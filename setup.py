from cx_Freeze import setup, Executable

setup(
    name="Automacao_Atados",
    version="1.0",
    description="Descrição do executável",
    executables=[Executable("index.py")],
)