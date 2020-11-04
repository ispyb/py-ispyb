# encoding: utf-8
"""
Application related tasks for Invoke.
"""

from invoke import Collection

from . import dependencies, env, run, swagger

from config import BaseConfig

namespace = Collection(
    dependencies,
    env,
    run,
    swagger,
)

namespace.configure({
    'app': {
        'static_root': BaseConfig.STATIC_ROOT,
    }
})
