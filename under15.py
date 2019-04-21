from flask import Flask, flash, jsonify, redirect, render_template, request, session, abort
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
 
@app.route("/students/")
def student():
        req=request.args.get('under15')
        over15 = []
        under15 = []
        for student in range(len(students)):
                name = students[student]['name']
                age = students[student]['age']
                line = 'Name: %s | Age: %d' %(name,age)
                if age >= 15:
                        over15.append(line)
                else:
                        under15.append(line)   
        if req == 'true':
                return jsonify(under15)
        elif req == 'false':
                return jsonify(over15)

if __name__ == "__main__":
	app.run(debug=True)
