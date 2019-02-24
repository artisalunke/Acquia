.. include:: /common/global.rst

Additional environments for |acquia-product:ace|
================================================

You may want more environments than the development, staging, and
production environments that you get initially. For example, you might
want additional environments to support:

-  Testing integration with other systems
-  Providing separate environments for different developers or
   development teams, where your developers want to work on the server
   instead of locally
-  Performing load testing on a copy of your production hardware

Note for |acquia-product:ace| users

Additional environments can be created for |acquia-product:ace|
applications. If you are an |acquia-product:ace| customer and you want
to set up additional environments for an application, `contact Acquia
Support </support#contact>`__. Be sure to note the following:

-  If your application uses shared staging servers, you will need to pay
   an additional fee for each environment added.
-  If your application uses dedicated staging servers, you will not be
   charged for additional environments, but your servers may need to be
   upsized to accommodate the increased load or reduced resources per
   environment caused by the additional environments.

.. _extra:

Aliases for additional environments
-----------------------------------

By default, |acquia-product:ac| applications have three environments
with the aliases ``dev``, ``test``, and ``prod``. If you have an
|acquia-product:ace| application with more than three environments and
you need to determine what your environment names and aliases are, you
can do one of the following:

-  Look at the ``$HOME/.drush`` folder on your server. Files in that
   folder list the aliases for the environments.
-  Use the Drush Cloud ``ac-environment-list`` command. For example:

   .. code-block:: none

      drush @site.env ac-environment-list

-  Use the Cloud API |command|_. For example:

   .. code-block:: none

      curl -s -u user:pass https://cloudapi.acquia.com/v1/sites/mysite/envs.json


.. |command| replace:: ``GET /sites/:site/envs`` command
.. _command: https://cloudapi.acquia.com/#GET__sites__site_envs-instance_route
