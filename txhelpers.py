def then(self, callback, *args, **kw):
    """
    Convenience method for adding a callback that will only be called
    with the given arguments and ignore any prior success result.

    See L{addCallbacks}.
    """
    return self.addCallbacks(lambda _: callback(*args, **kw))

#from txhelpers import then
#Deferred.then = then