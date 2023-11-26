from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def input():
    return render_template('input.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method =='POST':
        result=dict()
        result['Name']=request.form.get('name')
        result['Student Number']=request.form.get('StudentNumber')
        result['college']=request.form.get('college')
        result['Gender'] = request.form.get('gender') #radio
        result['Major'] = request.form.get('major') #select
        email = request.form.get('email') #email
        email_domain = request.form.get('email_domain')
        result['Email'] = f"{email}@{email_domain}"
        programming = request.form.getlist('programming_language') #checkbox
        result['Language'] = ', '.join(programming)
        return render_template('result.html',result=result)


if __name__ =='__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
