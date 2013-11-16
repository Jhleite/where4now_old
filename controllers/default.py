# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is the main controller
## - index is the default action of any application
#########################################################################

def index():
    """
    This action lists all the tourism operators that exist in the database.
    It orders them by operator name.
    """
    operators = db().select(db.operator.id, db.operator.name, orderby=db.operator.name)
    return dict(operators=operators)
    
def create_operator():
    """
    This action creates an tourism operator in the database.
    It creates a form with the fields corresponding to a table row.
    """
    form = SQLFORM(db.operator).process(next=URL('index'))
    return dict(form=form)
    
def show_operator():
    """
    This action shows a tourism operator.
    """
    this_operator = db.operator(request.args(0,cast=int)) or redirect(URL(index))
    return dict(operator=this_operator)
