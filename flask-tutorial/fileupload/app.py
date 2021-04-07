from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from io import BytesIO


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///filestorage.db'
db = SQLAlchemy(app)

class FileContents(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(300))
	data = db.Column(db.LargeBinary)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
	file = request.files['inputFile']

	newFile = FileContents(name=file.filename, data=file.read())
	db.session.add(newFile)
	db.session.commit()

	return 'Saved ' + file.filename + ' to the database!'

@app.route('/download')
def download():
	file_data = FileContents.query.filter_by(id=1).first()
	return send_file(BytesIO(file_data.data), attachment_filename='test.odt', as_attachment=True)


if __name__ == '__main__':
	app.run(debug=True)