import pyodbc
import sqlalchemy as sa
from sqlalchemy import text  # 追加

# 接続情報の設定
server = 'localhost,1433'  # DockerコンテナのSQL Serverはローカルで動いている
database = 'master'
username = 'sa'
password = 'YourStrongPassword!'
driver = 'ODBC Driver 17 for SQL Server'

# 接続を作成
connection_string = f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
engine = sa.create_engine(f"mssql+pyodbc:///?odbc_connect={connection_string}")

# テーブル作成
with engine.connect() as conn:
    conn.execute(text("""
    CREATE TABLE TestTable (
        id INT PRIMARY KEY,
        name NVARCHAR(50)
    );
    """))  # text()関数を使用してSQL文を渡す

# データを挿入
with engine.connect() as conn:
    conn.execute(text("""
    INSERT INTO TestTable (id, name) VALUES (1, 'TestName');
    """))  # こちらも同様にtext()を使用

print("データベース操作が完了しました。")
