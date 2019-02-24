.. include:: /common/global.rst

Installing CD pipelines client locally
=======================================

.. container:: message-status

   Getting Started with |acquia-product:ccd| – |Back to intro|_ |br| 
   Next lesson – |Next lesson|_

.. |Back to intro| replace:: Back to intro
.. _Back to intro: /tutorials/getting-started-acquia-cloud-cd

.. |Next lesson| replace:: Defining a Build
.. _Next lesson: /tutorials/getting-started-acquia-cloud-cd/defining-build

Lesson Goal:
------------

.. container:: message-status

   Download and install the CD pipelines client locally and execute pipelines commands.

In this lesson, we will install the Acquia `CD
pipelines </acquia-cloud/develop/pipelines>`__ client to your local
machine in order to execute CD pipelines commands. This tool is an
essential part of developing, testing, and deploying applications on
|acquia-product:ac|.

In order to complete this lesson you will need:

-  A web browser access to an |acquia-product:ac| subscription
-  An Acquia subscription user account with the `“Execute CD pipelines”
   permission </acquia-cloud/develop/pipelines#connect>`__
-  A \*NIX terminal on your local machine

In this lesson we will:

#. Download and install the CD pipelines client
#. Configure the CD pipelines client (authenticate with
   |acquia-product:ac|)
#. Execute a CD pipelines command to ensure that the installation was
   successful

1. Download and install the CD pipelines client
-----------------------------------------------

At a terminal command prompt, execute the following commands:

.. code-block:: none

   curl -o pipelines https://cloud.acquia.com/pipeline-client/download    chmod a+x pipelines

Test the downloaded client by executing: ``./pipelines``

.. raw:: html

   <iframe src="https://asciinema.org/a/105408/embed?size=medium&amp;speed=1&amp;autoplay=1&amp;loop=1&amp;theme=asciinema&amp;t=0&amp;preload=1" id="asciicast-iframe-105408" name="asciicast-iframe-105408" scrolling="no" allowfullscreen="true" style="overflow: hidden; margin: 0px; border: 0px; display: inline-block; width: 810px; float: none; visibility: visible; height: 521px;"></iframe>


**Note:** We recommend that the ``pipelines`` file move to a directory
in your local machine’s
`$PATH <http://www.linfo.org/path_env_var.html>`__. For instance, on
MacOS move the pipelines file to ``/usr/local/bin/pipelines``. Since
``/usr/local/bin`` is in ``$PATH``, moving ``pipelines`` here will allow
``pipelines`` to run on the command line and automatically find the
correct file.

.. code-block:: none

   mv pipelines /usr/local/bin/pipelines

2. Configure the CD pipelines client
------------------------------------

Please see the `step-by-step instructions for CD pipelines
authentication </acquia-cloud/develop/pipelines/connect>`__.

|Configuring CD pipelines in the AC UI|

3. Execute a pipelines command
------------------------------

| You may now run ``pipelines`` or ``pipelines list`` to view a list of
  available CD pipelines commands.
|  

.. code-block:: none

   pipelines list

Next Lesson > `Defining a Build </tutorials/2-defining-build>`__
----------------------------------------------------------------

.. |Configuring CD pipelines in the AC UI| image:: /sites/docs.acquia.com/files/inline-images/pipelines_configure%20%281%29_0.gif

