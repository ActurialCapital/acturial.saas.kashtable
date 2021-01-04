import dateutil.parser


class table:
    
    """
    Styler according to key element located in excel spreadsheet. For further
    information about the method used here, please look at the pandas styling 
    documentation: ..pandas.pydata.org/pandas-docs/stable/user_guide/style.html
    """
    
    def __init__(self, df, uuid='table1'):
        self.uuid = uuid
        self.desc = 'Description'
        self.formatter = ['table_name', 
                          'font_weight', 
                          'font_color', 
                          'background_color',	
                          'font_family', 
                          'font_size', 
                          'text_align', 
                          'sort_by']
        self.dt = list(df.loc[:, ~df.columns.isin(self.formatter)].drop(self.desc, axis=1).columns)
        try:
            self.dt_formatted = [d.strftime("%b %Y") for d in self.dt]
        except:
            self.dt_formatted = [dateutil.parser.parse(d).strftime("%b %Y") for d in self.dt]
        self.attrs = 'class="table table-separate table-head-custom"'
        self.df = df.rename(columns=dict(zip(self.dt, self.dt_formatted)))
        self.df = self.df.dropna(axis=1, how='all')
        
    def _css_format(self, col, style):
        return lambda x: ["{style}: {col}".format(style=style, col=x[col]) for _ in x]
    
    def _value_format(self, applied_to):
        return dict(zip(applied_to, [lambda x: '{0:,.0f}'.format(x)] * len(applied_to)))

    def financials(self):
        return (self.df.style
            .format(self._value_format(applied_to=self.dt_formatted), na_rep="-")
            .set_table_attributes(self.attrs)
            .apply(self._css_format(col='font_weight',      style='font-weight'     ), axis=1)
            .apply(self._css_format(col='font_weight',      style='font-style'      ), axis=1)
            .apply(self._css_format(col='font_color',       style='color'           ), axis=1)
            .apply(self._css_format(col='background_color', style='background-color'), axis=1)
            .apply(self._css_format(col='font_family',      style='font-family'     ), axis=1)
            .apply(self._css_format(col='font_size',        style='font-size'       ), axis=1)
            .apply(self._css_format(col='text_align',       style='text-align'      ), axis=1)
            .hide_index()
            .hide_columns(self.formatter)
            .render(uuid=self.uuid))  