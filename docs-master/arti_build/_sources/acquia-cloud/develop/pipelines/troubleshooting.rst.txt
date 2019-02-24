.. include:: /common/global.rst

Troubleshooting pipelines feature issues
========================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/develop/pipelines/troubleshooting/*

Troubleshooting |acquia-product:ac| pipelines

-  Failures
-  `Errors </acquia-cloud/develop/pipelines/troubleshooting/errors>`__
-  `Logs </acquia-cloud/develop/pipelines/troubleshooting/logs>`__

This page describes some of the approaches you can take in determining
the causes of errors or other problems with the |acquia-product:ac|
pipelines feature. It includes the following sections:

-  `Script failures <#script>`__
-  `GitHub issues <#github>`__
-  `Key issues <#keys>`__
-  `Terminating a job <#kill>`__

Note

After you fix any detected issues with any pipeline jobs, run the
``start`` command again to restart the build.

.. _script:

Script failures
---------------

By default, the pipelines feature prepends build scripts with
``set -e``, which causes the script to exit immediately if any command
has a non-zero exit code. You can override this behavior by including
``set +e`` in your build script.

Be aware that if you use ``set +e``, the script does not fail when a
command fails. Because of this, the script must manage its own exit
strategy and exit codes.

.. _github:

GitHub issues
-------------

If you encounter an error `running
``pipelines init-github`` </acquia-cloud/develop/pipelines/cli/github#init>`__,
ensure that you can view the GitHub Webhooks page for the repository by
using the following procedure:

#. Sign in to GitHub.
#. Go to your repository, and then click **Settings**.
#. In the menu on the left side, click **Webhooks**.

If you cannot view the Webhooks page, you may not have the necessary
`permissions </acquia-cloud/develop/pipelines/cli/github>`__ in GitHub.
Contact your organization's GitHub administrator for access.

Another possible cause is that you may have used an incorrect GitHub
personal access token. In GitHub, you can revoke your old personal
access token, `create a new
one </acquia-cloud/develop/pipelines/cli/github/reqs#token>`__, and then
try again to run ``pipelines init-github``.

.. _keys:

Key issues
----------

If you cannot connect to external resources, such as GitHub, but your
GitHub permissions are correct, use the following procedure to test your
SSH key:

Note

In the following commands, replace ``[/path/to/key]`` with the full path
to your SSH key.

#. Determine if the encrypted file in your ``acquia-pipelines.yml`` file
   can access your GitHub repo with the following command:

   ``ssh -i [/path/to/key] -vvv git@github.com``

   The ``-vvv`` switch forces verbose output, which can indicate if
   GitHub accepted your SSH key.

#. Confirm if your SSH key requires a passphrase because it is
   encrypted. Although newer encrypted SSH keys are indistinguishable
   from non-encrypted keys, use the following command to test older SSH
   keys:

   ``head -n2 /path/to/key``

   After you execute the command, review its output, which will appear
   similar to the following:

   ``-----BEGIN RSA PRIVATE KEY----- Proc-Type: 4,ENCRYPTED``

.. _kill:

Terminating a job
-----------------

You can voluntarily terminate a job that is in progress. You might do
this if the job seems stuck and unable to complete on its own, or if you
realize there is a problem with the job that you need to fix. To
terminate a job, use the ``terminate-job`` command:

``pipelines terminate-job [job ID]``

The ``terminate-job`` command terminates the most recent job, if it has
not yet completed. It has an optional argument, which is the job ID,
which you can use if you want to terminate a job other than the most
recently started one. You can get the job ID from the
``pipelines status`` command or from the output of the
``pipelines start`` command.
