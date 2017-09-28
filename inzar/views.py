from itertools import cycle
from flask_admin.contrib.sqla import ModelView
import sqlalchemy
import flask_admin
from flask_admin.model import typefmt
from flask_admin.base import expose
from formatters import column_formatters
from converters import CustomAdminConverter
from flask_admin.contrib.sqla.tools import is_relationship
from flask_admin.contrib.sqla import form, filters as sqla_filters, tools
from flask_admin._compat import string_types, text_type


class EnhancedModelView(ModelView):
    can_view_details = True
    column_formatters = column_formatters
    create_modal = True
    edit_modal = True
    model_form_converter = CustomAdminConverter
    mainfilter = ""

    form_widget_args = {
        'created_at': {
            'readonly': True,
        },
        'updated_at': {
            'readonly': True,
        },
    }

    def get_filter_arg_helper(self, filter_name, filter_op='equals'):
        filters = self._filter_groups[filter_name].filters
        position = list(self._filter_groups.keys()).index(filter_name)

        for f in filters:
            if f['operation'] == filter_op:
                return 'flt%d_%d' % (position, f['index'])

    @expose('/edit/', methods=('GET', 'POST'))
    def edit_view(self):
        if self.mainfilter:
            filtered_objects = {}

            self._template_args['filtered_objects'] = filtered_objects
        return super().edit_view()

    @expose('/details/', methods=('GET',))
    def details_view(self):
        if self.mainfilter:
            filtered_objects = {}
            self._template_args['filtered_objects'] = filtered_objects
        return super().details_view()

