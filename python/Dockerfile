# ベースとなる Docker イメージを指定
FROM python:3.7.5-alpine

# プロジェクトフォルダを指定
ARG project_dir=/helloworld/

# requirements.txt をコンテナにコピー
ADD requirements.txt $project_dir

# requirements.txt に書かれたパッケージをインストール
WORKDIR $project_dir
RUN pip3 install -r requirements.txt
RUN pip3 install mysqlclient