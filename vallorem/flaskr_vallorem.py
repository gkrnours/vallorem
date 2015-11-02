import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash


# create our little application :)
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, '/tmp/flask.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('getall_personne'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


"""PERSONNES"""


@app.route('/personne')
def getall_personne():
    db = get_db()
    cur = db.execute('SELECT nom, prenom,mail, mdp, statut,equipe,date_recrutement,permanent FROM personne order by id desc')
    personnes = cur.fetchall()
    return render_template('show_personnes.html', personnes=personnes)


@app.route('/personne/<int:personne_id>')
def getById_personne(personne_id):
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('ELECT nom, prenom,mail, mdp, statut,equipe,date_recrutement,permanent FROM personne WHERE id=?',
               [request.form['nom'], request.form['prenom'], request.form['mail'], request.form['mdp'],request.form['statut'], request.form['equipe'],
                request.form['date_recrutement'], request.form['permanent'], personne_id])
    db.commit()
    return redirect(url_for('getall_personne'))


@app.route('/personne/add', methods=['POST'])
def add_personne():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('INSERT INTO personne (nom, prenom,statut,equipe,date_recrutement,permanent) VALUES (?,?,?,?,?,?)',
               [request.form['nom'], request.form['prenom'], request.form['statut'], request.form['equipe'],
                request.form['date_recrutement'], request.form['permanent']])
    db.commit()
    flash('Nouvelle personne ajoutée')
    return redirect(url_for('getall_personne'))


@app.route('/personne/update/<int:personne_id>', methods=['PUT'])
def update_personne(personne_id):
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('UPDATE personne SET nom=?, prenom=?, statut=?, equipe=?, date_recrutement=?, permanent=? WHERE id=?',
               [request.form['nom'], request.form['prenom'], request.form['statut'], request.form['equipe'],
                request.form['date_recrutement'], request.form['permanent'], personne_id])
    db.commit()
    flash('personne modifiée')
    return redirect(url_for('getall_personne'))


@app.route('/personne/delete/<int:personne_id>', methods=['DELETE'])
def delete_personne(personne_id):
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('DELETE FROM personne WHERE id=?',
               [personne_id])
    db.commit()
    flash('personne supprimée')
    return redirect(url_for('getall_personne'))


"""STATUT"""


@app.route('/statut')
def getall_statut():
    db = get_db()
    cur = db.execute('SELECT description FROM statut order by id desc')
    statuts = cur.fetchall()
    return render_template('show_statuts.html', statuts=statuts)


@app.route('/statut/<int:statut_id>')
def getbyid_statut(statut_id):
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('SELECT description FROM statut WHERE id=?',
               [request.form['description'], statut_id])
    db.commit()
    return redirect(url_for('getall_statut'))


@app.route('/statut/add', methods=['POST'])
def add_statut():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('INSERT INTO statut (description) VALUES (?)',
               [request.form['description']])
    db.commit()
    flash('Nouveau statut ajouté')
    return redirect(url_for('getall_statut'))


@app.route('/statut/update/<int:statut_id>', methods=['PUT'])
def update_statut(statut_id):
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('UPDATE statut SET description=? WHERE id=?',
               [request.form['description'], statut_id])
    db.commit()
    flash('statut modifié')
    return redirect(url_for('getall_statut'))


@app.route('/statut/delete/<int:statut_id>', methods=['DELETE'])
def delete_statut(statut_id):
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('DELETE FROM statut WHERE id=?',
               [statut_id])
    db.commit()
    flash('statut supprimé')
    return redirect(url_for('getall_statut'))


"""TYPE_PRV"""


@app.route('/type_prv')
def getall_type_prv():
    db = get_db()
    cur = db.execute('SELECT description FROM type_prv order by id desc')
    type_prvs = cur.fetchall()
    return render_template('show_type_prvs.html', type_prvs=type_prvs)


@app.route('/type_prv/<int:type_prv_id>')
def getbyid_type_prv(type_prv_id):
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('SELECT description FROM type_prv WHERE id=?',
               [request.form['description'], type_prv_id])
    db.commit()
    return redirect(url_for('getall_type_prv'))


@app.route('/type_prv/add', methods=['POST'])
def add_type_prv():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('INSERT INTO type_prv (description) VALUES (?)',
               [request.form['description']])
    db.commit()
    flash('Nouveau type_prv ajouté')
    return redirect(url_for('getall_type_prv'))


@app.route('/type_prv/update/<int:type_prv_id>', methods=['PUT'])
def update_type_prv(type_prv_id):
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('UPDATE type_prv SET description=? WHERE id=?',
               [request.form['description'], type_prv_id])
    db.commit()
    flash('type_prv modifié')
    return redirect(url_for('getall_type_prv'))


@app.route('/statut/delete/<int:type_prv_id>', methods=['DELETE'])
def delete_type_prv(type_prv_id):
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('DELETE FROM type_prv WHERE id=?',
               [type_prv_id])
    db.commit()
    flash('type_prv supprimé')
    return redirect(url_for('getall_type_prv'))


"""EQUIPE"""


@app.route('/equipe')
def getall_equipe():
    db = get_db()
    cur = db.execute('SELECT nom, axe FROM equipe order by id desc')
    equipes = cur.fetchall()
    return render_template('show_personnes.html', equipes=equipes)


@app.route('/equipe/<int:equipe_id>')
def getById_equipe(equipe_id):
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('UPDATE equipe SET nom=?, axe=? WHERE id=?',
               [request.form['nom'], request.form['prenom'], request.form['statut'], request.form['equipe'],
                request.form['date_recrutement'], request.form['permanent'], personne_id])
    db.commit()
    return redirect(url_for('getall_equipe'))


@app.route('/equipe/add', methods=['POST'])
def add_equipe():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('INSERT INTO equipe (nom, axe) VALUES (?,?)',
               [request.form['nom'], request.form['axe']])
    db.commit()
    flash('Nouvelle equipe ajoutée')
    return redirect(url_for('getall_equipe'))


@app.route('/equipe/update/<int:equipe_id>', methods=['PUT'])
def update_equipe(equipe_id):
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('UPDATE equipe SET nom=?, axe=? WHERE id=?',
               [request.form['nom'], request.form['axe'], equipe_id])
    db.commit()
    flash('equipe modifiée')
    return redirect(url_for('getall_equipe'))


@app.route('/equipe/delete/<int:equipe_id>', methods=['DELETE'])
def delete_equipe(equipe_id):
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('DELETE FROM equipe WHERE id=?',
               [equipe_id])
    db.commit()
    flash('equipe supprimée')
    return redirect(url_for('getall_equipe'))

if __name__ == '__main__':
    app.run()

