.. include:: /common/global.rst

SOAP web service adaptor
========================

The connection defines the web service end point and the constant query
parameters. Extensions to the resource string and additional query
parameters are added in the adaptor screen. The Web Service Adaptor
supports the web service methods defined in the SOAP Web Service
Definition (WSDL).

Creating the adaptor
--------------------

Create a **SOAP Web Service** adaptor, and when it appears for
configuration, in the **Method** list, be sure to click the method you
want to use. The displayed methods and arguments will depend on those
made available by the WSDL.

For example, a sample temperature conversion web service from the
WebServiceX.NET website provides a method called ``ConverTemp`` that
takes a temperature an input unit and an output unit. Selecting this
method allows a conversion from degrees Celsius to Fahrenheit.

|SOAP adaptor example|

All SOAP arguments can be parameterized in the usual fashion using
``%%paramName%%``. If parameter values are added or changed, be sure to
click **Save Arguments & Headers / Update Parameters**.

SOAP envelope headers as well as HTTP request headers can be added to
the call. It is also possible to override the endpoint URL rather than
using the one specified in the WSDL — which is not always correct.

.. |SOAP adaptor example| image:: https://cdn4.webdamdb.com/1280_Jh1E2u41Lm81.png?1527090355
   :width: 1280px
   :height: 802px
