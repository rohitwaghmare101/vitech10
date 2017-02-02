# Adding Field in inherit
in model form field
<field name="inherit_id" ref="todo_app.todo_task_form"/>

<xpath expr="//field[@name]='is_done'" position="before">
	<field name="date_deadline" />
</xpath>

#position
# - before , -replace  , -after


or with field

<field name="is_done" position="before">
	<field name="date_deadline"/>
</field>