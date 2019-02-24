.. include:: /common/global.rst

Committing local changes to |acquia-product:ac|
===============================================

Using |acquia-product:add|, you can make changes to your local Drupal
website, and then push your changes to your website on
|acquia-product:ac|, as described in `Working with sites on
|acquia-product:ac| </dev-desktop/cloud/working>`__. This topic
describes the process in more detail.

When you use |acquia-product:add| to `push
code </dev-desktop/cloud/working#push>`__ to |acquia-product:ac|, a
dialog appears so you can review all your uncommitted changes. You can
optionally provide a commit message, and choose to ignore any of your
local changes. When you are ready, click **Commit** and your changes
will be committed. The title of the **Review uncommitted changes**
dialog shows the Git branch you are committing to, and the dialog lists
all of the directories and files in your local codebase that differ from
your |acquia-product:ac| repository. Remember that your
|acquia-product:ac| site has a single code repository which is shared by
each of your environments. Each environment can have a different tag or
branch deployed. You can't push local code changes if you have a tag
deployed in |acquia-product:ac|.

|Review uncommitted changes|

For each directory or file, the **Review uncommitted changes** dialog
displays:

-  The action that will be taken when you click **Commit**. You can
   change this action to ``Always ignore`` or ``Skip for now`` by
   selecting the item and clicking **Action**. For more information, see
   `Omitting files from code pushes <#omit>`__.
-  The local file or directory's Git status, which indicates the
   differences between your local copy and what is in your
   |acquia-product:ac| repository. Click on a row to view an explanation
   of the status. For more information, see `Git status
   codes <#status>`__.
-  The path of the file or directory within your docroot.

Before you click **Commit**, you can add a Commit message to identify
the changes you are pushing. This is optional, but recommended. Click
**Commit** to push all the changed files from your local codebase to
your |acquia-product:ac| repository. This pushes all files listed whose
action is marked ``Commit``.

|acquia-product:add| can only push code changes when the
|acquia-product:ac| environment and your local code repository have the
same branch (and not a tag) deployed. For more information, see `Branch
differences between |acquia-product:ac| and your local code
repository </dev-desktop/cloud/working#mismatch>`__.

When you sync your code, you may need to resolve merge conflicts in your
codebase. This is likely to happen if you have more than one developer
working in the same codebase, or if you are working both in
|acquia-product:add| and in |acquia-product:ac| Live Development mode.
For information about resolving merge conflicts, see `Resources for
learning Git <%5Bacquia-product:kb%5Darticles/resources-learning-git>`__
and `Git Immersion <http://gitimmersion.com/lab_28.html>`__.

.. _omit:

Omitting files from code pushes
-------------------------------

If you have changed files in your codebase that you do *not* want to
push to your |acquia-product:ac| repository, you can select those files,
click **Action**, and select **Skip for now** if you don't want to push
them now, but might in the future.

If you have added files in your local codebase and you know that you
will never want to push them to your |acquia-product:ac| repository, you
can select those files, click **Action**, and select **Always ignore**.
The next time you use |acquia-product:add| to push code to your
|acquia-product:ac| repository, those selected files will be ignored and
will not appear in the list of changed files.

|Skip or ignore changed files|

Then click **Commit** to make the changes to your |acquia-product:ac|
repository.

Note

For information on managing and moving your code between your
|acquia-product:ac| environments, see `Managing your
code </acquia-cloud/develop/code>`__.

Git status codes
----------------

The `status code displayed for each
file <https://www.kernel.org/pub/software/scm/git/docs/git-status.html>`__
shows you information about the state of the file in your local
codebase, compared to the state of the file in your |acquia-product:ac|
repository.

.. |Review uncommitted changes| image:: https://cdn2.webdamdb.com/1280_gQkjlNUvG0C0.png?1526476082
   :width: 590px
   :height: 310px
.. |Skip or ignore changed files| image:: https://cdn2.webdamdb.com/1280_ILfm3sWEAKM2.png?1526476195
   :width: 590px
   :height: 162px
