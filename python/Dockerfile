# ベースとなる Docker イメージを指定
FROM python:3.7.5-alpine

# プロジェクトフォルダを指定
ARG project_dir=/helloworld/

# requirements.txt をコンテナにコピー
ADD requirements.txt $project_dir

# requirements.txt に書かれたパッケージをインストール
WORKDIR $project_dir
RUN apt-get update
RUN apt-get install python3.7
RUN apt-get install python3-pip
RUN pip3 install -r requirements.txt
RUN pip3 install requests
RUN pip3 install openpyxl
RUN pip3 install mysqlclient
RUN pip3 install python-dotenv