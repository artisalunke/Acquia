.. include:: /common/global.rst

Installing the pipelines client
===============================

.. container:: internal-navigation

   **Acquia Cloud pipelines client**

   * :doc:`Intro </acquia-cloud/develop/pipelines/cli>`
   * Install
   * :doc:`Connect </acquia-cloud/develop/pipelines/cli/github>`
   * :doc:`Require </acquia-cloud/develop/pipelines/cli/github/reqs>`
   * :doc:`Commands </acquia-cloud/develop/pipelines/cli/commands>`
   * :doc:`Migrate </acquia-cloud/develop/pipelines/cli/github/migrate>`
   * :doc:`Workflows </acquia-cloud/develop/pipelines/cli/workflows>`

This page describes how to download and install the pipelines client,
and how to update a previously installed client. The client is installed
locally to perform pipelines jobs, which are carried out by
|acquia-product:ac|.

.. note::

   Installing the pipelines command-line client is optional, and not required for pipelines to function with your application.

Requirements
------------

To use the pipelines client, you must have one of the following versions
of PHP available in your local work environment:

-  PHP 5.6
-  PHP 7.1

Permission
----------

To use the pipelines client, you must have the **Execute pipelines**
permission for the |acquia-product:ac| application that you're working
with. By default, users who have been assigned the *Team lead* role have
this permission, while users with the *Senior Developer* or *Developer*
role do not.

An organization's Administrator can create new roles that have these
permissions, or modify existing roles to add these permissions. For more
information, see `Setting the Execute pipelines permission using the
Acquia Cloud interface </acquia-cloud/teams/permissions>`__. For
more general information about permissions in |acquia-product:ac|, see
`Working with roles and permissions </acquia-cloud/teams/roles>`__.

Installing with |acquia-product:add|
------------------------------------

The pipelines client is included with
|add|_ (2016-07-28 release or later), which is Acquia's free application that 
allows you to run and develop Drupal websites locally on your computer. Download
|acquia-product:add| from the `Acquia downloads page <http://dev.acquia.com/downloads>`__,
then open and run the installer. For full installation instructions, see
|install-add|_.

After you install |acquia-product:add|, close and then reopen your
command prompt window or shell sessions to ensure that the pipelines
client directory (``/Applications/DevDesktop/tools``) is in your
``PATH``.

.. _cli:

Installing from the command prompt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also install the pipelines client from the command prompt by
using the following commands:

.. code-block::

   curl -o pipelines https://cloud.acquia.com/pipeline-client/download 
   chmod a+x pipelines

Move the ``pipelines`` program to a directory in your ``PATH``. If you
are not familiar with how to make the pipelines client executable in
your ``PATH``, we recommend using the |acquia-product:add| installer.

.. _authenticate:

Configuring the client (authentication)
---------------------------------------

After you have installed the pipelines client, you must configure the
client with an |acquia-product:ac| API token. This enables the client to
authenticate with |acquia-product:ac|. You can obtain the
|acquia-product:ac| API token from the |acquia-product:ui| by completing
the following steps:

#. Sign in to the |cloud-ui|_.
#. Click the avatar in the upper right to open your profile, and then
   click **API tokens** in the left sidebar. Or, go directly to
   `cloud.acquia.com/app/profile/tokens <https://cloud.acquia.com/app/profile/tokens>`__.
#. Click the **Create Token** button to add an API token:

   |Create Token button|

#. In the **Create API Token** dialog box, enter a label for the token,
   such as ``Pipelines CLI Client``. A token label can help you identify
   your tokens if you create more than one.
#. Click **Create Token**. The **Create API Token** dialog displays the
   API key and the API secret that make up the token. You can view the
   API key at any time in the |acquia-product:ui|.

   .. important::

    *Do not close the dialog box until you record the API secret.*
    Because you *cannot* display the API secret at a later time, be sure
    to configure the pipelines client with the API secret before you
    close the dialog box.

    If you lose the API secret, you must create another API token.

#. In a separate command prompt window, run the following command:

   ``pipelines configure``

#. Copy and paste the API key and API secret you previously obtained in
   this procedure to the ``pipelines configure`` command prompts.

You can now use the pipelines client with your codebase. Your credentials are 
stored at ``~/.acquia/pipelines/credentials``.

.. _update:

Updating the pipelines client
-----------------------------

If you have already installed the pipelines client, run the
``pipelines self-update`` command to update your client to the latest
available version. You can use the command ``pipelines --version`` to
display your current version number.

.. |Create Token button| image:: https://cdn4.webdamdb.com/1280_wDmTqEC90m21.png?1527195222
   :alt: Create token button

.. |add| replace:: \ |acquia-product:add|\
.. _add: /dev-desktop

.. |install-add| replace:: \ |acquia-product:add|\
.. _install-add: /dev-desktop/install

.. |cloud-ui| replace:: \ |acquia-product:ui|\
.. _cloud-ui: https://cloud.acquia.com
