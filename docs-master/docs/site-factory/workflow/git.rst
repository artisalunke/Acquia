.. include:: /common/global.rst

Accessing your |acquia-product:edg| repository
==============================================

.. toctree::
   :hidden:
   :glob:

   /site-factory/workflow/git/*

Before you begin to develop your websites on |acquia-product:edg|, you
must configure your Git repository. Until configured, you cannot access,
edit, or update your websites' codebases.

To prepare your environment for code development, you must first `add
your SSH key </acquia-cloud/ssh/enable/add-key>`__ to your
|acquia-product:ac| repository, and then `clone your code
repository <#clone>`__ for local work.

Note

For more information about Git, see the online version of *`Pro
Git <http://git-scm.com/book>`__* by Scott Chacon.

Adding your SSH key to your |acquia-product:ac| profile
-------------------------------------------------------

Without a SSH key added to your |acquia-product:ac| profile, you cannot
clone down your repository or perform other Git commands against it. For
a step-by-step description of adding your SSH key to your profile, see
`Adding a public key </acquia-cloud/ssh/enable/add-key>`__.

.. _clone:

Cloning your code repository
----------------------------

After you have added your SSH key to the |acquia-product:ac| interface,
you can clone your code from your |acquia-product:ac| Git repository to
your local computer. Your code repository contains a basic
|acquia-product:dgd|, along with its install files, profile, and
required and default modules.

Create a new folder to contain the code repository, and then run the
following command from the folder:

``git clone [Git_URL]``

where the ``[Git_URL]`` is your Git repository's URL.

Obtaining the Git URL
~~~~~~~~~~~~~~~~~~~~~

To obtain your Git repository's URL, complete the following steps:

#. `Sign in to |acquia-product:ac| </acquia-cloud/cloud-ui>`__.
#. Select your subscription, and then go to **Cloud > Workflow**.
#. Click **Git URL** to display a window that contains your
   subscription's Git URL.

   |Git URL button in the Cloud interface|

Next step
---------

Before beginning development on your new repository, you should review
`Best practices for Git on
|acquia-product:edg| </site-factory/workflow/git/practices>`__

.. |Git URL button in the Cloud interface| image:: https://cdn2.webdamdb.com/1280_M2AqZomGrB12.png?1526475788
   :width: 750px
   :height: 339px
