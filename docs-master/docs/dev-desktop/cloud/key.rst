.. include:: /common/global.rst

Acquia Cloud credentials and permissions
========================================

Communication with your |acquia-product:ac| server is protected with a
private/public key pair. In order to host an |acquia-product:add|
website on |acquia-product:ac|, you need to:

-  Generate an SSH private/public key pair (if you don't already have
   one). You can `use the |acquia-product:add| Preferences
   page </dev-desktop/keygen>`__ to generate your keys.
-  `Ensure that you have the correct permissions for your
   |acquia-product:ac| website <#permissions>`__.
-  `Register your public key with your |acquia-product:ac|
   website <#register>`__.
-  `Enter your private key in |acquia-product:add| <#enter>`__.

.. _register:

Registering your public key with |acquia-product:ac|
----------------------------------------------------

You can add a public key to your Acquia account on the **Profile >
Credentials** page. For more information, read `Adding a public key to
your server </acquia-cloud/ssh/enable/add-key>`__ and `Enabling SSH
access </acquia-cloud/ssh/enable>`__.

|acquia-product:ac| permissions
-------------------------------

To sync a website between |acquia-product:add| and |acquia-product:ac|,
you must have the correct permissions. Site group administrators, as
well as users with the default role Team Lead, have the necessary
permissions. A role needs the following permissions to support using
|acquia-product:add| with an |acquia-product:ac| website:

-  Access the Cloud API
-  Add SSH key to the Git repository
-  Add SSH key to non-Production environments
-  Add SSH key to the Production environment
-  Pull and deploy code, files, or databases to non-Production
   environments

You may want to create a custom role that includes these permissions, or
modify the Senior Developer role so that it includes these permissions.
Learn more about `Acquia teams, roles, and
permissions </acquia-cloud/teams>`__.

.. _enter:

Entering your private key in |acquia-product:add|
-------------------------------------------------

When you host a local |acquia-product:add| website on
|acquia-product:ac| or create a local clone of an |acquia-product:ac|
website for the first time, |acquia-product:add| prompts you for the
private key that corresponds to the public key registered on
|acquia-product:ac|. Click **Browse,** and select the location of your
private key. Then click **OK**.

|Enter private key file location|

Finding your private key
~~~~~~~~~~~~~~~~~~~~~~~~

By default, the location of your private key should be ``~/.ssh/id_dsa``
or ``~/.ssh/id_rsa``. If you can't either view or edit your private key
file using a text editor, use a command like the following to copy the
contents of the key file directly to the clipboard:

``pbcopy < ~/.ssh/id_dsa``

Changing your private key location
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can view and modify your private key location at any time in
|acquia-product:add| by completing the following steps:

#. Select an |acquia-product:ac| website.
#. In the right panel, click **Settings**.
#. Click **Browse**, and then select the new location of your private
   key.
#. Click **OK**.

Related topics
--------------

-  `Generating an SSH key </dev-desktop/keygen>`__
-  `Adding a public key to your
   server </acquia-cloud/ssh/enable/add-key>`__

.. |Enter private key file location| image:: https://cdn4.webdamdb.com/1280_oR9iRbH64Et3.png?1526475597
   :width: 590px
   :height: 148px
