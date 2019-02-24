.. include:: /common/global.rst

Deploying your applications to |acquia-product:ac|
================================================================

.. container:: message-status

   Node.js with Decoupled Drupal on |acquia-product:ac| – |Back to intro|_ |br| 
   Previous lesson – |Previous lesson|_

.. |Back to intro| replace:: Back to intro
.. _Back to intro: tutorials/nodejs-decoupled-drupal-acquia-cloud.html

.. |Previous lesson| replace:: Setting up a local Drupal and Node.js application
.. _Previous lesson: /tutorials/nodejs-decoupled-drupal-acquia-cloud/setting-local-drupal-and-nodejs-application

Lesson Goal
-----------

.. container:: message-status

   Deploy Drupal and Node.js applications to |acquia-product:ac|

Overview and Configuration
--------------------------

*To complete this lesson you need access to an Acquia Cloud environment with both a Drupal and a Node.js dev environment*

With the Drupal and JavaScript applications available locally, we will
focus next on the deployment of these applications. While steps slightly
vary for each application, the same workflow methodology applies when
deploying a build artifact to the Acquia Cloud.

To complete the next tasks, you will need to add the Acquia Cloud Git
URL as a remote using the following command.

Locate the Git URL under the "Information" section in your Acquia Cloud
Subscription:

|giturl|

Add the URL as a Git remote:

::

       git remote add cloud YOUR_CLOUD_GIT_URL

The new git remote has been added. Switch to the master branch of this
location for each application.

Creating the deploy artifact with Acquia Pipelines
--------------------------------------------------

Acquia Pipelines will now create the build artifact. So if you have not
set up Acquia Pipelines locally, follow the steps outlined in `this
tutorial </tutorials/getting-started-acquia-cloud-cd/installing-cd-pipelines-client-locally>`__.

To build an artifact for both applications, add a acquia-pipelines.yml
file in the respective root of each codebase. An example of the
acquia-pipelines.yml file for Drupal is available at this
`reference </acquia-cloud/cd/pipelines/yaml>`__ and the example for
Node.js is found at this `reference </acquia-cloud/node-js/start>`__.

There may be the need to set the default Application ID for your local
repository to properly associate the artifact to the subscription. Use
``pipelines list-applications`` to find the ID for your Acquia Cloud
application, then set the ID with
``pipelines set-application-id --application-id=[application-id]``.

Now that everything is configured appropriately, you can build your
artifact with:

::

       pipelines start

Deploying the Drupal codebase
-----------------------------

Once the artifact is built, deploy the artifact to your environment
within the Cloud UI. This can be accomplished by going to the
"Environments" tab and choosing "Switch" for the proper build artifact.
You can see a full explanation of the process at the `Code
workflows </acquia-cloud/develop/code/environments>`__ documentation.

|code switch|

Deploying the JavaScript codebase
---------------------------------

Deploying the artifact to the Acquia Cloud can be accomplished by
following the same workflow as the Drupal deployment steps. Go to the
"Environments" tab and click the "Code" element icon. This will allow
you to switch the artifact to based on a hash number. You can view the
complete steps for deploying your application in the `Deploying build
artifacts in your Node.js
environment </acquia-cloud/node-js/workflow>`__ documentation.

|artifact|

Resources
---------

-  `Code workflows
   documentation </acquia-cloud/develop/code/environments>`__
-  `Deploying build artifacts in your Node.js
   environment </acquia-cloud/node-js/workflow>`__
-  `Do you have a question or comment regarding this
   lesson? <mailto:tutorial-help@acquia.com?subject=Decoupled%20Tutorial%20Lesson#3>`__

**Congratulations! You have deployed both applications to the appropriate Acquia Cloud environments and are ready for review.**
-------------------------------------------------------------------------------------------------------------------------------

.. |giturl| image:: https://cdn4.webdamdb.com/1280_EpkIam26KN91.png?1527886246
.. |code switch| image:: https://cdn4.webdamdb.com/1280_cNeXsHAaVgS6.png?1527886249
.. |artifact| image:: https://cdn4.webdamdb.com/1280_wZhFho5iBub3.png?1527886247

