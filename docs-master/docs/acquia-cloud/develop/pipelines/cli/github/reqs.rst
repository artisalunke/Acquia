.. include:: /common/global.rst

Obtaining required Github information
=====================================

.. container:: internal-navigation

  **Acquia Cloud pipelines client**

  * :doc:`Intro </acquia-cloud/develop/pipelines/cli>`
  * :doc:`Install </acquia-cloud/develop/pipelines/cli/install>`
  * :doc:`Connect </acquia-cloud/develop/pipelines/cli/github>`
  * Require
  * :doc:`Commands </acquia-cloud/develop/pipelines/cli/commands>`
  * :doc:`Migrate </acquia-cloud/develop/pipelines/cli/github/migrate>`
  * :doc:`Workflows </acquia-cloud/develop/pipelines/cli/workflows>`

|acquia-product:ac| pipelines client

-  `Intro </acquia-cloud/develop/pipelines/cli>`__
-  `Install </acquia-cloud/develop/pipelines/cli/install>`__
-  `Connect </acquia-cloud/develop/pipelines/cli/github>`__
-  Require
-  `Commands </acquia-cloud/develop/pipelines/cli/commands>`__
-  `Migrate </acquia-cloud/develop/pipelines/cli/github/migrate>`__
-  `Workflows </acquia-cloud/develop/pipelines/cli/workflows>`__

Use this page if you have questions about how to obtain the information
that the optional |acquia-product:ac| pipelines command-line client
requires from GitHub during the `connection configuration
process </acquia-cloud/develop/pipelines/cli/github/connect>`__. These
steps are not required to `connect through the user
interface </acquia-cloud/develop/pipelines/connect>`__.

.. _permissions:

Required GitHub permissions
---------------------------

To control the connection between a GitHub repository and the pipelines
client, the user running the ``pipelines github-connect`` or
``pipelines github-disconnect`` command must have the proper permissions
for the GitHub repository.

Git repositories can be owned by a user or an organization:

-  *For repositories owned by a user account,* the user must be the
   owner of the user account.
-  *For repositories owned by an organization,* the user must have the
   GitHub *Owner* role in the organization that owns it.

For more information, see `What are the different access
permissions? <https://help.github.com/articles/what-are-the-different-access-permissions/>`__
in the GitHub help.

.. _token:

Obtaining your GitHub personal access token
-------------------------------------------

To use ``pipelines github-connect`` or ``pipelines github-disconnect``,
you must supply a GitHub personal access token. To obtain your GitHub
personal access token, complete the following steps:

#. Sign in to your GitHub account.
#. Modify the settings for your GitHub profile by clicking your profile
   image in the upper right, and then click **Settings**.

   |Profile Settings option|

#. At the bottom of the left menu, in the **Developer settings**
   section, click the **Personal access tokens** link.

   |Person access tokens link|

#. On the `Personal access tokens <https://github.com/settings/tokens>`__ page, 
   click **Generate new token** at the top of the page.
#. In the **Token description** field, enter a description or name for
   your new token (such as ``Acquia Cloud``).
#. In the **Select scopes** section, select the **repo** check box.

   |Personal access token settings|

#. Scroll to the bottom of the page, and then click **Generate token**.

   |Generate token button|

The **Personal access tokens** page displays your new token, which is a
string similar to ``91a2b3c45d6f159ce524ac411e6d63b307e5ca93``. Because
you cannot display the token again in the GitHub interface, copy the
token and save it in a secure place.

You can then paste the token into the appropriate pipelines command.

.. note:: After creating the personal access token, the GitHub user no longer needs the *Owner* role on GitHub. Changing the user's permission levels once the token is created will have no effect on the token.

.. |Profile Settings option| image:: https://cdn3.webdamdb.com/1280_EM0jzQEvseE3.png?1526475761
   :alt: Profile Settings option
.. |Person access tokens link| image:: https://cdn4.webdamdb.com/1280_69IiPkRRBA51.png?1526475812
   :alt: Person access tokens link
.. |Personal access token settings| image:: https://cdn3.webdamdb.com/1280_7gxAsjPCz31.png?1526475671
   :alt: Personal access token settings
.. |Generate token button| image:: https://cdn3.webdamdb.com/1280_I85itrs0iJ34.png?1526475680
   :alt: Generate token button
