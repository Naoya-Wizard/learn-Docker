import pyodbc

# SQL Serverに接続 (autocommit=True を追加)
connection = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost,1433;"
    "UID=sa;"
    "PWD=YourStrongPassword!",
    autocommit=True  # これを追加してトランザクションを使用しない
)

cursor = connection.cursor()

# データベース作成
cursor.execute("CREATE DATABASE TestDB")

print("データベース 'TestDB' が作成されました。")

cursor.close()
connection.close()
