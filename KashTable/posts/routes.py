import os
import pandas as pd
import numpy as np
from flask_login import current_user, login_required
from flask import (
    render_template, 
    url_for, 
    flash, 
    redirect, 
    request, 
    Blueprint,  
    current_app,
    g,
    session
    )
from KashTable.models import File
from KashTable.posts import utils
from KashTable.posts.forms import (
    UploadForm, 
    TableForm,
    GraphForm,
    )


posts = Blueprint('posts', __name__)
 

@posts.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = UploadForm()
    user_email = str(current_user.email)
    try:
        os.mkdir(os.path.join(current_app.root_path, 'files/raw/' + user_email))
    except OSError:
        pass
    if request.method == 'POST':
        if form.validate_on_submit():
            file = request.get_array(field_name='file')
            df = pd.DataFrame(file)
            path = current_app.root_path
            name = str(form.dt.data)
            
            with pd.ExcelWriter(os.path.join(path, f'files/raw/{user_email}/{name}.xlsx')) as writer:
                df.to_excel(writer)
            
            with open(os.path.join(path, f'files/raw/{user_email}/{name}.txt'), "w") as text_file:
                print(f"Title: {form.title.data}\nBody: {form.body.data}", file=text_file)
            
            flash('File has been uploaded successfuly!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('OOPS! Something went wrong here! Please try again.', 'danger')
    return render_template('user_upload.html', form=form)

    
@posts.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']
            
@posts.route('/<string:table_name>', methods=['GET', 'POST'])
@login_required
def table(table_name):   

    def refresh(doc):
        """Filter out table using table_name column in pandas.DataFrame obj
        Note: Do not modify uuid=table1, as it matches $("#T_table1").DataTable() 
        in template. Note that the "T_" is created by pandas.DataFrame().style
        .render() located in .users.render.table class. For more information 
        visit pandas.pydata.org.
        """
        doc = pd.json_normalize(doc)
        df = doc.loc[doc["table_name"] == table_name] # filter to access spec table
        return utils.table(df, uuid='table1').financials()  

    form = TableForm()
    user = File.query.filter_by(user_id=current_user.id)
    try:
        file = user.order_by(File.date.desc()).first()
        form.opts.choices = [(item.id, item.date.strftime('%B %Y')) for item in user.all()]
  
        try:
            if request.method == 'POST':
                ufile = user.filter_by(id=form.opts.data).first()
                tb = refresh(ufile.doc)
                session.pop('user', None)
                session['user'] = form.opts.data
                flash(f"Updated as at {ufile.date.strftime('%B %Y')}.", 'info')
                return render_template('table.html', title=table_name, tb=tb, form=form) 
            elif session['user']==None: # before first request
                tb = refresh(file.doc)
                flash(f"Updated as at {file.date.strftime('%B %Y')}.", 'info')
            else:
                ufile = user.filter_by(id=session['user']).first()
                form.opts.data = session['user']
                tb = refresh(ufile.doc)
                flash(f"Updated as at {ufile.date.strftime('%B %Y')}.", 'info')
            return render_template(
                'table.html', 
                title=table_name, 
                tb=tb, 
                form=form,
                )  
        except:
            tb = refresh(file.doc)
            flash(f"Updated as at {file.date.strftime('%B %Y')}.", 'info')
            return render_template(
                'table.html', 
                title=table_name, 
                tb=tb, 
                form=form,
                )  
    except:
        flash('OOPS! There is no materials to display!', 'danger')
        flash('Please contact us and upload a project.', 'info')
        return redirect(url_for('posts.upload'))  


import dateutil
@posts.route('/graph', methods=['GET', 'POST'])
@login_required
def graph(): 
    
    def reshape(doc):
        doc = pd.json_normalize(doc)   
        df = doc.loc[doc["table_name"].isin(['Bilan', 'Compte de Resultat Analytique Cumulé'])]
        labels = 'Description'
        formatter = ['table_name', 
                     'font_weight', 
                     'font_color', 
                     'background_color',	
                     'font_family', 
                     'font_size', 
                     'text_align', 
                     'sort_by']        
        dt = list(df.loc[:, ~df.columns.isin(formatter)].drop(labels, axis=1).columns)
        dt_formatted = [str(dateutil.parser.parse(d).strftime("%b %Y")) for d in dt]
        df = df.rename(columns=dict(zip(dt, dt_formatted)))
        df = df.drop(formatter, axis=1)
        df = df.set_index(labels)
        df = df.dropna(axis=1, how='all')
        df = df.replace(np.nan, 'null')
        df = round(df, 0)
        return df
    
    form = GraphForm()
    user = File.query.filter_by(user_id=current_user.id)

    file = user.order_by(File.date.desc()).first()
    doc = file.doc
    df = reshape(doc)

    form.opts.choices = [(item.id, item.date.strftime('%B %Y')) for item in user.all()]
    
    choice_labels = [(label, label) for _, label in enumerate(df.index)]
    
    choice_labels.append(("--", "--"))
    
    form.series_1.choices = choice_labels
    form.series_2.choices = choice_labels
    form.series_3.choices = choice_labels
    
    if request.method == 'POST':
#        ufile = user.filter_by(id=form.opts.data).first()
#        df = reshape(ufile.doc)      
#        flash(f"Updated as at {ufile.date.strftime('%B %Y')}.", 'info')
        return render_template(
            'graph.html', 
            title='Dashboard',
            chart_id='chart1', 
            df=df, 
            form=form
            ) 
    
    # default
    form.series_1.data = "Chiffre d'affaires"
    form.series_2.data = "--"
    form.series_3.data = "--"
    
    return render_template(
        'graph.html', 
        title='Dashboard', 
        chart_id='chart1',
        df=df,
        form=form,
        )

