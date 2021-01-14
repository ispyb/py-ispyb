from functools import wraps

import flask
import flask_marshmallow
from flask_restx import Namespace as OriginalNamespace
from flask_restx.utils import merge, unpack
from flask_restx._http import HTTPStatus
from webargs.flaskparser import parser as webargs_parser
from werkzeug import exceptions as http_exceptions

# from .model import Model, DefaultHTTPErrorSchema

from flask_restx.model import Model


class Namespace(OriginalNamespace):

    WEBARGS_PARSER = webargs_parser

    def _handle_api_doc(self, cls, doc):
        if doc is False:
            cls.__apidoc__ = False
            return
        # unshortcut_params_description(doc)
        # handle_deprecations(doc)
        # for key in 'get', 'post', 'put', 'delete', 'options', 'head', 'patch':
        # if key in doc:
        # if doc[key] is False:
        # continue
        # unshortcut_params_description(doc[key])
        # handle_deprecations(doc[key])
        # if 'expect' in doc[key] and not isinstance(doc[key]['expect'], (list, tuple)):
        ##            doc[key]['expect'] = [doc[key]['expect']]
        cls.__apidoc__ = merge(getattr(cls, "__apidoc__", {}), doc)

    def resolve_object(self, object_arg_name, resolver):
        """
        A helper decorator to resolve object instance from arguments (e.g. identity).

        Example:
        >>> @namespace.route('/<int:user_id>')
        ... class MyResource(Resource):
        ...    @namespace.resolve_object(
        ...        object_arg_name='user',
        ...        resolver=lambda kwargs: User.query.get_or_404(kwargs.pop('user_id'))
        ...    )
        ...    def get(self, user):
        ...        # user is a User instance here
        """

        def decorator(func_or_class):
            if isinstance(func_or_class, type):
                # Handle Resource classes decoration
                # pylint: disable=protected-access
                func_or_class._apply_decorator_to_methods(decorator)
                return func_or_class

            @wraps(func_or_class)
            def wrapper(*args, **kwargs):
                kwargs[object_arg_name] = resolver(kwargs)
                return func_or_class(*args, **kwargs)

            return wrapper

        return decorator

    def model(self, name=None, model=None, mask=None, **kwargs):
        """
        Model registration decorator.
        """
        if isinstance(
            model, (flask_marshmallow.Schema, flask_marshmallow.base_fields.FieldABC)
        ):
            if not name:
                name = model.__class__.__name__
            api_model = Model(name, model, mask=mask)
            api_model.__apidoc__ = kwargs
            return self.add_model(name, api_model)
        return super(Namespace, self).model(name=name, model=model, **kwargs)

    def parameters(self, parameters, locations=None):
        """
        Endpoint parameters registration decorator.
        """

        def decorator(func):
            if locations is None and parameters.many:
                _locations = ("json",)
            else:
                _locations = locations
            if _locations is not None:
                parameters.context["in"] = _locations

            return self.doc(params=parameters)(
                self.response(code=HTTPStatus.UNPROCESSABLE_ENTITY)(
                    self.WEBARGS_PARSER.use_args(parameters, locations=_locations)(func)
                )
            )

        return decorator

    def preflight_options_handler(self, func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if "Access-Control-Request-Method" in flask.request.headers:
                response = flask.Response(status=HTTPStatus.OK)
                response.headers["Access-Control-Allow-Methods"] = ", ".join(
                    self.methods
                )
                return response
            return func(self, *args, **kwargs)

        return wrapper

    def route(self, *args, **kwargs):
        base_wrapper = super(Namespace, self).route(*args, **kwargs)

        def wrapper(cls):
            if "OPTIONS" in cls.methods:
                cls.options = self.preflight_options_handler(
                    self.response(code=HTTPStatus.NO_CONTENT)(cls.options)
                )
            return base_wrapper(cls)

        return wrapper
