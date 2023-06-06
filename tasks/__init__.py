"""
Invoke entrypoint, import here all the tasks we want to make available
"""
from __future__ import absolute_import, division, print_function
from invoke import Collection

from . import role

ns = Collection()

ns.add_collection(role)


ns.configure(
    {
        "run": {
            # this should stay, set the encoding explicitly so invoke doesn't
            # freak out if a command outputs unicode chars.
            "encoding": "utf-8",
        }
    }
)
