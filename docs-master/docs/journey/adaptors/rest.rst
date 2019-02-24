.. include:: /common/global.rst

REST web service adaptor
========================

.. toctree::
   :hidden:
   :glob:

   /journey/adaptors/rest/*

The connection defines the web service end point and the constant query
parameters. Extensions to the resource string and additional query
parameters are added in the adaptor screen.

.. _create:

Creating the adaptor
--------------------

Create a **REST Web Service** adaptor, and when it appears for
configuration, in the **Method** list, be sure to click the appropriate
method from the following options:

-  `GET </journey/adaptors/rest/get>`__
-  `POST </journey/adaptors/rest/post>`__
-  `PUT </journey/adaptors/rest/put>`__
-  `DELETE </journey/adaptors/rest/delete>`__

For information about creating or configuring adaptors, see |adaptors|_.

.. |adaptors| replace:: \ |acquia-product:aj| \ adaptors
.. _adaptors: /journey/adaptors

The **Request String** field can now be edited to extend the complete
URL by adding new resources or query parameters. To extend the URL just
type the new resource or a parameter and the **Final Full Request URL**
will update to display the full web service call.

For example, the following actions will occur when entering values into
the **Request String** field:

-  ``/end/point`` - Extends the URL to include the resource
   ``/end/point``
-  ``/%%resource%%`` - Extends the URL to include a resource that will
   be populated from a dynamic value
-  ``?newparam=456`` - Extends the URL to include a new query parameter
   with a constant value include the question mark in the Request String
-  ``?newparam=%%newParamVal%%`` - Extends the URL to include a new
   query parameter that will be populated from a dynamic value
-  ``/end/point/%%endPoint%%?qp2=hello&qp3=%%qp3Val%%`` - Extends the
   URL with a combination of the previously described options

Whenever a parameter is used in the **Request String** field, be sure to
click **Save Request / Update Parameter** to update the parameters.

.. _warnings:

Validation Warnings
-------------------

+-----------------------------------+-----------------------------------+
| Warning                           | Description                       |
+===================================+===================================+
| **Invalid Adaptor                 | The Output destination has not    |
| Adaptor connection is not         | been set.                         |
| complete                          |                                   |
| Missing data destination/output** |                                   |
+-----------------------------------+-----------------------------------+
