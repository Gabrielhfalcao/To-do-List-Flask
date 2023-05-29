from app import db

class Task(db.Model):

    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    tituloTarefa = db.Column(db.String)
    descricaoTarefa = db.Column(db.String)

    def __init__(self, tituloTarefa, descricaoTarefa):
        self.tituloTarefa = tituloTarefa
        self.descricaoTarefa = descricaoTarefa

    def __repr__(self):
        return '<%r>' % self.id

    
