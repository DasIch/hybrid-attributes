Hybrid-Attributes Documentation
===============================

Hybrid-Attributes provides a :class:`~hybrid_attributes.hybrid_property` and a
:class:`~hybrid_attributes.hybrid_method` descriptor, which call the underlying
function both in a class and instance context::

   class SomeClass:
       @hybrid_property
       def spam(self):
           return 'spam'

       @hybrid_method
       def eggs(self):
           return 'eggs'


.. testsetup::

   from hybrid_attributes import hybrid_property, hybrid_method

   class SomeClass:
       @hybrid_property
       def spam(self):
           return 'spam'

       @hybrid_method
       def eggs(self):
           return 'eggs'

.. doctest::

   >>> SomeClass.spam
   'spam'
   >>> SomeClass.eggs()
   'eggs'
   >>> SomeClass().spam
   'spam'
   >>> SomeClass().eggs()
   'eggs'


Installation
------------

Hybrid-Attributes is available on the PyPI and can be installed with pip::

  pip install hybrid-attributes


API Reference
-------------

.. module:: hybrid_attributes

.. autoclass:: hybrid_property
   :members:

.. autoclass:: hybrid_method
   :members:


Additional Information
----------------------

.. toctree::

   license
