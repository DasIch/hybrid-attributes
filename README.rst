Hybrid-Attributes
=================

.. image:: https://travis-ci.org/DasIch/hybrid-attributes.svg?branch=master
   :target: https://travis-ci.org/DasIch/hybrid-attributes
   :alt: Travis CI Status

.. image:: https://codecov.io/gh/DasIch/hybrid-attributes/coverage.svg
   :target: https://codecov.io/gh/DasIch/hybrid-attributes
   :alt: Codecov Status

.. image:: https://readthedocs.org/projects/hybrid-attributes/badge/?version=latest
   :target: http://hybrid-attributes.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation

Hybrid-Attributes implements a `hybrid_property` and `hybrid_method`
descriptor, which call the underlying function both in a class and instance
context.

Assume you have a class like::

  class Foo:
      @classmethod
      def spam(self):
          return 'spam'

      @property
      def eggs(self):
          return 'eggs'

      def ham(self):
          return 'ham'

You can get the values returned by calling `.spam()` on the class, accessing
'.eggs' or calling `.ham()` on an instance:

>>> Foo.spam()
'spam'
>>> foo = Foo()
>>> foo.eggs
'eggs'
>>> foo.ham()
'ham'

If you access these in a different context, `.spam()` will still be
called with the class as first argument, `.eggs` will return a property object
only useful for introspection and `.ham()` will raise an exception because
there is no instance for it to be called with.

Hybrid-Attributes are different. They don't care about the object are accessed
through, the underlying function will always be called with whatever object
it's being accessed on. As an example, take this class::

  class HybridFoo:
      @hybrid_property
      def spam(self):
          return 'spam'

      @hybrid_method
      def eggs(self):
          return 'eggs'

You can access the property and call the method on the class or on an instance:

>>> Foo.spam
'spam'
>>> Foo.eggs()
'eggs'
>>> foo = Foo()
>>> foo.spam
'spam'
>>> foo.eggs

Hybrid-Attributes is BSD licensed and available for Python 3.4 and later.
