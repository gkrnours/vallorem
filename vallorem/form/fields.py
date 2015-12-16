from wtforms.widgets import HTMLString, CheckboxInput
from wtforms.fields import BooleanField

class ToggleInput(CheckboxInput):
    def __call__(self, field, **kwargs):
        checkbox = super(ToggleInput, self).__call__(field, **kwargs)
        kwargs.setdefault('id', field.id)
        label = '<label for="%s"></label>' % kwargs['id']
        return HTMLString('%s\n%s' % (checkbox, label))

class ToggleField(BooleanField):
    widget = ToggleInput()
