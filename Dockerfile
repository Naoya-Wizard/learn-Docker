# ベースイメージとしてMicrosoftのSQL Serverを使用
FROM mcr.microsoft.com/mssql/server:2022-latest

# rootユーザーで実行
USER root

# 必要なパッケージをインストール（Pythonと依存関係）
RUN apt-get update && \
    apt-get install -y curl gnupg2 python3 python3-pip && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17 mssql-tools && \
    apt-get clean && \
    echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc && \
    pip3 install pyodbc && \
    . ~/.bashrc

# ホストマシンのPythonスクリプトをコンテナ内にコピー
COPY create_database.py /app/create_database.py

# コンテナ起動時にSQL Serverを開始し、Pythonスクリプトを実行
CMD /bin/bash -c "/opt/mssql/bin/sqlservr & sleep 30 && python3 /app/create_database.py && wait"

