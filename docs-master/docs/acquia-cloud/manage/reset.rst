.. include:: /common/global.rst

Starting over with an |acquia-product:ac| subscription
======================================================

Although websites on |acquia-product:ac| cannot be deleted by users, it
is possible to remove the website's data and start over from scratch.
Use the information on this page to help you find the resources you can
use to reset a previously created and developed website.

.. important:: 

   If you delete your website's data and then need to recover it, Acquia
   can provide only *extremely* limited support, if any at all. Do *not*
   follow these suggestions unless you are completely confident that you
   want to remove your website. If you are not sure, `contact Acquia
   Support </support#contact>`__.

.. _add:

Removing your local |acquia-product:add| site
---------------------------------------------

Some users may develop their websites using |acquia-product:add|. If you
no longer need to keep your data locally, you can `delete the local
site </dev-desktop/sites/delete>`__.

If you delete a website in |acquia-product:add| that is hosted on
|acquia-product:ac|, this process will delete only the local version of
the website, and does not affect the website on |acquia-product:ac|.

.. _clean-git:

Resetting the Git repository
----------------------------

For an explanation of how to delete the Git repository for a website and
remove all of its the code and history, see |resetrepo|_.

.. |resetrepo| replace:: Reset a Git repository on \ |acquia-product:ac|\ 
.. _resetrepo: /articles/reset-git-repository-acquia-cloud

.. _cleanup:

Deleting files and databases
----------------------------

After you determine that you no longer require your website's files, you
can `rsync the
files <%5Bacquia-product:kb%5Darticles/rsyncing-files-acquia-cloud>`__
to another location before deleting them from the directories, if
needed. After you have copies of any required files from your website,
you can `delete the website
files <%5Bacquia-product:kb%5Darticles/using-external-storage-files#cleanup>`__
if you do not plan to use them again.

For instructions about how to delete a database, see `Deleting a
database </acquia-cloud/manage/database#delete>`__.
