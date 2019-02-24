.. include:: /common/global.rst

Understanding the architectural workflow
================================================

.. container:: message-status

   Node.js with Decoupled Drupal on |acquia-product:ac| – |Back to intro|_ |br| 
   Next lesson – |Next lesson|_

.. |Back to intro| replace:: Back to intro
.. _Back to intro: tutorials/nodejs-decoupled-drupal-acquia-cloud.html

.. |Next lesson| replace:: Setting up a local Drupal and Node.js application
.. _Next lesson: /tutorials/nodejs-decoupled-drupal-acquia-cloud/setting-local-drupal-and-nodejs-application

Lesson Goal
-----------

.. container:: message-status

   Understand the core workflow of a decoupled architecture.

Introduction
------------

Before diving into the technical steps, let’s understand the high-level
design of the architecture itself. A “headless” or “decoupled” Drupal
architecture typically involves the communication between two separate
applications: a Drupal website (acting as a data source) and a front-end
application (acting to display data provided by Drupal). For the
purposes of this tutorial, we will use a Node.js based front-end
application.

|simple decoupled|

Benefits of a Decoupled Architecture
------------------------------------

There are often project requirements which help to surface benefits of
leaning on a decoupled Drupal architecture. These project requirements
usually revolve around the intent of an “API-first” methodology.
API-first Drupal can be contextually understood as leveraging the CMS to
expose data for consumption in another application. Benefits of this
architecture typically revolve around the desire to store data in
Drupal, while offering options of displaying that same data in other
locations outside of Drupal.

Role of Drupal in a Decoupled Architecture
------------------------------------------

The core function of Drupal within the decoupled architecture to serve
as a data source, but that role could translate into a couple of
different things. There are project scenarios in which the Node.js
application is intended to emulate the content type fields and mirror
the data in the same manner. Some project requirements indicate that
selected content combine to offer promotional or real-time updates.
While there are a wide range of technical purposes, the end result of
this scenario is typically structured around the housing of data. In
this case a “data source” should be interpreted for both database
storage and data construction patterns.

Role of Node.js in a Decoupled Architecture
-------------------------------------------

The role of Node.js within our decoupled architecture is two-fold:
presenting data that is ingested from Drupal and sending data back to
Drupal. In most cases, the Node.js application core focus serves the
application and displays data from Drupal. This is not a suggestion that
the application pulls data from Drupal solely, but for the purpose of
this tutorial we will make this assumption. This need is a key driver
for the adoption of Node.js as the abstracted presentation layer.

Next lesson:
------------

`Setting up a local Drupal and Node.js
Application </tutorials/nodejs-decoupled-drupal-acquia-cloud/setting-local-drupal-and-nodejs-application>`__

.. |simple decoupled| image:: https://cdn2.webdamdb.com/md_UavQHFqqAuu2.jpg?1527881349

