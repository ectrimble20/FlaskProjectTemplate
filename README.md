# Flask Project Template

This is mostly for my own use, but if someone stumbles on this, feel free to utilize this if you think it'll 
help you get started with Flask.

This is a starting point for a Flask project, it includes enough stuff to get a basic Flask site up and 
running quickly.

So lets go through what's actually in this and how to use this.

First, you'll notice the `build.py` and the `run.py` scripts.  These should be fairly easy to understand as 
their names are descriptive.

`build.py` is used to initially build our data structure based off the model.  This should only be run once 
or when changes have been made to the model.  Generally, you'll want to draw out your data model on paper, 
work out the kinks, then start working with code.  However you go about it, once you have your `models.py` 
populated, you'll want to go through the `build.py` file and add in the appropriate includes in order to 
give the ORM (SQLAlchemy) access to built it's model.  For information on SQLAlchemy, see the link below 
this section.

[SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/latest/genindex.html)
[Flask-SQLAlchemy Documentation](http://flask.pocoo.org/docs/1.0/patterns/sqlalchemy/)

`run.py` as it's name implies is the main execution point for the application.  You'll generally want to 
over-write settings used outside of production here. For instance, you might want to turn on debug, change 
the logging levels, set the database handle, etc.  Generally speaking, this is all you need to do prior to 
running so long as you've run `build.py` and you're database/data structure is established.

#### Where code lives

The structure of the application is laid out as **I** usually setup my application.  This is by no means 
**THE** way to do this.  Feel free to experiment with it and settle on something you like.  Below is an 
explaination of the files and directories that are already in place and what they're used for and why they 
are where they are.

##### Directory structure

`/flashproject/forms/`

This is where the **flask_wtf** form classes live.  It is setup as a python module directory so it can be 
easily called with `flaskproject.forms.my_form.CLASS`.

`/flashproject/routes/`

This is where the mean and potatoes are built.  Generally speaking, most of the logic will end up in the 
routes, at least initially.  This is where you can build your `flask.Blueprint` objects and establish the 
`@my_blueprint.route(XXX)` routing logic required for the application to route incoming HTTP requests.

`/flashproject/static/`

Used if you're building a web page into the Flask application that utilizes build in Flask template engine. 
This should be the repository for images, CSS, JavaScript, Fonts or any other file an HTML page might need 
to include. 

`/flashproject/template/`

As with the above, if you're utilizing the Flask template engine, you need to place your templates in this 
directory.  When calling the templates with `render_template` the path looks for the templates directory as 
it's root when looking up templates.

##### Files

`__init__.py`

This is used to initially build the application objects.

`config.py`

This is used to initially build a default Configuration object.

`database.py`

This is used to build a non-contextual database object.  As you might have noticed in the `__init__.py` of 
the main application, the application is build using the `with app.app_content():` closure and context 
management syntax which allows us to more dynamically build the application.

`models.py`

This is used to build the applications data structure.  Review the `build.py` documentation above for more
information on how to use this or check out the SQLAlchemy documentation linked above.