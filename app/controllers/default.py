from app import app, db
from flask import render_template, request, redirect, session
from app.models.tables import Task

@app.route('/')
def homePage():
    return render_template('home.html')


@app.route('/taskList')
def taskListPage():
    r = Task.query.order_by(Task.id.desc()).all()
    print(len(r))
    return render_template('taskList.html', r=r)

@app.route('/deletar_registro/<int:registro_id>', methods=['POST'])
def deletar_registro(registro_id):
    registro = Task.query.filter_by(id=registro_id).first() 
    db.session.delete(registro)
    db.session.commit()
    return redirect('/taskList')


@app.route('/newTask', methods=['GET', 'POST'])
def criar_registro():
    if request.method == 'POST':
        campo1 = request.form['campo1']
        campo2 = request.form['campo2']
        
        novo_registro = Task(tituloTarefa=campo1, descricaoTarefa=campo2)
        db.session.add(novo_registro)
        db.session.commit()
        
        return redirect('/taskList')
    
    return render_template('/newTask.html')

@app.route('/newTask2', methods=['GET', 'POST'])
def criar_registro2():
    if request.method == 'POST':
        campo1 = request.form['campo1']
        campo2 = request.form['campo2']
        
        novo_registro = Task(tituloTarefa=campo1, descricaoTarefa=campo2)
        db.session.add(novo_registro)
        db.session.commit()
        
        return redirect('/taskList')
    
    return render_template('/newTask2.html')

@app.route('/selecionarRegistro/<int:registro_id>', methods=['GET', 'POST'])
def selecionarRegistroPraEditar(registro_id):
    if request.method == 'POST':
        session['registroSelecionado'] = registro_id
    print(registro_id)
    return render_template('editTask.html')

@app.route('/editar_registro/<int:registro_id>', methods=['POST'])
def editar_registro(registro_id):
    if request.method == 'POST':
        campo1 = request.form['campo1']
        campo2 = request.form['campo2']
        registroSelecionado = Task.query.filter_by(id=registro_id).first()
        registroSelecionado.tituloTarefa = campo1
        registroSelecionado.descricaoTarefa = campo2

        db.session.commit()
        return redirect('/taskList')
    return render_template('editTask.html')

@app.route('/teste', methods=['GET','POST'])
def teste():
    x = 'cuida'
    return render_template('teste.html', x=x)