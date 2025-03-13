from wtforms import Form
from wtforms import StringField, PasswordField, EmailField, BooleanField, SubmitField, IntegerField, RadioField
from wtforms import validators

class UserForm(Form):
	matricula = IntegerField("Matricula",[
		validators.DataRequired(message="El campo es requerido")
	])
	nombre = StringField("Nombre",[
		validators.DataRequired(message="El campo es requerido")
	])
	apellido = StringField("Apellido",[
		validators.DataRequired(message="El campo es requerido")
	])
	correo = EmailField("Correo",[
		validators.DataRequired(message="El campo es requerido")
	])
	
class ZodiacoForms(Form):
	nombre = StringField("Nombre:",[
		validators.DataRequired(message="El campo es requerido"),
		validators.Length(min=4, max=50, message="Debe tener entre 2 y 50 caracteres")
	])
	apellido_paterno = StringField("Apellido Paterno:",[
		validators.DataRequired(message="El campo es requerido"),
		validators.Length(min=4, max=50, message="Debe tener entre 2 y 50 caracteres")
	])
	apellido_materno = StringField("Apellido Materno:",[
		validators.DataRequired(message="El campo es requerido"),
		validators.Length(min=4, max=50, message="Debe tener entre 2 y 50 caracteres"),
		validators.Length(min=2, max=50, message="Debe tener entre 2 y 50 caracteres")
	])
	dia = IntegerField("Dia",[
		validators.DataRequired(message="El campo es requerido"),
		validators.NumberRange(min=1, max=31, message="Debe ser un día válido (1-31)")
	])
	mes = IntegerField("Mes",[
		validators.DataRequired(message="El campo es requerido"),
		validators.NumberRange(min=1, max=12, message="Debe ser un mes válido (1-12)")
	])
	anio = IntegerField("Año",[
		validators.DataRequired(message="El campo es requerido"),
		validators.NumberRange(min=1, max=2025, message="Debe ser un año válido (1-2025)")
	])
	sexo = RadioField('Sexo', choices=[('masculino', 'Masculino'),('femenino', 'Femenino')], validators=[
		validators.DataRequired(message="Debes seleccionar una opción")
	])
	
	submit = SubmitField('Imprimir')