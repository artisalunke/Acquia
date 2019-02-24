.. include:: /common/global.rst

Configuring an environment
==========================

From the `Overview page of an
environment </acquia-cloud/manage/environments>`__, click **Configure**
to configure the environment.

|Click Configure or the gear icon to configure an environment|

In the **Configuration** panel, you can:

-  Select the PHP version for the environment.
-  `Modify PHP settings </acquia-cloud/manage/php>`__.
-  Enter the `Sendmail path <#sendmail>`__ for the application.
-  Enable or disable `Varnish over
   SSL </acquia-cloud/performance/varnish#ssl>`__.
-  Find your `New Relic account ID </acquia-cloud/monitor/apm>`__.

|Configuration overview screen|

.. _sendmail:

Configuring the Sendmail path
-----------------------------

You can configure the path used by Sendmail for email originating from
your application. For more information, see |aboutemail|_.


.. |aboutemail| replace:: About email in your \ |acquia-product:ac|\  environment
.. _aboutemail: /acquia-cloud/manage/email

.. |Click Configure or the gear icon to configure an environment| image:: https://cdn3.webdamdb.com/1280_sLlRRqa45z02.png?1526475944
   :width: 750px
   :height: 330px
.. |Configuration overview screen| image:: https://cdn2.webdamdb.com/1280_U2CE9HwsTuK4.png?1526475592
   :width: 542px
   :height: 782px
