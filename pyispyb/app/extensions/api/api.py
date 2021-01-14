"""
Project: py-ispyb
https://github.com/ispyb/py-ispyb

This file is part of py-ispyb software.

py-ispyb is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

py-ispyb is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.
"""


__license__ = "LGPLv3+"


from six import iteritems

from flask_restx import Api as BaseApi

from .namespace import Namespace


class Api(BaseApi):
    """
    Having app-specific handlers here.
    """

    def namespace(self, *args, **kwargs):
        # The only purpose of this method is to pass custom Namespace class
        _namespace = Namespace(*args, **kwargs)
        self.namespaces.append(_namespace)
        return _namespace

    def add_oauth_scope(self, scope_name, scope_description):
        for authorization_settings in self.authorizations.values():
            if authorization_settings["type"].startswith("oauth"):
                assert scope_name not in authorization_settings["scopes"], (
                    "OAuth scope %s already exists" % scope_name
                )
                authorization_settings["scopes"][scope_name] = scope_description

    def add_namespace(self, ns, path=None):
        # Rewrite security rules for OAuth scopes since Namespaces don't have
        # enough information about authorization methods.
        for resource, _, _ in ns.resources:
            for method in resource.methods:
                method_func = getattr(resource, method.lower())

                if (
                    hasattr(method_func, "__apidoc__")
                    and "security" in method_func.__apidoc__
                    and "__oauth__" in method_func.__apidoc__["security"]
                ):
                    oauth_scopes = method_func.__apidoc__["security"]["__oauth__"][
                        "scopes"
                    ]
                    method_func.__apidoc__["security"] = {
                        auth_name: oauth_scopes
                        for auth_name, auth_settings in iteritems(self.authorizations)
                        if auth_settings["type"].startswith("oauth")
                    }

        super(Api, self).add_namespace(ns, path=path)
