.. include:: /common/global.rst

Set node
========

|Set node|

Use a Set node as a shortcut for copying a value from one data location
to another. Set nodes can copy data from the schema, public variables,
or literal values, and then transmit that data to the schema or public
variables.

If the value is copied successfully, the Set node will return ``true``;
it will not return the value of the variable that was copied.

Set nodes support the following sources and destinations:

 

To

 

Schema

Public Variable

Literal

From

Schema

|yes|

|yes|

|no|

Public Variable

|yes|

|yes|

|no|

Literal

|yes|

|yes|

|no|

.. |Set node| image:: https://cdn4.webdamdb.com/1280_E8csjf05tZS8.png?1526475556
   :class: no-sb float-left logo-sm-lift
   :width: 51px
