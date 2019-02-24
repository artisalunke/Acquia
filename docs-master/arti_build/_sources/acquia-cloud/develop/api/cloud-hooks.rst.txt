.. include:: /common/global.rst

Automating with Cloud Hooks
===========================

The |acquia-product:ui| automates the most common tasks involved in
developing a Drupal application: deploying code from a version control
system, and migrating code, databases, and files across your
development, staging, and production environments. Cloud Hooks allow you
to automate other tasks as part of these migrations.

A Cloud Hook is a script in your code repository that
|acquia-product:ac| executes on your behalf when a triggering action
occurs. Examples of tasks that you can automate with Cloud Hooks
include:

-  Performing Drupal database updates each time you develop new code.
-  Scrubbing your production database each time you copy it to
   development or staging by removing customer emails or disabling
   production-only modules.
-  Running your test suite or an application performance test each time
   you deploy new code.

.. _install:

Installing Cloud Hooks
----------------------

Your Cloud Hooks are located in your |acquia-product:ac| code
repository. In each branch of your repo, there is a directory named
``docroot`` that contains your application's source code. Cloud Hooks
are in the ``hooks`` directory *next to* ``docroot`` (not inside of
``docroot``).

The Cloud Hooks directory structure, sample and community-contributed
hook scripts, and documentation can be found at
https://github.com/acquia/cloud-hooks. To start using Cloud Hooks with
your application, copy the current version of the Cloud Hooks repository
on GitHub into your |acquia-product:ac| repository.

Using Git, you can copy the Cloud Hooks repository with these commands:

``cd /my/repo curl -L -o hooks.tar.gz https://github.com/acquia/cloud-hooks/tarball/master  tar xzf hooks.tar.gz mv acquia-cloud-hooks-* hooks git add hooks git commit -m 'Import Cloud hooks directory and sample scripts.' git push``

.. _exec:

Cloud Hooks must be executable
------------------------------

To be able to run, hook scripts must have the Unix executable bit.
Although scripts with the executable bit set when first added to your
repository should be fine, run the following commands to set the
executable bit for files already in your Git repository:

``chmod a+x ./my-hook.sh git add ./my-hook.sh git commit -m 'Add executable bit to my-hook.sh' git push``

.. _quick:

Quick start
-----------

To see the power of Cloud Hooks in action, you can run the "Hello,
Cloud!" script when new code is deployed in your development
environment. Be sure to install Cloud Hooks first as previously
explained.

#. Install the ``hello-world.sh`` script to run on code deployments to
   development.

   Note

   This example assumes that your development environment is running the
   *master* branch.

   ``cd /my/repo git checkout master cp hooks/samples/hello-world.sh hooks/dev/post-code-deploy git commit -a 'Run the hello-world script on post-code-deploy to Dev.' git push``

#. Sign in to the `|acquia-product:ui| <https://cloud.acquia.com>`__ and
   select your application.
#. In the Dev environment code section, click the code switch button and
   select the *master* branch (if your Dev environment is already
   running **master**, select any other tag, and then select **master**
   again), and then click **Continue**. Click **Switch** to confirm the
   switch to the master branch.
#. View the task log. After the code deployment task is done, click its
   **Details** link to see the hook's output. It will look like this:

   ``Started Updating s1.dev to deploy master Deploying master on s1.dev [05:28:33] Starting hook: post-code-deploy Executing: /var/www/html/s1.dev/hooks/dev/post-code-deploy/hello-world.sh  s1 dev master master s1@svn-3.devcloud.hosting.acquia.com:s1.git git (as s1@srv-4) Hello, Cloud! [05:28:34] Finished hook: post-code-deploy``

You can use the code switch button on the **Environments** page to
restore your development environment back to whatever branch it
previously had deployed.

.. _ra:

Cloud Hooks and Remote Administration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have an |acquia-product:ace| application with a `Remote
Administration </ra>`__ (RA) environment, Cloud Hooks in the RA
environment may result in unexpected behaviors or task failures, which
can cause the RA automated update process to fail. For more information,
see `Remote Administration environment: Deploy
hooks </ra/environment#hooks>`__.

.. _more:

Going further with Cloud Hooks
------------------------------

Complete documentation for Cloud Hooks and the latest sample and
community-contributed hook scripts are available at
https://github.com/acquia/cloud-hooks. By browsing the GitHub repo, you
can do the following:

-  Find and use the latest sample and community-contributed hook
   scripts.
-  Read the complete documentation on how to write your own custom hook
   scripts.
-  Contribute your own hook scripts so that others can use them.

Check out these blog posts to see how some |acquia-product:ac| users
have taken advantage of the power of Cloud Hooks:

-  `10 Ways Acquia Cloud Hooks can help you sleep at
   night <http://i-kos.com/developing/blog/2014-01-14/10-ways-acquia-cloud-hooks-can-help-you-sleep-night>`__,
   by Richard Jones, Technical Director at i-KOS
-  `Using Cloud Hooks on Acquia Cloud
   Hosting <http://www.mediacurrent.com/blog/using-cloud-hooks-acquia-cloud-hosting>`__,
   by James Rutherford, Lead Drupal Architect at Mediacurrent
