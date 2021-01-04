import os
from datetime import date
import pandas as pd
import json
from jinja2 import Markup
import uuid
from flask import request, render_template
from flask_admin.model import typefmt
from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import FileUploadField
from wtforms import PasswordField
from wtforms.validators import DataRequired
from KashTable.models import AVAILABLE_USER_TYPES
from KashTable import bcrypt
from KashTable.config import Config
from KashTable.posts import utils


# Create directory for file fields to use
file_path = Config.FILE_PATH + '/archive'

try:
    os.mkdir(file_path)
except OSError:
    pass


class CustomPasswordField(PasswordField): 
    
    def populate_obj(self, obj, name):
        setattr(obj, name, bcrypt.generate_password_hash(self.data).decode('utf-8'))


class UserCRUD(ModelView):
    
    list_template = 'admin/my_clients.html'
    page_size = 100
    can_set_page_size = True
    can_view_details = True
    can_export = True
    export_types = ['csv', 'xls']
    form_choices = {
        'type': AVAILABLE_USER_TYPES,
    }
    form_widget_args = {
        'id': {
            'readonly': True
        }
    }
    column_list = [
        'activated',
        'type',
        'bundle',
        'company_name',
        'email',
        'phone_number',
    ]
    column_searchable_list = [
        'company_name',
        'email',      
    ]
    column_editable_list = [
        'type', 
        'bundle', 
        'activated'
    ]
    column_details_list = [
        'id',
        'activated',
        'type',
        'bundle',
        'company_name',
        'first_name',
        'last_name',
        'email',
        'phone_number',        
        'street',
        'postcode',
        'city',
        'country',
        'siren',
        'password'

    ]
    form_columns = [
        'id',
        'type',
        'last_name',
        'first_name',
        'email',
        'company_name',
        'street',
        'postcode',
        'city',
        'country',
        'siren',        
        'phone_number',
        'bundle',
        'activated',
        'password'
    ]
    form_create_rules = [
        'type',
        'last_name',
        'first_name',
        'email',
        'company_name',
        'street',
        'postcode',
        'city',
        'country',
        'siren',     
        'phone_number',
        'bundle',
        'activated',
        'password'
    ]

    column_auto_select_related = True
    column_default_sort = [('type', False), ('company_name', False)]  # sort on multiple columns

    # custom filter: each filter in the list is a filter operation (equals, not equals, etc)
    # filters with the same name will appear as operations under the same filter
    column_filters = [
        'type',
        'last_name',
        'first_name',
        'email',
        'company_name',
        'street',
        'postcode',
        'city',
        'country',
        'siren',        
        'phone_number',
        'bundle',
        'activated',
    ]

    form_extra_fields = {
        'password': CustomPasswordField('Password')
    }
  

class FileCRUD(ModelView):
 
    def _date_format(view, value):
        return value.strftime('%B %Y')

    def _json_formatter(view, context, model, name):
        """Format model.doc as it is extracted in route posts.table in order to
        give realistic reprensentation of the client side"""
        value = getattr(model, name)
        df = pd.json_normalize(value)
        # split tables into different tabs
        list_tables = list(df['table_name'].drop_duplicates())
        items = {}
        for table_name in list_tables:  
            frame = df.loc[df['table_name'] == table_name]
            # dict table_name as key, tuple (id, rendered html tables)
            items.update( {table_name: ( uuid.uuid4(), utils.table(frame).financials() )} )
        return Markup(render_template('admin/details.html', items=items))

    def on_model_change(self, form, model, is_created=False):
        file = request.get_array(field_name='doc')
        df = pd.DataFrame(file)
        # convert first row to column header
        df = df.rename(columns=df.iloc[0]).drop(df.index[0])
        df = df.apply( pd.to_numeric, errors='ignore')
        # load to db
        model.doc = json.loads(df.to_json(orient='records', date_format='iso'))


    list_template = 'admin/my_files.html'    
    MY_DEFAULT_FORMATTERS = dict(typefmt.BASE_FORMATTERS)
    MY_DEFAULT_FORMATTERS.update({
        date: _date_format       
    })    
    column_type_formatters = MY_DEFAULT_FORMATTERS
    form_args = dict(
        time = dict(validators=[DataRequired()],format='%B %Y')
    )
    form_widget_args = dict(
        time={'data-date-format': u'%B %Y'} 
    )
    page_size = 100
    can_set_page_size = True
    can_view_details = True
    can_edit = False
    column_list = [
        'user', 
        'name', 
        'date', 
    ]
    column_details_list = [
        'id',
        'user',
        'name',
        'date',
        'doc'             
    ]
    form_columns = [
        'user', 
        'name',
        'date',
        'doc',
    ]
    column_default_sort = [
        ('user.company_name', False), 
        ('user.email', False), 
        ('date', True)
    ]
    can_export = True
    export_types = ['csv', 'xls']
    column_sortable_list = [
        ('user', ('user.company_name', 'user.email')),  # sort on multiple columns
        'name',       
        'date',
    ]
    column_searchable_list = [
        'user.company_name',
        'user.email',
        'name',
        'date'
    ]
    column_filters = [
        'user.company_name',
        'user.email',
        'name',     
        'date',
    ]
    column_formatters = {
        'doc': _json_formatter,
    }    
    form_overrides = {
        'doc': FileUploadField
    }
    # Pass additional parameters to 'path' to FileUploadField constructor
    form_args = {
        'doc': {
            'label': 'Doc',
            'base_path': file_path,
            'allow_overwrite': True
        }
    }