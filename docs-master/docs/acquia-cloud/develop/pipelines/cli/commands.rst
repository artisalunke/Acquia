.. include:: /common/global.rst

Using the |acquia-product:ac| pipelines client
==============================================

.. container:: internal-navigation

   **Acquia Cloud pipelines client**

   * :doc:`Intro </acquia-cloud/develop/pipelines/cli>`
   * :doc:`Install </acquia-cloud/develop/pipelines/cli/install>`
   * :doc:`Connect </acquia-cloud/develop/pipelines/cli/github>`
   * :doc:`Require </acquia-cloud/develop/pipelines/cli/github/reqs>`
   * Commands
   * :doc:`Migrate </acquia-cloud/develop/pipelines/cli/github/migrate>`
   * :doc:`Workflows </acquia-cloud/develop/pipelines/cli/workflows>`

The |acquia-product:ac| pipelines client gives you access to a set of commands you can run to start, manage, and troubleshoot your continuous delivery pipeline jobs from the command line.

.. note::

   Installing the pipelines command-line client is optional, and not required for pipelines to function with your application.

Pipelines client commands
-------------------------

The pipelines client provides the following commands:

.. list-table::
 :widths: 25 25 50
 :header-rows: 1

 * - Command
   - Parameter
   - Description
 * - ``pipelines``
   - ``start``
   - Execute an pipelines job. `Learn more <#start>`__.
 * - ``pipelines``
   - ``configure``
   - Configure the client with the credentials required to authenticate with |acquia-product:ac|.
 * - ``pipelines``
   - ``encrypt``
   - Encrypt confidential data for use with |acquia-product:ac|. For more information, see `Encrypting keys and variables </acquia-cloud/develop/pipelines/encrypt>`__.
 * - ``pipelines``
   - ``github-connect``
   - Use a GitHub repository as the source repository, instead of your |acquia-product:ac| repository. For more information, see `Using GitHub with the pipelines client </acquia-cloud/develop/pipelines/cli/github>`__.
 * - ``pipelines``
   - ``github-disconnect``
   - Disconnect pipelines from a GitHub repository. For more information, see `Configuring the GitHub to pipelines connection </acquia-cloud/develop/pipelines/cli/github/connect#disconnect>`__.
 * - ``pipelines``
   - ``help``
   - Display help for a command.
 * - ``pipelines``
   - ``list``
   - List the available commands.
 * - ``pipelines``
   - ``list-applications``
   - List the application ID and other information about all of the |acquia-product:ac| applications that you have access to. `Learn more <#appids>`__.
 * - ``pipelines``
   - ``list-jobs``
   - Return a list of jobs for a given application ID, including the start time and duration of the jobs.
 * - ``pipelines``
   - ``logs``
   - Display the logs for a given application and job.
 * - ``pipelines``
   - ``self-update``
   - Check for a newer version of the pipelines client, and if found, update to the latest version.
 * - ``pipelines``
   - ``set-application-id``
   - Set the default application ID, for cases where you are not using an |acquia-product:ac| repository as a remote. `Learn more </acquia-cloud/develop/pipelines/cli/github#set-appid>`__.
 * - ``pipelines``
   - ``show-connection``
   - Verify the connection used to execute pipelines jobs.
 * - ``pipelines``
   - ``status``
   - Display the status of a pipelines job. `Learn more <#errors>`__.
 * - ``pipelines``
   - ``terminate-job``
   - Terminates a pipelines job. `Learn more </acquia-cloud/develop/pipelines/troubleshooting#kill>`__.
 * - ``pipelines-artifact``
   - ``start``
   - Start the upload of a artifact. Be sure to enter the artifact's custom name as a second parameter; otherwise, |acquia-product:ac| will expect a ``branch_name@commit_hash`` artifact name structure. (Used only with `Node.js applications </acquia-cloud/node-js/start>`__)
 * - ``pipelines-artifact``
   - ``upload``
   - Upload the artifact and provide notifications regarding its status. (Used only with `Node.js applications </acquia-cloud/node-js/start>`__)
 * - ``pipelines-artifact``
   - ``fail``
   - Notify with the failure status. (Used only with `Node.js applications </acquia-cloud/node-js/start>`__)

.. _help:

Help and troubleshooting
------------------------

Each of these commands is documented in the pipelines client help. To find the documentation for a command from the client, enter a command similar to the following:

.. code-block:: none

   pipelines help [command]

where ``[command]`` is the name of the command for which you want to obtain help.

If a command fails, re-running the command with the ``-x`` flag will enable debugging output, which may help you identify the cause of the error.

