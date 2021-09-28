
from logging import DEBUG
from flask import Flask, request

app = Flask(__name__)

def ERP5_1(body):
    stud_dict = {}
    u1 = int(body['u1'])
    u2 = int(body['u2'])
    u3 = int(body['u3'])
    p1 = int(body['p1'])
    p2 = int(body['p2'])
    f = int(body['f'])
    t_s = u1 + u2 + u3 + p1 + p2
    SfR = int(t_s)/int(f)
    stud_dict['u1'] = u1
    stud_dict['u2'] = u2
    stud_dict['u3'] = u3
    stud_dict['p1'] = p1
    stud_dict['p2'] = p2
    stud_dict['t_s'] = t_s
    stud_dict['SfR'] = SfR
    if SfR<=15:
        score= 20
    elif SfR<=17:
      score= 18
    elif SfR<=19:
      score= 16
    elif SfR<=21:
      score= 14
    elif SfR<=23:
      score= 12
    elif SfR<=25:
      score= 10
    elif SfR>25:
      score= 0
    print("marks=" +str(score))
    stud_dict['Score'] = score
    return  stud_dict


def ERP5_2(body):
    professors = {}
    N = body['N'] 
    a_f1 = int(body['a_f1'])
    a_f2 = int(body['a_f2'])
    a_f3 = int(body['a_f3'])
    r_f1=1/9*((N/15))
    r_f2=2/9*((N/15))
    r_f3=6/9*((N/15))
    r_f1=round(r_f1)
    r_f2=round(r_f2)
    r_f3=round(r_f3)
    professors['a_f1'] = a_f1
    professors['a_f2'] = a_f2
    professors['a_f3'] = a_f3
    professors['r_f1'] = r_f1
    professors['r_f2'] = r_f2
    professors['r_f3'] = r_f3

    if a_f1==a_f2==0:
        CRD=0
    else:
        CRD=((a_f1/r_f1)+((a_f2*0.6)/r_f2)+((a_f3*0.4)/r_f3))*12.5
    if CRD>25:
        CRD=25
    professors['CRD']=CRD
    print("Cadre Ratio Marks "+str(CRD))
    
    return professors , CRD


@app.route('/', methods = ['POST'])
def home():
    return "Welcome to The Point Seven"

@app.route('/5.1', methods = ['POST'])
def erp51():
    body = request.get_json()
    output = ERP5_1(body)
    return output

@app.route('/5.2', methods = ['POST'])
def erp52():
    body = request.get_json()
    output = ERP5_2(body)
    return output


if __name__ == '__main__':
    app.run(debug= True, port= 5000)
