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
        # added code
        result['Gender'] = request.form.get('gender') #radio
        result['Major'] = request.form.get('major') #select
        programming = request.form.getlist('programming_language') #checkbox
        result['Language'] = ', '.join(programming)
        # -----------------
        return render_template('result.html',result=result)


if __name__ =='__main__':
    app.run(debug=True)