.. include:: /common/global.rst

Using Drush aliases
===================

|acquia-product:ac| defines
`Drush <https://www.drupal.org/project/drush>`__ aliases for all of your
application's environments. For example, the application named
(|acquia-product:ac| username) *example* has the following Drush aliases
for its Development, Staging, and Production environments:

-  example.dev
-  example.test
-  example.prod

Your environments might not all be on the same server, depending on your
account and configuration. Using Drush's remote command capability, you
can use any of the aliases to access any of your applications from your
local computer or any |acquia-product:ac| server. The remote aliases
work seamlessly if you have your SSH private key available on the source
server. To use your SSH private key from |acquia-product:ac| without
having to copy the private key to the |acquia-product:ac| server, use
`SSH key forwarding <#forward>`__ by using the ``-A`` argument to SSH
when connecting from your local computer.

For the following examples, the Staging environment is on server
``staging-1`` and your Production environment is on ``web-1``,
``web-2``, and ``web-3``.

.. note::

   If you have more than one subscription that uses the same name, your
   Drush aliases will use the same namespace and overwrite each other.

.. _download:

Downloading Drush aliases
-------------------------

Use the following method to download your Drush aliases:

#. Sign in to the |cloud-ui|
   using your email address and Acquia password.
#. Click your user avatar in the upper right corner, and then click
   **Edit profile**.

   |Edit your profile|

#. On the Profile page, click **Credentials**.

   |Profile Credentials page|

#. Under **Drush integration**, click **Download Drush aliases**

Extract the downloaded archive file into ``$HOME``:

``tar -C $HOME -xf $HOME/Downloads/example.tar.gz``

Use the aliases on your local command line as though you were signed in
to your |acquia-product:ac| server to view the Drush status. For
example:

``drush @example.test status``

.. note::
   Microsoft Windows users may need to edit their ``$PATH`` variable to use
   Drush properly. Options to resolve this issue include the following:

   -  Use |add| (which will install and configure Drush with the appropriate
      ``$PATH`` value)
   -  `Edit the path manually 
      <http://betanews.com/2015/11/23/windows-10-finally-adds-a-new-path-editor/>`__

Important

Do not add files from your ``.drush`` aliases directory to your
|acquia-product:ac| server's home directory. The Drush alias files
include a ``remote-host`` setting that enables them to function from
your local machine, but which can prevent SSH connections if it is
present on your |acquia-product:ac| servers.

.. _status:

Example: Viewing site status with Drush
---------------------------------------

To view the status of your application on the Production environment
from your local computer using Drush, enter the following command:

``drush @example.prod status``

.. note:: 

   Depending on the age of your subscription, there are two available
   formats for ``remote-host``. Be sure to examine your alias file to
   validate that one of the following correct formats is in use, when
   needed:

   -  ``[subscriptionname][env].ssh.prod.acquia-sites.com``
   -  ``serverrname-nnnn.prod.hosting.acquia.com``

.. _forward:

Viewing site status using Drush and SSH forwarding
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By signing in to an |acquia-product:ac| server with SSH forwarding, you
can access all of your environments without copying your private key to
|acquia-product:ac|. To view the Drush status for your Production
website while being signed in to the server for your Staging
environment, enter the following commands, replacing server names as
appropriate:

``ssh -A example.test@staging-1.prod.hosting.acquia.com  drush @example.prod status``

.. _refresh:

Refreshing Drush aliases
------------------------

From time to time, your Drush aliases may change. This can happen when
your server infrastructure (and therefore the hostname of your
|acquia-product:ac|) changes. That might happen if your server instance
is resized or relaunched, for example, or if you upgrade your
subscription from |acquia-product:acfs| to |acquia-product:acs|, or from
|acquia-product:acs| to |acquia-product:ace|.

You can refresh your Drush aliases by `downloading them <#download>`__
again, and pasting the new version over the old one. As an alternative,
you can use this Drush command:

``drush acquia-update``

.. _related:

Related topics
--------------

-  `Enabling SSH access </acquia-cloud/ssh/enable>`__
-  `About Drush on Acquia Cloud </acquia-cloud/drush>`__

.. |Edit your profile| image:: https://cdn3.webdamdb.com/md_ANJ4181Z1uE8.png?1526476118
   :width: 321px
   :height: 483px
.. |Profile Credentials page| image:: https://cdn4.webdamdb.com/md_M5MWwTjfhUA1.png?1526475789
   :width: 509px
   :height: 416px

.. |cloud-ui| replace:: \ |acquia-product:ui|\
.. _cloud-ui: https://cloud.acquia.com

.. |add| replace:: \ |acquia-product:add|\
.. _add: </dev-desktop>
