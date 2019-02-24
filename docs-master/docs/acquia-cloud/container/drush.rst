.. include:: /common/global.rst

Using different Drush versions in containers
============================================

Because |acquia-product:ac| containers support several versions of
Drush, |acquia-product:ac| provides a set of aliases that you can use to
access specific Drush major versions for your use.

To run a specific version of Drush, specify the major version in the
``drush`` command. For example:

-  *Drush 8* - ``drush8``
-  *Drush 7* - ``drush7``
-  *Drush 6* - ``drush6``

To run the default version of Drush, use the command ``drush`` (which in
|acquia-product:ac| containers is currently Drush 8).

Note for pipelines feature users

Acquia strongly recommends that you always run a specific major version
of Drush. Running the default version of Drush is dangerous because the
behavior of your build definition file may change unexpectedly when a
new version of Drush becomes the default.

.. _drush9:

Using Drush 9 with your container
---------------------------------

Drush 9 is not installed in your |acquia-product:ac|-supplied container.
If you want to use Drush 9 with your application, you must include it as
a requirement in your application's ``composer.json`` file.
