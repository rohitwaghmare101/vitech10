New decorators are just mapper around the new API. The decorator are mandatory as webclient and HTTP controller are not 
compliant with new API.
api namespace decorators will detect signature using variable name and decide to match old signature or not.
Recognized variable names are:

cr, cursor, uid, user, user_id, id, ids, context

#@api.returns
#This decorator guaranties unity of returned value. 
#It will return a RecordSet of specified model based on original returned value:

@api.returns('res.partner')
def afun(self):
    ...
    return x  # a RecordSet
	
	
#@api.one
#This decorator loops automatically on Records of RecordSet for you. Self is redefined as current record:

@api.one
def afun(self):
    self.name = 'toto'
	

#@api.multi
Self will be the current RecordSet without iteration. It is the default behavior:

@api.multi
def afun(self):
    len(self)
	
#@api.model
#This decorator will convert old API calls to decorated function to new API signature.
#It allows to be polite when migrating code.

@api.model
def afun(self):
    pass
	
#@api.constrains
#This decorator will ensure that decorated function will be called
#on create, write, unlink operation. 
#If a constraint is met the function should raise a openerp.exceptions.Warning with appropriate message.

#@api.depends
#This decorator will trigger the call to the decorated function if any of the fields specified in the decorator
#is altered by ORM or changed in the form:

@api.depends('name', 'an_other_field')
def afun(self):
    pass

#@api.onchange
#This decorator will trigger the call to the decorated function if any of the fields specified in the decorator is changed in the form:

@api.onchange('fieldx')
def do_stuff(self):
   if self.fieldx == x:
      self.fieldy = 'toto'
	  
@api.noguess
#This decorator prevent new API decorators to alter the output of a method