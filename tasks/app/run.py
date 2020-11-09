# encoding: utf-8
# pylint: disable=too-many-arguments
"""
Application execution related tasks for Invoke.
"""

try:
    from importlib import reload
except ImportError:
    pass  # Python 2 has built-in reload() function
import os
import platform
import warnings

try:
    from invoke import ctask as task
except ImportError:  # Invoke 0.13 renamed ctask to task
    from invoke import task


@task(default=True)
def run(
        context,
        host='127.0.0.1',
        port=5000,
        flask_config=None,
        install_dependencies=False,
        with_gevent=False,
        uwsgi=False,
        uwsgi_mode='http',
        uwsgi_extra_options='',
    ):
    """
    Run py-ispyb Server.
    """
    if flask_config is not None:
        os.environ['FLASK_CONFIG'] = flask_config

    if install_dependencies:
        context.invoke_execute(context, 'app.dependencies.install')

    from app import create_app
    app = create_app()

    use_reloader = app.debug
    if uwsgi:
        uwsgi_args = [
            "uwsgi",
            "--need-app",
            "--manage-script-name",
            "--mount", "/=app:create_app()",
            "--%s-socket" % uwsgi_mode, "%s:%d" % (host, port),
        ]
        if use_reloader:
            uwsgi_args += ["--python-auto-reload", "2"]
        if uwsgi_extra_options:
            uwsgi_args += uwsgi_extra_options.split(' ')
        os.execvpe('uwsgi', uwsgi_args, os.environ)
    elif with_gevent:
        from gevent.pywsgi import WSGIServer
        http_server = WSGIServer((host, port), app)
        http_server.serve_forever()

    else:
        return app.run(host=host, port=port, use_reloader=use_reloader)
