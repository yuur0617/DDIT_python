
from flask import Flask, redirect,jsonify
from flask.globals import request
from flask.templating import render_template
import pymysql
from day10.daoemp import DaoEmp

app = Flask(__name__)

@app.route('/')
def index():
    
     #return '<script>location.href="static/ajax.html"</script>'
    return redirect('static/ajax.html')
    
@app.route('/ajax',methods=['POST'])
def ajax():

    data = request.get_json() # 브라우저가 요청해서 날린 파라미터 가져오기
    print(data['menu']) # 가져온 데이터 확인 - 딕셔너리 
    return jsonify(result = data) # 결과를 다시 브라우저로 반환해 주는 형태 설정'

@app.route('/emp_list',methods=['POST'])
def emp_list():
    de = DaoEmp()
    list = de.selectList()
    # print(list)
    return jsonify(list = list) 

@app.route('/emp_one',methods=['POST'])
def emp_one():
    data = request.get_json()
    e_id = data['e_id']
    de = DaoEmp()
    vo = de.select(e_id)
    return jsonify(vo = vo) 


@app.route('/emp_mod',methods=['POST'])
def emp_mod():
    data = request.get_json()
    e_id = data['e_id']
    e_name = data['e_name']
    gen = data['gen']
    addr = data['addr']
    
    print(e_id,e_name,gen,addr)
    de = DaoEmp()
    cnt = de.update(e_id, e_name, gen, addr)
    return   jsonify(cnt = cnt) 

@app.route('/emp_add',methods=['POST'])
def emp_add():
    data = request.get_json()
    e_id = data['e_id']
    e_name = data['e_name']
    gen = data['gen']
    addr = data['addr']
    
    print(e_id,e_name,gen,addr)
    de = DaoEmp()
    cnt = de.insert(e_id, e_name, gen, addr)
    return   jsonify( cnt =  cnt) 


@app.route('/emp_del',methods=['POST'])
def emp_del():
    data = request.get_json()
    e_id = data['e_id']  
    de = DaoEmp()
    cnt = de.delete(e_id)
    # cnt = de.delete(6)
    print('e_id',e_id)
    print('cnt',cnt)
    return jsonify(cnt = cnt) 



if __name__ == '__main__':

    app.run(debug=True)