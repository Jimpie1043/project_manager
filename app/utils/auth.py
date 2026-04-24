import functools

from flask import (
    g, redirect, url_for
)


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        
        return view(**kwargs)
    
    return wrapped_view


def admin_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.admin is False or g.user is None:
            return redirect(url_for('workspace.index'))
        
        return view(**kwargs)
    
    return wrapped_view