# pyrest_sample

* はじめに
本プロジェクトはRESTを用いたクライアントサーバ通信のPythonでの実装サンプルです。
ORMフレームワークのpeeweeを用いて、sqliteデータベースファイルに送信された内容を格納します。

* 初期設定
必要なパッケージをrequirements.txtに記述しています。
以下を実行してください。

pip install -r requirements.txt

* 使い方
python server.py
→サーバが起動します。

別のターミナルで、以下を実行します。
python client.py

うまく行けば、以下のように表示されます。
$ python client.py
add[0] 200:ok
add[1] 200:ok
add[2] 200:ok
add[3] 200:ok
add[4] 200:ok
show 200:{
	"data":{
	"2020-06-06/05/20 09:13:13":{"humidity":30.0,"numOfPeople":10,"recdate":"2020-13-06/05/20_09-06-13","temperature":25.0},
	"2020-06-06/05/20 09:13:19":{"humidity":31.0,"numOfPeople":11,"recdate":"2020-13-06/05/20_09-06-19","temperature":26.0},
	"2020-06-06/05/20 09:13:25":{"humidity":32.0,"numOfPeople":12,"recdate":"2020-13-06/05/20_09-06-25","temperature":27.0},
	"2020-06-06/05/20 09:13:31":{"humidity":33.0,"numOfPeople":13,"recdate":"2020-13-06/05/20_09-06-31","temperature":28.0},
	"2020-06-06/05/20 09:13:37":{"humidity":34.0,"numOfPeople":14,"recdate":"2020-13-06/05/20_09-06-37","temperature":29.0},
	"2020-06-06/05/20 09:14:52":{"humidity":30.0,"numOfPeople":10,"recdate":"2020-14-06/05/20_09-06-52","temperature":25.0},
	"2020-06-06/05/20 09:14:58":{"humidity":31.0,"numOfPeople":11,"recdate":"2020-14-06/05/20_09-06-58","temperature":26.0},
	"2020-06-06/05/20 09:15:04":{"humidity":32.0,"numOfPeople":12,"recdate":"2020-15-06/05/20_09-06-04","temperature":27.0},
	"2020-06-06/05/20 09:15:10":{"humidity":33.0,"numOfPeople":13,"recdate":"2020-15-06/05/20_09-06-10","temperature":28.0},
	"2020-06-06/05/20 09:15:17":{"humidity":34.0,"numOfPeople":14,"recdate":"2020-15-06/05/20_09-06-17","temperature":29.0}
},"result":true}

5件のデータをデータ登録APIを実行してDBに登録して、
直近10件を参照するサンプルです。


client.pyのURLの部分を編集することで、サーバとクライアントを別々のマシンで実行することもできます。



