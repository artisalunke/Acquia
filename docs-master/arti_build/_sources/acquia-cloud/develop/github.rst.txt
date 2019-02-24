.. include:: /common/global.rst

Using |acquia-product:ac| with a remote repository
==================================================

If you use Git, you may want to host your Git repository at
`GitHub <https://github.com/>`__ or on
`Bitbucket <https://bitbucket.org/>`__ to take advantage of their
excellent Git support, pull requests with integrated code review, and
use other features. The following methods are available to keep your
application’s code in GitHub or Bitbucket while still hosting it on
|acquia-product:ac|:

-  The `|acquia-product:ac| pipelines feature </acquia-cloud/cd>`__,
   which provides integration with GitHub, Bitbucket, and the
   |acquia-product:ui|.
-  Manually creating two *remotes* for your local repository clone: one
   at GitHub or Bitbucket, and one at |acquia-product:ac|.

.. _github:

Using GitHub with |acquia-product:ac|
-------------------------------------

The first step is to create two remote repositories. Suppose you have an
existing repository at GitHub containing your application’s code. Use
the following commands to make a local clone:

``git clone git@github.com:me/mysite.git cd mysite git remote -v``

``origin  git@github.com:me/mysite.git (fetch) origin  git@github.com:me/mysite.git (push)``

GitHub is the *origin* remote, the default location for ``git push`` and
``git pull``.

To deploy this code to |acquia-product:ac|, add your |acquia-product:ac|
repository as an additional remote, named something short, like ``ac``,
and then do an initial ``git push --force ac`` to reinitialize the
|acquia-product:ac| repository. You can find the URL of your
|acquia-product:ac| repository in the |acquia-product:ui|, using
`**Application info** </acquia-cloud/develop/repository/git#basic>`__
panel.

``git remote add ac mysite@svn-18.devcloud.hosting.acquia.com:mysite.git git remote -v``

``origin  git@github.com:me/mysite.git (fetch) origin  git@github.com:me/mysite.git (push) ac  mysite@svn-18.devcloud.hosting.acquia.com:mysite.git (fetch) ac  mysite@svn-18.devcloud.hosting.acquia.com:mysite.git (push)``

``git push --force ac``

Now you have two remotes, ``origin`` (GitHub) and ``ac``
(|acquia-product:ac|).

Pushing changes
~~~~~~~~~~~~~~~

After you have set up your two remote repositories, keep them in sync by
pushing local changes to both GitHub and |acquia-product:ac|. You can
edit some files and push them to GitHub:

``vi somefile.php git add somefile.php git commit -m ‘edited somefile.php’ git push origin master``

You can also push the same changes to |acquia-product:ac|:

``git push ac master``

Your new code is now in both your GitHub and |acquia-product:ac|
repositories and is running on your |acquia-product:ac| application.

Synchronizing release tags
~~~~~~~~~~~~~~~~~~~~~~~~~~

Suppose that now you deploy your code on |acquia-product:ac| from the
Development environment (running the master branch) to Production. This
creates a new release tag in your |acquia-product:ac| repository that
shows you exactly what code you deployed that day. You do not have to
synchronize that release tag to GitHub, but you can:

``git pull ac``

``From svn-18.devcloud.hosting.acquia.com:mysite * [new tag]  2012-03-12 -> 2012-03-12``

``git push --tags``

Now your GitHub repository contains the same release tag as your
|acquia-product:ac| repository.

.. _gitsubtree:

Translating your root directory with git subtree
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is one other wrinkle you may need to address. |acquia-product:ac|
requires that you keep all of your Drupal application code in the
directory ``docroot`` in your repository. Your existing GitHub
repository may not be set up that way, and you may have a lot of commit
history in that repository that you want to preserve. To preserve your
GitHub repository's directory structure and commit history, you can use
``git subtree`` to translate your GitHub repository’s root directory
into an |acquia-product:ac| ``docroot`` directory.

.. _bitbucket:

Using BitBucket with |acquia-product:ac|
----------------------------------------

Here is how to make your |acquia-product:ac| code repository available
on Bitbucket as well:

#. Create an account on `bitbucket.org <https://bitbucket.org/>`__.
   Bitbucket offers unlimited private repositories for free for up to
   five users. During the account creation process, select the empty
   repository option and provide it with a name.
#. Once your account has been created and your empty repository is
   provisioned, add your SSH public key to Bitbucket under your account
   settings. You can either use an existing key or generate a new key
   pair just for Bitbucket.
#. On your Bitbucket repository overview page, under **Command line**,
   click **I have an existing project** and copy the remote URL, which
   should appear similar to the following:

   ``git@bitbucket.org:[username]/[repo].git``

#. On your local command line, navigate to your |acquia-product:ac|
   repository directory and run the following to add a new *remote*
   named ``bitbucket``. Of course, you'll need to replace the
   ``git@bitbucket`` location with the actual one you copied from your
   repository overview page; you can also name the new remote whatever
   you'd like:

   ``git remote add bitbucket git@bitbucket.org:[username]/[repo].git``

#. Push all of your code, including branches and tags, to your new
   Bitbucket remote repository:

   ``git push -u bitbucket --all``

   When prompted for a password, which is only necessary the first time
   you connect, enter your actual Bitbucket account password before you
   proceed with the push.

#. When you refresh your repository overview on Bitbucket, you should
   now see all of your code and commits.

If you want to keep your |acquia-product:ac| and Bitbucket repositories
in sync, create a new alias named ``all`` in the ``.git/config`` file in
your repository:

``[remote "all"]     url = [sitename]@svn-[number].prod.hosting.acquia.com:[sitename].git     url = git@bitbucket.org:[username]/[repo].git``

You can find the URL of your |acquia-product:ac| repository in the
|acquia-product:ui|', using the `**Application
info** </acquia-cloud/develop/repository/git#basic>`__ panel.

When you push new commits, use the ``all`` alias to push simultaneously
code to both |acquia-product:ac| and Bitbucket:

``git push all``

.. _jira:

Connecting to JIRA
------------------

JIRA is Atlassian's issue tracking and project management software. For
information about how to connect your remote Bitbucket or GitHub
repository to JIRA, see `Atlassian's
documentation <https://confluence.atlassian.com/display/JIRACLOUD/Linking+a+Bitbucket+or+GitHub+repository+with+JIRA>`__.

.. _related:

Related topics
--------------

-  `About your code repository </acquia-cloud/develop/repository>`__
-  `Using Git </acquia-cloud/develop/repository/git>`__
