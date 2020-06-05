from flask import Flask,render_template,jsonify,make_response,abort,request
import datetime
import peewee


db = peewee.SqliteDatabase("data.db")


class VentilationInfo(peewee.Model):
    recdate = peewee.DateTimeField()
    temperature = peewee.FloatField()
    humidity = peewee.FloatField()
    numOfPeople = peewee.IntegerField()

    class Meta:
        database = db

api = Flask(__name__)

@api.route('/getVentilation/<int:numOfRecord>', methods=['GET'])
def get_Ventilations(numOfRecord):
    try:
        ventilist = VentilationInfo.select().order_by(VentilationInfo.recdate.desc()).limit(numOfRecord)
    except VentilationInfo.DoesNotExist:
        abort(404)
    result = {
        "result":True,
        "data":{
            }
        }
    for v in ventilist:
        key=v.recdate.strftime('%Y-%m-%D %H:%M:%S')
        result["data"][key]={"recdate":v.recdate.strftime('%Y-%M-%D_%H-%m-%S'),"temperature":v.temperature,"humidity":v.humidity,"numOfPeople":v.numOfPeople}

    return make_response(jsonify(result))

@api.route('/addVentilation/', methods=['POST'])
def add_Ventilation():
    result="ok"
    try:
        db.create_tables([VentilationInfo])
        d = datetime.datetime.now()
        t = request.form["temperature"]
        h = request.form["humidity"]
        p = request.form["numOfpeople"]
        print("{} {} {} {}".format(d,t,h,p))
        v = VentilationInfo(recdate=d,temperature=t,humidity=h,numOfPeople=p)
        v.save()
    except Exception as e:
        print(e)
        result="ng"
    return result

@api.route('/delVentilation/', methods=['POST'])
def del_Ventilation():
    result="ok"
    try:
        q = VentilationInfo.delete()
        q.execute()
    except Exception as e:
        print(e)
        result="ng"
    return result

@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3000)