Using the start command
-----------------------

.. admonition:: Using pipelines with Node.js applications

   For information about using the ``pipelines-artifact`` command to access pipelines in your Node.js applications, see `Getting started with Node.js applications and environments </acquia-cloud/node-js/start>`__.

The command that does most of the work in the pipelines client is the ``start`` command, which has the following syntax:

.. code-block:: none

   pipelines start

Use the ``start`` command with a `build definition file </acquia-cloud/develop/pipelines/yaml>`__ to build your application. The ``start`` command accepts the following parameters:

.. list-table::
 :widths: 40 60
 :header-rows: 1

 * - Parameter
   - Description
 * - ``--application-id``
   - The |acquia-product:ac| application ID |br|
     See `Application IDs <#appids>`__ for more  information
 * - ``--format``, ``-f``
   - The output format — either``text`` (default) or ``json``
 * - ``--vcs-path``
   - The Git branch or tag that contains the build definition file for executing the build job
 * - ``--deploy-vcs-path``
   - The Git branch or tag to which the build artifact should be written. By default, this is the name of the branch that you built, with ``pipelines-build-`` prepended
 * - ``--source-vcs-uri``
   - The URI of a Git repository from which the source will be cloned. If present, the specified URI will be used instead of the |acquia-product:ac| code repository
 * - ``--source-key-path``
   - The path to an SSH private key file used to access an external code repository
 * - ``--environment-variable``, ``-D``
   - Specify one or more environment variables for this job, which are set for the duration of the job and can supplement or override `variables set in the build definition file </acquia-cloud/develop/pipelines/yaml#variables>`__ |br|
     For example: ``pipelines start -D [variable name 1]=[value] -D [another variable name]=[value]`` 
 * - ``--keep-process-alive``
   - Keeps the container process active for up to 60 minutes for debugging purposes
 * - ``--tail``
   - Tail your complete build logs
 * - ``--retries``
   - Number of retries (default: 50)
 * - ``--delay``
   - Number of seconds to wait between retries (default: 1)
 * - ``--help``, ``-h``
   - Display information about the ``start`` command's parameters
 * - ``--quiet``, ``-q``
   - Do not output any message
 * - ``--version``, ``-V``
   - Display this application version
 * - ``--ansi``
   - Force ANSI output
 * - ``--no-ansi``
   - Disable ANSI output
 * - ``--no-interaction``, ``-n``
   - Do not ask any interactive questions
 * - ``--verbose``, ``-v|vv|vvv``
   - Use this to output more verbose messages, which can help with debugging (1 for normal output, 2 for more verbose output and 3 for debug)

.. _appids:

Application IDs
---------------

Some pipelines client commands require an application ID, which corresponds to the |acquia-product:ac| application or website that you want to build against. The ``pipelines start`` command determines the application ID itself when you run it from within an |acquia-product:ac| Git repository clone. To run the ``start`` command from outside of an |acquia-product:ac| Git repository clone, use the ``--application-id`` argument. To find the application ID, run the following command:

.. code-block:: none

  pipelines list-applications

The response will include the application ID for each of your applications. If you have many applications, you can run ``list-applications`` through ``grep`` to filter for the name of the application you are looking for:

.. code-block:: none

  pipelines list-applications|grep my_app

You can also find the application ID in the |acquia-product:ui|. Sign in at `cloud.acquia.com <https://cloud.acquia.com>`__, and then click your subscription. The application ID is in the URL, which appears similar to the following:

.. code-block:: none

  https://cloud.acquia.com/app/develop/applications/12cc63dd-57db-4d50-6bc5-4b60d2198d14

In this example, ``12cc63dd-57db-4d50-6bc5-4b60d2198d14`` is the application ID.

.. _errors:

Viewing job status
------------------

You can view the output of a pipelines job using the ``status`` command. If a build job does not complete as expected, the ``status`` output will include descriptions of any errors. For example, you may get errors if your build definition file is malformed (contains missing elements or elements that cannot be parsed) or if it includes secure elements that cannot be decrypted. For more information, see the `pipelines feature troubleshooting guide </acquia-cloud/develop/pipelines/troubleshooting>`__.

The ``status`` command displays the results of the the most recent build job. You can optionally specify a different job, using the ``--job-id`` option. You can find the job ID in the output of the ``start`` command, or by running the ``list-jobs`` command.

If you are using the `pipelines_metadata </acquia-cloud/develop/pipelines/yaml#metadata>`__ element in your build definition file to set tracking variables for any purpose, adding the ``--format=json`` option to the status command will return the keys you set and their values.
