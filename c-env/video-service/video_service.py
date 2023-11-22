from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content.db'
db = SQLAlchemy(app)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    video_filename = db.Column(db.String(255), nullable=False)

@app.route('/content', methods=['GET'])
def get_content():
    with app.app_context():
        content_list = Content.query.all()
        content_data = [{'title': c.title, 'description': c.description, 'video_filename': c.video_filename} for c in content_list]
    return jsonify(content_data)

@app.route('/content', methods=['POST'])
def add_content():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    video_filename = data.get('video_filename')

    with app.app_context():
        content = Content(title=title, description=description, video_filename=video_filename)
        db.session.add(content)
        db.session.commit()

    return jsonify({'message': 'Content added'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5002)