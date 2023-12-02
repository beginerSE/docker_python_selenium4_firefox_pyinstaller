# Python-Selenium on Docker

## 事前準備

・Dockerのダウンロード

https://www.docker.com/products/docker-desktop/

・Realvncのダウンロード

https://www.realvnc.com/en/connect/download/viewer/


## 使用方法

`build.sh`を実行すれば必要なDockerコマンドが実行される。

→ 中身でやっていることは以下のような感じ、必要に応じてチューニングしてください


cdコマンドで「docker-compose.yml」がある直下のディレクトリにアクセス

```
docker-compose build --no-cache
docker-compose up -d
docker-compose exec app bash
```


`vnc://localhost:5901`にてブラウザの表示を見ながらデバッグが可能。

WindowsユーザならRealVNCで動作確認済み。


## 変更点

コンテナ内でダウンロードしたファイルは「tempDownload」に保存されます

保存先を変更したい場合は「docker-compose.yml」を編集してください

