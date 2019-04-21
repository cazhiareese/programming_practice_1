
from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

students = [
	{'name': 'hersey', 'age':14, 'leader': 'michaels'},
	{'name': 'lei', 'age':15, 'leader': 'eleazar'},
	{'name': 'elyssa', 'age':16, 'leader': 'kulot'},
	{'name': 'jagmoc', 'age':16, 'leader': 'apen'},
	{'name': 'cazhia', 'age':15, 'leader': 'jabala'},
	{'name': 'lea', 'age':17, 'leader': 'lopez'},
	{'name': 'naruto', 'age':17, 'leader': 'kakashi'},
	{'name': 'gelo', 'age':15, 'leader': 'leindra'},
	{'name': 'cedy', 'age':17, 'leader': 'gia'}
]  
@app.route("/")
def index():
	return "Hey!"
 
@app.route("/students/<string:name>/")
def student(name):
	for student in students:
		if name == student.get('name'):
			print (student.get('age'))
			print (student.get('leader'))
			age = student.get('age')
			leader = student.get('leader')
			return render_template('unit.html',**locals())
	return render_template('lss.html',**locals())	
 
if __name__ == "__main__":
	app.run()