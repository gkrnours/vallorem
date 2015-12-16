from wtforms.widgets import HTMLString, CheckboxInput, TextInput
from wtforms.fields import BooleanField, TextField

class ToggleInput(CheckboxInput):
    def __call__(self, field, **kwargs):
        checkbox = super(ToggleInput, self).__call__(field, **kwargs)
        label = '<label for="%s"></label>' % kwargs.get('id', field.id)
        return HTMLString('%s\n%s' % (checkbox, label))

class AutoFillInput(TextInput):
    def __call__(self, field, **kwargs):
        kwargs['list'] = "%s-data" % kwargs.get('id', field.id)
        widget = super(AutoFillInput, self).__call__(field, **kwargs)
        dl = ['<datalist id="%s-data">' % kwargs.get('id', field.id)]
        for val in field.iter_choices():
            dl.append('<option value="%s">' % val)
        dl.append('</datalist>')
        return HTMLString("%s\n%s" % (widget, ''.join(dl)))

class ToggleField(BooleanField):
    widget = ToggleInput()

class AutoFillField(TextField):
    widget = AutoFillInput()

    def __init__(self, choices=None, **kwargs):
        """Choice is an iterable containing simple value"""
        super(AutoFillField, self).__init__(**kwargs)
        self.choices = choices

    def iter_choices(self):
        for value in self.choices:
            yield value
