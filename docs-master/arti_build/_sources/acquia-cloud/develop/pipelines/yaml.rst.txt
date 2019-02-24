.. include:: /common/global.rst

Creating and managing your build definition file
================================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/develop/pipelines/yaml/*

An important element of the pipelines feature is the build definition file. This is a YAML format file (named ``acquia-pipelines.yml``) that you create in your workspace. The build definition file contains all of the information that is required to perform the build, including any variables that are required and the instructions used to perform the build. The components of the build process can be broken into individual steps in the build definition file, and each step will be executed in order. Each step corresponds to the keys at the top level in the ``steps`` section of the build definition file.

.. admonition:: Note for pipelines feature usage with Node.js applications

   An example of build definition file syntax suitable for use with Node.js is available at `Getting started with Node.js applications and environments </acquia-cloud/node-js/start>`__.

Pipeline builds will time out after 60 minutes. Unless all steps and processes used during the build are closed before the timeout, the build job will fail.

.. _toplevel:

Build definition file structure
-------------------------------

The build definition file must be named ``acquia-pipelines.yml`` and must exist in the root directory in the branch you wish to build.

The file will have the following approximate key/value structure. Click a key for additional information.

* `version: <#version>`__
* `variables: <#variables>`__
* `cde-databases: <#cde-databases>`__
* `services: <#services>`__
* `events: <#events>`__
     - `build: <#build>`__
         * `steps: <#steps>`__
     - `fail-on-build: <#fail>`__
         * steps:
     - `pr-merged: <#pr-merged>`__
     - `pr-closed: <#pr-closed>`__
* `ssh-keys: <#ssh-keys>`__

You can also use the ``pipelines_metadata`` key in any of the previously mentioned sections of your build definition file to send build or container information back for your use. `Learn more <#metadata>`__.

.. _version:

version key
~~~~~~~~~~~

This *required* key must have a value of at least ``1.0.0`` for use with the pipelines feature.

To use PHP 7, you must use ``1.1.0`` for the version key value. For more information about using PHP 7 in your build definition file, see the `services: php <#php7>`__ section on this page.

.. _variables:

variables key
~~~~~~~~~~~~~

The ``variables`` key of the build definition file provides a means of setting environment variables that are needed for your build. The environment variables are defined for all commands run during the job.

Here is a simple example of the ``variables`` key:

.. code-block:: none

      variables:
        global:
          ADMIN_USERNAME: admin
          ADMIN_PASSWORD:
            secure: 2aciWcRBNXrG/KcWG1bb0uSRTOVoiDl+h+QRi$. . .

For details about including secure (encrypted) variables in the variables key, see `Encrypting keys and variables </acquia-cloud/develop/pipelines/encrypt>`__ .

.. _defaultenvars:

Default environment variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following environment variables are set by the system:

.. list-table::
 :widths: 40 60
 :header-rows: 1

 * - Variable name
   - Description
 * - ``CI``, ``CONTINUOUS_INTEGRATION``
   - With a value of ``true``, indicates that this job is being run in a continuous integration context, rather than initiated directly by a human.
 * - ``PIPELINE_APPLICATION_ID``
   - The application ID for this job's pipeline.
 * - ``PIPELINE_CLOUD_REALM``
   - The |acquia-product:ac| realm, which is a prefix to the application name or site name for |acquia-product:ac| API purposes. For |acquia-product:ace| applications, this is ``prod``.
 * - ``PIPELINE_CLOUD_SITE``
   - The |acquia-product:ac| application name or site name that corresponds to the application ID.
 * - ``PIPELINE_DEPLOY_VCS_PATH``
   - The branch or tag that will hold the output of the job.
 * - ``PIPELINE_ENV``
   - With a value of ``true``, indicates that this job is being run in a pipeline context.
 * - ``PIPELINE_GIT_HEAD_REF``
   - A reference to the last commit in the Git repository.
 * - ``PIPELINE_JOB_ID``
   - The job ID for this job.
 * - ``PIPELINE_STATUS``
   - With a value of ``running``, indicates that this job is running in a pipeline context.
 * - ``PIPELINE_VCS_PATH``
   - The path of the branch specified in the ``--vcs-path`` argument of the ``start`` command.

cde-databases
~~~~~~~~~~~~~

This key enables you to specify which database schemas in a multisite configuration will be used to build this application. You can select a maximum of three databases.

.. code-block:: none

      cde-databases:
        - my-first-database
        - my-second-database

This definition has one of the following results, depending on its
settings:

+-----------------------------------+-----------------------------------+
| Definition value                  | Result                            |
+===================================+===================================+
| undefined/empty                   | All of the databases that are     |
|                                   | available for the application     |
|                                   | will be deployed to the           |
|                                   | environment                       |
+-----------------------------------+-----------------------------------+
| null ``(~)``                      | All of the databases that are     |
|                                   | available on the application will |
|                                   | be deployed to the environment    |
+-----------------------------------+-----------------------------------+
| array                             | Only the specified databases will |
|                                   | be included in the environment    |
|                                   | created by the job                |
+-----------------------------------+-----------------------------------+
| database name not defined on the  | The job will fail                 |
| application                       |                                   |
+-----------------------------------+-----------------------------------+
| any other value                   | The job will display an error     |
|                                   | message                           |
+-----------------------------------+-----------------------------------+

.. _services:

services key
~~~~~~~~~~~~

The ``services`` key allows you to enable one or more services to be
available during the execution of your pipelines job.

.. _mysql:

services: mysql
^^^^^^^^^^^^^^^

If your build process requires the use of MySQL, be sure to include the
``services: mysql`` key in your build definition file.

The ``mysql`` service starts a MySQL database server on 127.0.0.1 port
3306 for the duration of the job. This database is configured with only
one user configured, which has the username ``root`` and the password
``root``.

.. note::

  You must use the ``services: mysql`` key to start MySQL in your build definition file. The |acquia-product:ac| pipelines feature does not support ``sudo mysql`` commands.

.. _php7:

services: php
^^^^^^^^^^^^^

If your build process requires PHP 7, be sure to both `set your version key to 1.1.0 <#version>`__ and include the ``services: php`` key in your build definition file. For a ``services: php`` example, see the following:

.. code-block:: none

      services:
        - php:
            version: 7.1

.. _events:

events key
~~~~~~~~~~

The *required* ``events`` key is the parent of the following keys:

+-----------------------+-----------------------+-----------------------+
| Key                   | Required              | Description           |
+=======================+=======================+=======================+
| ```build`` <#build>`_ | Yes                   | Describes how the     |
| _                     |                       | workspace will be     |
|                       |                       | built                 |
+-----------------------+-----------------------+-----------------------+
| ```pr-merged`` <#pr-m | No                    | Steps taken if a pull |
| erged>`__             |                       | request is merged to  |
|                       |                       | its base branch       |
+-----------------------+-----------------------+-----------------------+
| ```pr-closed`` <#pr-c | No                    | Steps taken if a pull |
| losed>`__             |                       | request is closed     |
|                       |                       | without being merged  |
|                       |                       | to its base branch    |
+-----------------------+-----------------------+-----------------------+

.. _build:

build key
~~~~~~~~~

The ``build`` key is required in the ``events`` top-level key. The build
event is triggered by the ``pipelines start`` command. The contents of
the ``build`` key describe how the workspace is to be built. It must
contain a single ``steps`` key, with values describing the actual
process of the build.

.. _fail:

fail-on-build key
~~~~~~~~~~~~~~~~~

The ``fail-on-build`` key is optional in the ``events`` top-level key, and will execute only if the build event fails. The ``fail-on-build`` must contain a single ``steps`` key, which may have multiple values. For example:

.. code-block:: none

      fail-on-build:
          steps:
            - runonfailure:
                type: script
                script:
                  - "echo 'This is simple echo from fail-on-build event'"

.. _pr-merged:

pr-merged key
~~~~~~~~~~~~~

The ``pr-merged`` key is triggered when a GitHub pull request is merged
to its base branch. This key must contain a single ``steps`` key, with a
value describing the actual process.

.. _pr-closed:

pr-closed key
~~~~~~~~~~~~~

The ``pr-closed`` key is triggered when a GitHub pull request is closed
without being merged to its base branch. This key must contain a single
``steps`` key, with values describing the actual process.

.. _steps:

steps key
~~~~~~~~~

The ``steps`` key describes the steps to accomplish the build. Each step
will be executed in the order it appears in the ``steps`` key of the
build definition file.

Each ``steps`` key has a ``type`` property that indicates how the step
will be executed.

.. note::

  When creating your build definition file, the final action in the ``steps`` key should move the directory to the docroot. If you do not do this, your build cannot be used on |acquia-product:ac|.

type: script
^^^^^^^^^^^^

Steps of ``type: script`` let you specify arbitrary shell commands to be
executed by Bash. Each ``type: script`` step must include a ``script``
key whose value is a list of shell commands, each listed on a separate
line starting with a dash (-). When the ``script`` step runs, the lines
are all combined into a single Bash script and executed.

By default, the pipelines feature prepends scripts with ``set -e``,
which causes the script to exit immediately if any command has a
non-zero exit code. You can override this behavior by including
``set +e`` in your build script. Be aware that if you use ``set +e``,
the script does not fail when a command fails, and so it is the
responsibility of the script to manage its own exit strategy and exit
codes.

If a ``script`` step runs a program in the background (such as an HTTP
server), the backgrounded program is terminated at the end of the step
that it was started in. This means that a backgrounded program that
started in one ``script`` step will not be present and available in a
subsequent steps.

.. _ssh-keys:

ssh-keys key
~~~~~~~~~~~~

The ``ssh-keys`` key enables you to add SSH keys that may be required to access private resources. These keys are encrypted and can be generated using the ``pipelines encrypt`` command. Here is an example ``ssh-keys`` key:

.. code-block:: none

      ssh-keys:
        mykey:
           secure: 2aciWcRBNXrG/KcABCOvoIDTDG1bboUsVjDl+h+QRi$

Any number of keys can be added in the ``ssh-keys`` key. The value of
the ``ssh-keys`` key (``mykey`` in this example) is the name of the key.
When the pipelines feature reads the build definition file, it attempts
to decrypt the SSH keys. If the decryption is successful for one or more
keys, |acquia-product:ac| writes those keys into the ``~/.ssh``
directory, making them automatically available for use when accessing
private resources from the build script.

.. _ssh-keys-link:

Linking to specific SSH keys with a variable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To specify which SSH key will be used in a script, set the ``PIPELINE_SSH_KEY`` variable with the correct key, as in the following example:

.. code-block:: none

      version: 1.1.0
      events:
        build:
          steps:
            - welcome:
                script:
                  - echo 'STARTED'
                  - export PIPELINE_SSH_KEY=~/.ssh/ssh-key-1
                  - git ls-remote git@bitbucket.org:username/repo-dependent-on-ssh-key-1.git
                  - echo 'Steps (git operations) will be successful which are dependent on ssh-key-1' 
                  - unset PIPELINE_SSH_KEY
                  - echo 'Step executed with default ssh keys'
                  - export PIPELINE_SSH_KEY=~/.ssh/ssh-key-2
                  - git ls-remote git@bitbucket.org:username/repo-dependent-on-ssh-key-2.git
                  - - echo 'Steps (git operations) will be successful which are dependent on ssh-key-2' 
                  - unset PIPELINE_SSH_KEY
                  - echo 'FINISHED'
      ssh-keys:
        ssh-key-1:
          secure: REDACTED
        ssh-key-2:
          secure: REDACTED

When a specified SSH key is no longer required in a step, use ``unset PIPELINES_SSH_KEY`` to switch back to the default key.

.. _metadata:

pipelines_metadata key
~~~~~~~~~~~~~~~~~~~~~~

There are times when it can be useful to provide information from the
container or the build execution back for your use — for example, one
item from a specific execution step that could influence a future
direction for your desired execution process. To allow for this,
|acquia-product:ac| includes the ``pipelines_metadata`` key, which can
be run from any section of the build definition file.

The key's usage is based on the following structure:

.. code-block:: none

     pipelines_metadata [key] [value]

where

-  ``[key]`` is the variable name you want to create for reporting
-  ``[value]`` is the value you want to set for your created variable

You can view the contents of any metadata created using this key by running the `status </acquia-cloud/develop/pipelines/cli/commands#errors>`__ command with the ``--format=json`` option.

.. _lint:

Validating your build definition file
-------------------------------------

To determine if your build definition file uses valid YAML syntax, you
can use an online validator, such as one of the following:

-  `YAML Lint <http://www.yamllint.com>`__
-  `Yaml Validator <http://codebeautify.org/yaml-validator>`__ at Code
   Beautify

.. _fullexample:

Examples
--------

Use this section as you develop your own, custom build definition files.

General example
~~~~~~~~~~~~~~~

Here is an example of a complete build definition file:

.. code-block:: none

      version: 1.1.0
  
      variables:
        global:
          SLACK_HOSTNAME: "yourslack.slack.com"
          SLACK_TOKEN:
            secure: U48EOVjDl+h+QRi$x3kpGwBIc27rKqCblXqkv2MxMBDyV+Pas3x...
          SLACK_CHANNEL: "#pipelines"

      events:
        build:
          steps:
            - build:
                type: script
                script:
                  - composer install
                  - compass compile docroot/themes/custom/MY_THEME
            - unit_tests:
                type: script
                script:
                  - ./vendor/bin/phpunit
            - notify:
                type: script
                script:
                  - curl -X POST --data "payload={"channel": "${SLACK_CHANNEL}", "username": "${SLACK_USERNAME}", "text": "success"}" https://${SLACK_HOSTNAME}/services/hooks/incoming-webhook?token=${SLACK_TOKEN}

      ssh-keys:
        my_module:
          secure: SCxLERS9GcOrgz72zZwqBiCIx7GsWpP2Nxyx3kpGwBIc27rKqCblXqkv2MxM...

Empty MySQL database
~~~~~~~~~~~~~~~~~~~~

The following build definition file example creates an empty MySQL database:

.. code-block:: none

     version: 1.0.0
     services: 
       - mysql

     events:
       build:
         steps:
           - setup:
               type: script
               script:
                 - mysql -u root -proot -e "CREATE DATABASE drupal"
