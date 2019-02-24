.. include:: /common/global.rst

Setting up a local Drupal and Node.js application
================================================================

.. container:: message-status

   Node.js with Decoupled Drupal on |acquia-product:ac| – |Back to intro|_ |br| 
   Previous lesson - |Previous lesson|_ |br|
   Next lesson – |Next lesson|_

.. |Back to intro| replace:: Back to intro
.. _Back to intro: tutorials/nodejs-decoupled-drupal-acquia-cloud.html

.. |Previous lesson| replace:: Understanding the architectural workflow
.. _Previous lesson: /tutorials/nodejs-decoupled-drupal-acquia-cloud/understanding-architectural-workflow

.. |Next lesson| replace:: Deploying your applications to \ |acquia-product:ac|\ 
.. _Next lesson: /tutorials/nodejs-decoupled-drupal-acquia-cloud/deploying-your-applications-acquia-cloud

Lesson Goal
-----------

.. container:: message-status

   Structure a local Drupal website and a local JavaScript application for a decoupled architecture.

In this lesson, we will stand up a pre-built Drupal website locally
using some common Acquia build tools `Acquia BLT (Build and Launch
Tool) <http://blt.readthedocs.io/en/latest/readme/onboarding/#initial-setup>`__
& `Drupal VM <https://www.drupalvm.com/>`__. The Drupal sample content
and fields demonstrate a clear correlation between Drupal and the
JavaScript application, allowing for easy extensibility.

In order to complete this lesson you will need to have the following
software packages installed:

-  `Git <https://git-scm.com/downloads>`__
-  `Composer <https://getcomposer.org/download/>`__
-  `Vagrant <https://www.vagrantup.com/downloads.html>`__
-  `VirtualBox <https://www.virtualbox.org/wiki/Downloads>`__

You'll also need PHP 7.1 CLI installed in order to complete the
installation. `On MacOS the easiest way to install PHP 7.1 is with
Homebrew <https://developerjack.com/blog/2016/installing-php71-with-homebrew/>`__.

For a complete list of prerequisites and more extensive setup
instructions, refer to the `BLT
onboarding <http://blt.readthedocs.io/en/latest/readme/onboarding/>`__
and `DrupalVM quick-start
documentation <https://github.com/geerlingguy/drupal-vm#quick-start-guide>`__.

Download and Install Code Dependencies
--------------------------------------

Download the Drupal codebase by cloning the repository with:

.. code-block:: none

   git clone https://github.com/acquia/decoupled-drupal.git

Once the code has finished downloading, ``cd`` into the folder with:

.. code-block:: none

   cd decoupled-drupal/

From this location, install the package dependencies with:

.. code-block:: none

   composer install

.. raw:: html

   <iframe src="https://asciinema.org/a/135519/embed?size=“medium”&amp;speed=1&amp;autoplay=1&amp;loop=1&amp;theme=asciinema&amp;t=0&amp;preload=1" id="asciicast-iframe-135519" name="asciicast-iframe-135519" scrolling="no" allowfullscreen="true" style="overflow: hidden; margin: 0px; border: 0px; display: inline-block; width: 720px; float: none; visibility: visible; height: 466px;"></iframe>

Stand up the local Drupal instance
----------------------------------

For the next steps, set up the local Drupal site with
`BLT <http://blt.readthedocs.io/en/latest/readme/onboarding/#initial-setup>`__
& `Drupal VM <https://www.drupalvm.com/>`__ to expedite the process.
These steps can also be accomplished with a standard local LAMP stack or
a similar preference, with the assumption of maintaining the same
localhost name (local.decoupled.com).

From the same ``decoupled-drupal/`` folder location, install the BLT
alias:

.. code-block:: none

   composer run-script blt-alias

Setup your local virtual box with Drupal VM, using the BLT command:

.. code-block:: none

   blt vm

This will indicate a question "Do you want to boot Drupal VM?", which
you can type "y" to proceed. You might want to get a cup of coffee while
this completes.

Build and install the Drupal installation with:

.. code-block:: none

   blt setup

.. raw:: html

   <iframe src="https://asciinema.org/a/135528/embed?size=“medium”&amp;speed=1&amp;autoplay=1&amp;loop=1&amp;theme=asciinema&amp;t=0&amp;preload=1" id="asciicast-iframe-135528" name="asciicast-iframe-135528" scrolling="no" allowfullscreen="true" style="overflow: hidden; margin: 0px; border: 0px; display: inline-block; width: 720px; float: none; visibility: visible; height: 466px;"></iframe>

CD into docroot/ and log into your Drupal application with:

.. code-block:: none

   drush @decoupled.local uli

If you are seeing errors with the "uli" command or do not see the alias
with the "drush sa" command, you can also shell into the vagrant box. To
proceed with this workaround, follow these instructions:

.. code-block:: none

   > vagrant ssh
   > cd docroot/
   > drush uli

You can now review the test content at http://local.decoupled.com/admin/content.

|Drupal local site|
.. |Drupal local site| image:: https://cdn4.webdamdb.com/1280_k6Kf9hC0r561.png?1527885580


Setting up the Node.js Application locally
------------------------------------------

The next steps involve setting up a previously constructed JavaScript
application to work in tandem with our local Drupal application. Follow
this step only after your local Drupal codebase and site is set up. For
our example JavaScript application, `Node.js <https://nodejs.org/>`__ is
leveraged to create the pages, while using the
`Ember.js <https://www.emberjs.com/>`__ framework to pull the API data.

