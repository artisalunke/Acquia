.. include:: /common/global.rst

Getting started with Node.js applications and environments
==========================================================

If you're already familiar with the |acquia-product:ac| interface,
getting started with a Node.js application is similar to the other
applications you have already created in |acquia-product:ac|.

For your reference, here's how Node.js applications and environments are
managed, and how you develop your code in them, which may be slightly
different than your previously created applications and environments.

.. _manage:

Managing applications
---------------------

Many of the basic application management functions are the same for
|acquia-product:ac|-hosted Drupal applications. These functions include:

-  Modifying views of applications
-  Adding applications
-  Renaming applications

For a full explanation of each of these functions, see `Managing
applications with the |acquia-product:ac|
interface </acquia-cloud/manage/applications>`__.

.. _environments:

Managing environments
---------------------

The |acquia-product:ac| implementation of Node.js uses separate
environments to help you maintain a clear and orderly workflow as you
develop, test, and publish your applications. An application is deployed
on each of its environments, but each environment may be in a different
state — possibly with a build artifact deployed. Each environment has a
URL at which its application can be accessed, but only the production
environment's URL is designed to be visible to the application's users
(website visitors).

Acquia Node.js applications start with one production (**Prod**)
environment, and one development (**Dev**) environments. See `Resources
and limitations for Node.js
environments </acquia-cloud/node-js/resources>`__ for server details.

-  *Development environments* - Shared between customers
-  *Production environments* - Dedicated to a single customer

.. _develop:

Developing your application
---------------------------

Development with Node.js on |acquia-product:ac| requires that you create
`pipelines </acquia-cloud/develop/pipelines>`__ for your code.

Based on the normal pipelines workflow, after `connecting your
application to a repository </acquia-cloud/develop/pipelines>`__, you
must `create your build definition
file </acquia-cloud/develop/pipelines/yaml>`__.

The |acquia-product:ac| uses the conventional ``npm start`` command to
start your Node.js application. Ensure that you have a snippet similar
to the following in your application's ``package.json`` file:

.. code-block:: json

    "scripts": {   
        "start": "node index.js" 
    }

For a detailed tutorial regarding local Drupal and Node.js setup, see
`Setting up a local Drupal and Node.js
application </tutorials/nodejs-decoupled-drupal-acquia-cloud/set-local-drupal-and-nodejs-application>`__.

.. _pl-commands:

Pipelines client commands
~~~~~~~~~~~~~~~~~~~~~~~~~

The pipelines client for |acquia-product:ac| includes `commands that are
specific to Node.js
applications </acquia-cloud/develop/pipelines/cli/commands#nodecommands>`__.
For a full listing of all commands the pipelines client provides, see
`Using the |acquia-product:ac| pipelines
client </acquia-cloud/develop/pipelines/cli/commands>`__.

.. _pl-script:

Example script
~~~~~~~~~~~~~~

Here is an example script for building a pipelines artifact with your
Node.js application:

.. code-block:: yaml

    version: 1.0.0 
    variables:   
            global:     
                HOSTING_API_STAGE: canary
                
    events:   
        build:
         steps:
            - build:
               script:
                 - nvm install v6.11.2
                 - nvm use 6.11.2
                 - npm install --production
            - upload-artifact:
               script:
                 - pipelines-artifact start
                 - pipelines-artifact upload $SOURCE_DIR 
        fail-on-build:
         steps:
            - fail: 
               script:
                 - pipelines-artifact fail
