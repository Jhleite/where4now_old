# -*- coding: utf-8 -*-

#db = DAL('sqlite://storage.sqlite')
#db = DAL('postgres://Hugo:Satriani@localhost/db')
db = DAL('postgres://postgres:Satriani@localhost/test')

from gluon.tools import *
auth = Auth(db)
auth.define_tables()
crud = Crud(db)

#
# Table that defines a touristic operator
# - GPS coordinates of the building, operator code, NIF and
#   NIB shopuld be unique
# - segments : Tourism segments of operation (list)
# - regions  : Regions of operation (list)
#
db.define_table('operator',
    Field('name'),
    Field('code', unique=True),
    Field('nif', unique=True),
    Field('nib', unique=True),
    Field('address', 'text'),
    Field('email'),
    Field('website'),
    Field('gpscoord', unique=True),
    Field('segments'),
    Field('regions'),
    format='%(name)s')

db.operator.name.requires = IS_NOT_IN_DB(db, db.operator.name)
db.operator.name.requires = IS_NOT_EMPTY()
db.operator.code.requires = IS_NOT_IN_DB(db, db.operator.code)
db.operator.code.requires = IS_NOT_EMPTY()
db.operator.nif.requires  = IS_NOT_IN_DB(db, db.operator.nif)
db.operator.nif.requires  = IS_NOT_EMPTY()
db.operator.nib.requires  = IS_NOT_IN_DB(db, db.operator.nib)
db.operator.nib.requires  = IS_NOT_EMPTY()
db.operator.gpscoord.requires  = IS_NOT_IN_DB(db, db.operator.gpscoord)
db.operator.email.requires = IS_EMAIL()

#
# People of contact for a given touristic operator
#    
db.define_table('contact',
    Field('operator_id', 'reference operator'),
    Field('name'),
    Field('phone'),
    Field('mobile'),
    Field('fax'),
    Field('email'),
    Field('observations', 'text'),
    format='%(name)s')

db.contact.operator_id.requires = IS_IN_DB(db, db.operator.id)
db.contact.name.requires = IS_NOT_EMPTY()
db.contact.email.requires = IS_EMAIL()
db.contact.operator_id.writable = db.contact.operator_id.readable = False

#
# Services available for a given touristic operator
#    
db.define_table('service',
    Field('operator_id', 'reference operator'),
    Field('name'),
    Field('code', unique=True),
    Field('risk_level'),
    Field('selling_price'),
    Field('operator_price'),
    Field('comission'),
    Field('opening_time', 'time'),
    Field('closing_time', 'time'),
    Field('start_time', 'datetime'),
    Field('duration', 'time'),
    Field('mean_appreciation'),
    Field('gpscoord', unique=True),
    Field('segments'),
    Field('region'),
    format='%(name)s')
    
db.service.operator_id.requires = IS_IN_DB(db, db.operator.id)
db.service.gpscoord.requires = IS_NOT_IN_DB(db, db.service.gpscoord)
db.service.operator_id.writable = db.service.operator_id.readable = False   

#
# Service extensions for a given touristic service
#    
db.define_table('service_extension',
    Field('service_id', 'reference service'),
    Field('name'),
    Field('selling_price'),
    Field('operator_price'),
    Field('comission'),
    format='%(name)s')

db.service_extension.service_id.requires = IS_IN_DB(db, db.service.id)    
db.service_extension.service_id.writable = db.service_extension.service_id.readable = False

#
# Photos for a given touristic service
#    
db.define_table('photo',
    Field('service_id', 'reference service'),
    Field('title', unique=True),
    Field('file', 'upload'),
    format='%(title)s')

db.photo.service_id.requires = IS_IN_DB(db, db.service.id)    
db.photo.service_id.writable = db.photo.service_id.readable = False
    
db.define_table('cust_comment',
    Field('service_id', 'reference service'),
    Field('comment', 'text'),
    Field('appreciation'))
    
db.cust_comment.service_id.requires = IS_IN_DB(db, db.service.id)
db.cust_comment.service_id.writable = db.cust_comment.service_id.readable = False
