# pytorch が動く Dockerfile を作成

* [0. Alpine Linux](#alpine-linnux-の利用)
* [1. Dockerfile作成](#1-dockerfile-の作成)
* [2. Docker実行](#2-docker-実行)


## Alpine Linux の利用
> [Alpine Linux](https://alpinelinux.org/) は、muslと [BusyBox](http://monoist.atmarkit.co.jp/mn/articles/0802/04/news114.html) をベースとしたLinuxディストリビューションである。セキュリティ・シンプルさ・リソース効率を重視するパワーユーザー向けに設計されている (wikipedia)

* CentOS: 4GB
* Ubuntu: 700MB
* Alpine: 100MB

### apk
パッケージ管理ツール
* CentOS: apt-get
* Ubuntu: yum
* Alpine: apk

## 1. Dockerfile の作成
[pytorch-alpine](https://github.com/petronetto/pytorch-alpine/blob/master/Dockerfile) を参考にする

```Dockerfile

```

### Dockerfile command
- [FROM](#fromベースイメージの指定)
- [MAINTAINER](#maintainer作成者情報)
- [LABEL](#labelメタデータ追加)
- [RUN](#runコマンド実行)
- [CMD](#cmdコンテナ実行時の実行コマンド)
- [ENTRYPOINT](#entrypointコンテナ実行時の実行コマンド)
- [EXPOSE](#exposeポート解放)
- [VOLUME](#volumeマウント)
- [ADD](#addファイル・ディレクトリ追加)
- [COPY](#copyファイル・ディレクトリコピー)
- [USER](#userユーザ指定)
- [WORKDIR](#workdir作業ディレクトリ指定)
- [ENV](#env環境変数設定)

### FROM（ベースイメージの指定）
* `$ docker search` でイメージを検索可能
* [alpine-python](https://github.com/jfloff/alpine-python)から python をいれる（基準となる python の image が用意されている）

```Dockerfile
# FROM <image>:<tag>
FROM jfloff/alpine-python:3.7-slim
```

### MAINTAINER（作成者情報）
```Dockerfile
# MAINTAINER <名前>
```

### LABEL（メタデータ追加）
* image にメタデータを追加
* `$ docker inspect`でイメージに設定されているLABELを参照可能

```Dockerfile
# LABEL <key>=<value>
LABEL maintainer="Juliano Petronetto <juliano@petronetto.com.br>" \
      name="PyTorch Alpine" \
      description="PyTorch in Alpine Linux" \
      url="https://hub.docker.com/r/petronetto/pytorch-alpine" \
      vcs-url="https://github.com/petronetto/pytorch-alpine" \
      vendor="Petronetto DevTech" \
      version="1.0"
```

### RUN（コマンド実行）
```Dockerfile
# RUN <コマンド>
# RUN ["実行バイナリ", "パラメータ１", "パラメータ２"]
```

### CMD（コンテナ実行時の実行コマンド）
* Dockerfileで一度だけ指定可能
* docker run時に実行されるコマンドを指定
```Dockerfile
# CMD <コマンド>
# CMD ["実行バイナリ", "パラメータ１", "パラメータ２"]
```

### ENTRYPOINT（コンテナ実行時の実行コマンド）
* Dockerfileで一度だけ指定可能
* docker run時に実行されるコマンドを指定
* docker run時にコマンドを指定しても、ENTRYPOINTのコマンドがそのまま実行
* `["command", "paramN"]`形式 による引数付きコマンドで記述した場合、docker run時にparam部分だけ上書きする
```Dockerfile
# ENTRYPOINT ["実行可能なもの", "パラメータ１", "パラメータ２"]
# ENTRYPOINT コマンド パラメータ１ パラメータ２
```

### EXPOSE（ポート解放）
```Dockerfile
# EXPOSE <port> [<port>...]
```

### VOLUME（マウント）
* マウントポイントを作成
* dockerコンテナで作成したデータをホストのファイルシステムをマウントしてデータを置く
```Dockerfile
# VOLUME ["/data"]
```

### ADD（ファイル・ディレクトリ追加）
```Dockerfile
# ADD <ソース>... <送信先>
# ADD ["<ソース>", ... "<送信先>"] 
```

### COPY（ファイル・ディレクトリコピー）
```Dockerfile
# COPY <ソース>... <送信先>
# COPY ["<ソース>",... "<送信先>"]
```

### USER（ユーザ指定）
```Dockerfile
# USER <user name>
```

### WORKDIR（作業ディレクトリ指定）
```Dockerfile
# WORKDIR <ディレクトリパス>
```

### ENV（環境変数設定）
```Dockerfile
# ENV <key>=<value> ...
```

## 2. docker 実行
```bash
$ touch Dockerfile
$ docker build ./ -t hoge -f Dockerfile
$ docker run -it hoge    # -it で intaractive shell 
```

### docker build
Dockerイメージのビルドとは、ベースとなるイメージに対して、何らかの機能を加えて、ユーザイメージ（自分独自のイメージ）を作り出すことを指します。Dockerfile ではベースイメージい対して実行する操作を記述．
<img src="https://www.ogis-ri.co.jp/otc/hiroba/technical/docker/img/part2/build.png">


### docker run
コンテナを作成し，そのコンテナを起動まで行う
* `-it`: (interactive)コンテナ内で対話的に作業する
* `-name`: コンテナ名の指定
* `-e　HOGE=hoge`: 環境変数 HOGE に hoge という値を格納
* `-p 8888:5000`: ポートの開放．Dockerfile で 5000 を指定し，コンテナ上では 8888 を開放する

# my log
```bash
# alpine-python を clone
$ git clone https://github.com/jfloff/alpine-python.git
$ cd alpine-python
$ cp 3.7-slim/Dockerfile 3.7-slim/myDokerfile

# まずは試しに
$ docker build 3.7-slim -t sample -f 3.7-slim/myDokerfile
$ docker run -it sample

# 拡張
$ vim 3.7-slim/myDockerfile

<<PLAN
1. pyenv install

ENV HOME=hoge
ENV CMD_UTIL=~/.bashrc

RUN git clone https://github.com/pyenv/pyenv.git $HOME/.pyenv \
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> $CMD_UTIL \
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> $CMD_UTIL \
    echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> $CMD_UTIL \
    exec "$SHELL"


2. pytorch install
2.1. git install

2.2. pytorch-alpine


PLAN

# diff
$ diff 3.7-slim/Dockerfile 3.7-slim/myDokerfile
```


# 参考
* [Docker cheetsheet](https://www.docker.com/sites/default/files/d8/2019-09/docker-cheat-sheet.pdf)
* [Docker builder](http://docs.docker.jp/engine/reference/builder.html)
* [Docker commands](https://docs.docker.com/engine/reference/commandline/docker/)
* [Alpine Linux](https://alpinelinux.org/)
* [Alpine Linux GitHub](https://github.com/alpinelinux)
* [pytorch-alpine](https://github.com/petronetto/pytorch-alpine)


* [pyenv install](https://github.com/pyenv/pyenv#basic-github-checkout)
