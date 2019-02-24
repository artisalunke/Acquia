.. include:: /common/global.rst

Working with sites on |acquia-product:ac|
=========================================

Once you have a website with versions both locally in
|acquia-product:add| and hosted in |acquia-product:ac| (which you can
accomplish either by exporting a local website into |acquia-product:ac|
or by creating a local clone of an |acquia-product:ac| website), you can
use |acquia-product:add| to develop the website locally, while
synchronizing the website continuously with the version on
|acquia-product:ac|. This helps you coordinate your local workflow in
|acquia-product:add| with your |acquia-product:ac| workflow.

Here's what a website looks like in |acquia-product:add| after you have
either imported from |acquia-product:ac| or exported it to
|acquia-product:ac|:

||acquia-product:ac| website in |acquia-product:add||

For information about the features displayed in this view, see `Working
with your sites </dev-desktop/sites>`__.

Use the **Local workflow** section to push or pull between the local
version of your website and the |acquia-product:ac| version. For more
information about what happens when you push or pull, see `How
|acquia-product:add| works with
|acquia-product:ac| </dev-desktop/cloud/details>`__.

.. _push:

Pushing to your |acquia-product:ac| Dev environment
---------------------------------------------------

As you develop your website locally, you can use |acquia-product:add| to
push your changes to the version of the website on |acquia-product:ac|:

#. Select **Push to Cloud Dev**.
#. Select which elements of your website you want to update: Code,
   Database, and Files.
   By default, **Clear cache** is selected, so that the caches in your
   |acquia-product:ac| Dev environment are cleared, and your changes
   will become visible faster.
#. Optionally, select **Run update.php** if you are adding or updating
   Drupal modules to your |acquia-product:ac| website.
#. Click **Push to Cloud Dev**. |acquia-product:add| pushes your changes
   to the Dev environment of your |acquia-product:ac| website.
#. You may be asked to enter your SSH key password, your name, and email
   address before your files will push. Enter the appropriate
   information when you are asked for it.

When you make a local copy of an |acquia-product:ac| website,
|acquia-product:add| makes a modification to the website's
``settings.php`` file. This modification ensures that your local website
connects to your local database, while your |acquia-product:ac| website
continues to connect to the |acquia-product:ac| database. When you push
your local code to |acquia-product:ac|, you need to commit this modified
``settings.php`` file so that both your local and |acquia-product:ac|
database connections continue to function.

For more information about pushing your local website to
|acquia-product:ac|, see `Committing local changes to
|acquia-product:ac| </dev-desktop/cloud/commit>`__. If you run into
problems, see `Troubleshooting: Problems syncing sites with
|acquia-product:ac| </dev-desktop/troubleshooting#sync>`__.

.. _pull:

Pulling from your |acquia-product:ac| website
---------------------------------------------

You can use |acquia-product:add| to pull the version of the website on
|acquia-product:ac| into your local |acquia-product:add| website. The
**Code** label specifies which tag or branch is currently deployed on
the |acquia-product:ac| environment you're pulling from. Your
|acquia-product:ac| website has a single code repository which is shared
by each of your environments. Each environment can have a different tag
or branch deployed.

#. Select **Pull from Cloud**.
#. Select which environment on your |acquia-product:ac| website you want
   to pull from (Dev, Stage, or Prod).
#. Select which elements of your website you want to update: Code,
   Database, and Files.
#. Optionally, select **Run update.php** if you are adding or updating
   Drupal modules to your local |acquia-product:add| website.
#. Click **Pull code from Cloud Dev**. |acquia-product:add| pulls your
   changes from your |acquia-product:ac| website.

.. _sync:

Which files get synced
----------------------

When you pull files from |acquia-product:ac| or push files to
|acquia-product:ac|, |acquia-product:add| syncs the files in these
folders under your [docroot]:

-  ``/files``
-  ``/sites/all/files``
-  ``/sites/default/files`` (if you have no multisites) or
   ``/sites/[current multisite]/files`` (if you have multisites)

Since files don't belong to the codebase, they aren't tracked in the
version control system (Git), and therefore aren't synced when you pull
or push code. They are synced using ``rsync`` when you pull or push
files.

.. _mismatch:

Branch differences between |acquia-product:ac| and your local code repository
-----------------------------------------------------------------------------

When you pull code from |acquia-product:ac| or push code to
|acquia-product:ac|, it is possible that your local code repository may
have a different branch checked out from the one that is currently
deployed on your |acquia-product:ac| Dev or Stage environment. For
example, you may have pulled code from |acquia-product:ac| and then
another team member may have deployed a new branch on that environment.

|acquia-product:add| can only push code changes when the
|acquia-product:ac| environment and your local code repository have the
same branch deployed. If you try to push code from |acquia-product:add|
to |acquia-product:ac| when the branches don't match, the push operation
will fail with an error message. To change the |acquia-product:ac|
branch:

#. Click the **|acquia-product:ac| Workflow** button in
   |acquia-product:add|.
#. Click the code select button on the application's **Environments**
   page.
#. Select the branch you have checked out to your local code repository.

If you try to pull code from an |acquia-product:ac| environment when
your local code repository already has a different branch checked out,
then:

-  If you have no uncommitted code changes in your local code
   repository, |acquia-product:add| asks if you want to overwrite your
   local code repository with the deployed branch from your
   |acquia-product:ac| environment.
-  If you do have uncommitted code changes in your local code
   repository, the pull operation is not permitted.

.. ||acquia-product:ac| website in |acquia-product:add|| image:: /sites/default/files/doc/2015/apr/dd2-cloned-https.png
   :width: 590px
   :height: 376px