Install the following software packages (if not previously installed):

-  `Node.js <https://nodejs.org/>`__ (this includes NPM)
-  `Ember CLI <https://ember-cli.com/>`__ (as sudo)

For a complete list of prerequisites and setup instructions, refer to
the `decoupled-js
README <https://github.com/jenter/decoupled-js/blob/master/README.md>`__.

Download and install the Application
------------------------------------

Download the JavaScript codebase by cloning the repository with:

.. code-block:: none

   git clone https://github.com/acquia/decoupled-js.git

Once downloaded, ``cd`` into your application root with:

.. code-block:: none

   cd decoupled-js/

We will now install the required node modules with:

.. code-block:: none

   npm install

Now that the installation is complete, serve and view the JavaScript
application locally at http://localhost:8080 with:

.. code-block:: none

   npm start

.. raw:: html

   <iframe src="https://asciinema.org/a/135541/embed?size=“medium”&amp;speed=1&amp;autoplay=1&amp;loop=1&amp;theme=asciinema&amp;t=0&amp;preload=1" id="asciicast-iframe-135541" name="asciicast-iframe-135541" scrolling="no" allowfullscreen="true" style="overflow: hidden; margin: 0px; border: 0px; display: inline-block; width: 720px; float: none; visibility: visible; height: 466px;"></iframe>

**You can now view your Node.js application which is displaying the
content from Drupal!**

|nodejs app|

Overview of Current Architecture
--------------------------------

The two local applications are intended to display the scenario of a
"Decoupled Drupal" architecture. The Drupal CMS website serves as a data
source to collect data. The Drupal content types and fields are used to
structure the data.

Once the data has been structured and created, it is then exposed
through an API endpoint in Drupal. The purpose of the API endpoints is
to allow data to be used within our JavaScript application. In common
scenarios, you could allow data to be sent back and stored into Drupal.
For this tutorial, we are only pulling data from Drupal.

|simple decoupled|

.. |simple decoupled| image:: https://cdn3.webdamdb.com/md_UavQHFqqAuu2.jpg?1527881349

About the Drupal Application
----------------------------

The Drupal 8 application is built using the “Headless Lightning”
distribution as its functional baseline. `Headless
Lightning <https://github.com/acquia/headless-lightning>`__ is a more
opinionated sub-profile of the popular Lightning Drupal distribution
intended to be used as a backend for decoupled applications. It includes
two primary features: the Lightning Content API, and a Headless UI. The
Lightning Content API (which is also included in the standard Lightning
distribution) automatically exposes Drupal entities via a JSON-based
REST API. The Headless UI simplifies the Drupal administrative backend
and content authoring experience to be more accessible to users who
might be less familiar with Drupal’s administrative patterns.

The Drupal 8 application provides two simple content types ("Cats" and
"Dogs") and automatically populates them with sample data. Each of the
content types have a handful of fields for data collection.

|Cat-A|

.. |Cat-A| image:: https://cdn2.webdamdb.com/1280_Q92SMfO9um02.png?1527885756

The various content nodes are then exposed as API endpoints using the
`JSON API <https://www.drupal.org/project/jsonapi>`__ module. These
nodes can be viewed as a collection for that content type or by
individual ID based on selection. While most content scenarios are
addressed with the node patterns like ``/jsonapi/node/{content\_type}``,
others warrant combining user information as
``/jsonapi/node/{content\_type}/{uuid}``.

|jsonapi-cat|

.. |jsonapi-cat| image:: https://cdn2.webdamdb.com/1280_UPofHvAEdG35.png?1527885758

About the Node.js Application
-----------------------------

The Node.js application is a collection of modules which uses specific
functionality separately for a web server and the application itself:

-  The '/server' folder is designated to create a web server in which
   the application will layer upon. The 'server.js' file uses the
   `express.js <https://expressjs.com/>`__ web application framework to
   serve the application on port 8080 on your local machine.
-  The '/client' folder is designated for the application’s
   functionality that will interact with the content served from the
   Drupal API.

Since the core functionality of the application revolves around
ingesting an external API, the application uses the `Ember
Data <https://github.com/emberjs/data>`__ library. Ember Data does a
great job of handling the persistence of the data model, regardless of
record origin. The application validates and maps records according to
the Drupal entities by routes according to the JSON API standards for
the pertinent URL (jsonapi/node/{nodetype}). The records are then parsed
appropriately with the associated routes by querying the ID.

|cat-emberinspector|

.. |cat-emberinspector| image:: https://cdn2.webdamdb.com/1280_siVeNxDtgKw7.png?1527885758

Resources
---------

-  `Acquia BLT Documentation <http://blt.readthedocs.io/en/latest/readme/onboarding/>`__
-  `DrupalVM
   Documentation <https://github.com/geerlingguy/drupal-vm#quick-start-guide>`__
-  `decoupled-js
   README <https://github.com/jenter/decoupled-js/blob/master/README.md>`__
-  `Do you have a question or comment regarding this
   lesson? <mailto:tutorial-help@acquia.com?subject=Decoupled%20Tutorial%20Lesson#2>`__

Next lesson:
------------

`Deploying your application to Acquia
Cloud </tutorials/nodejs-decoupled-drupal-acquia-cloud/deploying-your-applications-acquia-cloud>`__


.. |nodejs app| image:: /sites/docs.acquia.com/files/inline-images/nodejs-app.gif


