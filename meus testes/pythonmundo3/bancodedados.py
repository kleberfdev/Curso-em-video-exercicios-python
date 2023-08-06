import pyodbc

# Configuração da conexão com o banco de dados SQL Server
server = '34.170.123.43'
database = 'BDADOS'
username = 'kleber'
password = 'Sacigk8877#@'
driver = '{ODBC Driver 18 for SQL Server}' # O driver ODBC necessário para SQL Server

# Criação da string de conexão
conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Network Library=DBMSSOCN"


try:
    # Tentando estabelecer a conexão com o banco de dados
    conn = pyodbc.connect(conn_str)

    # Se não houver exceção, a conexão foi estabelecida com sucesso
    print("Conexão estabelecida com sucesso!")

    # Fechando a conexão
    conn.close()

except pyodbc.Error as e:
    # Se ocorrer algum erro na conexão, será capturado aqui
    if 'Login failed for user' in str(e):
        print("Erro de logon: Usuário ou senha incorretos.")
    elif 'Database bddados not found' in str(e):
        print("Erro de banco de dados: Banco de dados 'bddados' não encontrado.")
    else:
        print("Erro desconhecido:", e)
