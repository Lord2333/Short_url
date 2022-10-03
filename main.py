from flask import Flask, request, render_template, redirect, escape
import json, random, time
from deta import App, Base

#  Todo  未检测重复Short_code


# app = Flask(__name__)
app = App(Flask(__name__))

@app.lib.cron()
def cron_job(event):
	check_code()

@app.route('/', methods=["GET"])
def index():
	return render_template('./index.html')


@app.route('/S_url', methods=['POST'])
def make_url():
	Form = json.loads(request.data)
	orgi_url = Form.get("orgi_url")
	short_code = Form.get("short_code")
	Type = Form.get("type")
	t = Form.get("Time")
	if short_code == '':
		short_code = Rand_url()
	resp = {
		'short_code': short_code
	}
	up_url(orgi_url, short_code, t, Type)
	return resp

@app.route("/<short_code>",methods=['GET'])
def deal_url(short_code):
	return Fetch_code(short_code)

def Fetch_code(code):
	# deta = Deta(deta_key)
	# db = deta.Base('Short')
	db = Base('Short')
	res = db.fetch({"Short_code": code}).items
	if len(res) != 0:
		if res[0]['type'] == 'link':
			return redirect(res[0]['Content'])
		else:
			return res[0]['Content']
	else:
		return '<h1>寄！</h1><p>您输入的短链接莫名其妙的没了呢~</p>'


def Rand_url():
	ran_str = ''.join(random.sample('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890', 5))
	return ran_str


def up_url(url, code, t, type):
	# deta = Deta(deta_key)
	# db = deta.Base('Short')
	db = Base('Short')
	if type != 'link':
		url = escape(url)
	Data = {
		'Content': url,
		'Short_code': code,
		'time': t,
		'type': type,
		'up_time': time.time()
	}
	db.put(Data)


def check_code():
	# deta = Deta(deta_key)
	# db = deta.Base('Short')
	db = Base('Short')
	res = db.fetch()
	for item in res.items:
		up_time = item['up_time']
		now_time = time.time()
		if now_time - up_time > int(item['time'])*24*3600:
			db.delete(item['key'])

if __name__ == '__main__':
	app.run()
