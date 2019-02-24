.. include:: /common/global.rst

Managing your pipelines from the command line
=============================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/develop/pipelines/cli/*

.. container:: internal-navigation

   **Acquia Cloud pipelines client**

   * Intro
   * :doc:`Install </acquia-cloud/develop/pipelines/cli/install>`
   * :doc:`Connect </acquia-cloud/develop/pipelines/cli/github>`
   * :doc:`Require </acquia-cloud/develop/pipelines/cli/github/reqs>`
   * :doc:`Commands </acquia-cloud/develop/pipelines/cli/commands>`
   * :doc:`Migrate </acquia-cloud/develop/pipelines/cli/github/migrate>`
   * :doc:`Workflows </acquia-cloud/develop/pipelines/cli/workflows>`

In addition to the `Pipelinespage </acquia-cloud/develop/pipelines/ui>`__ in the 
|acquia-product:ac| interface, you can also manage your pipelines by using a 
pipelines client from the command line.

.. note:

    -  The command-line client does not support Bitbucket at this time.
    -  Installing this command-line client is optional, and not required for
       pipelines to function with your application.

Getting started
---------------

To manage pipelines from the command line, you must first `install and
configure the pipelines command-line
client </acquia-cloud/develop/pipelines/cli/install>`__. For
convenience, the client is included with |acquia-product:add|.

For information about the available commands for the pipelines client,
see `Using the Acquia Cloud pipelines
client </acquia-cloud/develop/pipelines/cli/commands>`__. For Node.js
application-specific commands and syntax, see `Getting started with
Node.js applications and environments </acquia-cloud/node-js/start>`__.

Connecting to GitHub from the command line
------------------------------------------

After you have installed the command-line client, you must connect it to
your GitHub account. To do so, use the procedures described on the
`Configuring the GitHub to pipelines client
connection </acquia-cloud/develop/pipelines/cli/github/connect>`__
documentation page.

Optionally, you can also `migrate your code repository from
Acquia Cloud to
GitHub </acquia-cloud/develop/pipelines/cli/github/migrate>`__.

.. note::

   These steps are not required when connecting using the |acquia-product:ac| pipelines user interface.

.. _logs:

Logging and debugging
---------------------

You can review the results of each job with the ``pipelines status`` and
``logs`` commands. For a full list of commands available to you, see
`Using the Acquia Cloud pipelines
client </acquia-cloud/develop/pipelines/cli/commands>`__ for more
information.

Answers to common problems can be found in the `pipelines
troubleshooting
guide </acquia-cloud/develop/pipelines/troubleshooting>`__. Additional
help for each command is also available from the command line; see `Help
and
troubleshooting </acquia-cloud/develop/pipelines/cli/commands#help>`__
for more information.

.. _tutorial:

Tutorials and examples
----------------------

In addition to this product documentation, you can learn more about how
to use pipelines in the `tutorials and example
code <https://github.com/acquia/pipelines-examples>`__ at GitHub.
