from flask import Flask, render_template
app=Flask(__name__)

@app.route("/temp2")
def index():
	name='abc'
	list1=[1,2,3]
	return render_template('tmp1.html',name=name,list=list1)
	
if __name__=='__main__':
    app.run(debug=True)