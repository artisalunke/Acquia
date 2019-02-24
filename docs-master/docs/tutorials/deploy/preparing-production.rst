.. include:: /common/global.rst

Preparing for Production
=========================

.. container:: message-status

   Deploy – |Back to intro|_ |br| 
   Next lesson – |Next lesson|_

.. |Back to intro| replace:: Back to intro
.. _Back to intro: /tutorials/deploy.html

.. |Next lesson| replace:: Generating a deployment artifact
.. _Next lesson: /tutorials/deploy/generating-deployment-artifact

.. |bltlink| replace:: \ |acquia-product:blt|\ 
.. _bltlink: /devtools/blt

Lesson Goal
-----------

.. container:: message-status

   Review the fundamental quality assurance and deployment processes.

In order to complete this lesson you will need:

-  A Drupal 8 application that is ready to be reviewed and deployed

The following tools are not required, but are recommended:

-  |bltlink|_

In this lesson we will:

#. Review the role automated testing
#. Review the role of human review
#. Review the concept of “production as an artifact”
#. Create a production ready artifact

When deploying your code to production, you should have a high degree of
confidence that your application works as intended. Having a development
workflow that includes quality assurance (QA) is the best means of
instilling this confidence.

If you are using a continuous integration workflow, you have the
opportunity to perform quality assurance continuously. You will have
tested and reviewed your codebase throughout the development process.
This reduces the burden of deploying your code to production by
preventing QA debt from accumulating.

At a minimum, your QA process should include both automated testing and
human review. A brief overview of these topics is covered below.

Prerequisite QA process
-----------------------

|Automated test robot|
^^^^^^^^^^^^^^^^^^^^^^

Automated Tests
^^^^^^^^^^^^^^^

Your Drupal application should have a suite of automated tests. These
are custom to your application and they serve to assert that your
application works the way that you and your users expect.

Do not fall prey to common rationalizations and excuses relating to
insufficient time, money, or resources. Time spent developing tests will
yield future rewards exponentially. “The bitterness of poor quality
remains long after the sweetness of meeting the schedule has been
forgotten.”\ :sup:`1`

If you are not already using a testing framework, we recommend using
|bltlink|_.
|acquia-product:blt| provides a testing framework which enables you to
quickly write and execute automated tests using two popular testing
tools: Behat and PHPUnit. To learn more about these tools and how to
implement them on a Drupal application, please review this tutorial’s
**Resources** section.

|People reviewing plans|

Human Review
^^^^^^^^^^^^

Human review remains an essential component of quality assurance, even
with a robust suite of automated tests. There will always be issues that
only a human can catch.

Ideally, you will review code changes continuously throughout the
development process. There are many SaaS tools that enable you to do
this by providing interfaces for reviewing and discussing code changes.
Popular tools include GitHub, GitLab, and BitBucket. At present, GitHub
is directly integrated with the |acquia-product:ac| pipelines
functionality and is the recommended code collaboration tool.

In fact, you can use GitHub to enforce the practice of code review. See
`Enabling required reviews for pull
requests <https://help.github.com/articles/enabling-required-reviews-for-pull-requests/>`__
and `Protected
Branches <https://help.github.com/articles/about-protected-branches/>`__
to learn how you can require this practice when using GitHub.

Production is an artifact of development
----------------------------------------

With the adoption of Composer in Drupal 8, the process of deploying a
Drupal application has fundamentally changed. Drupal 8 applications
should not be deployed by merely uploading a site via FTP or pushing a
tag via Git. Instead, Drupal 8 should be deployed by executing a build
process that transforms your development “source” codebase into a
production-ready artifact.

This concept may be new to the Drupal community, but it is a well
established practice in software development. Much in the way that an
iOS or Java app needs to be compiled, a Drupal 8 codebase should be
“built” for production.

The underlying principle is simple: production is an artifact of
development. Put differently, the things that you need to run your
Drupal site in a production capacity are not the same things that you
need to develop your Drupal site locally. For instance, you may use a
suite of tools like Drush, Devel, Views UI, PHP CodeSniffer, SASS, etc.,
to develop your Drupal application. These are tools used to produce your
site, but they are not your site, and hence these things do not belong
on your production server.

The build process is intended to take your development “source” code and
produce an artifact that is production ready. Often, this means removing
development-only packages, sanitizing your codebase, and optimizing your
application for performance.

Next Lesson > `Generating a deployment artifact </tutorials/deploy/generating-deployment-artifact>`__
-----------------------------------------------------------------------------------------------------

:sup:`1`\ Karl Wiegers

Resources
---------

-  `Automated Testing - BLT
   Documentation <http://blt.readthedocs.io/en/8.x/readme/testing/#testing>`__
-  `Testing your site with the Drupal Extension to Behat and
   Mink <http://behat-drupal-extension.readthedocs.io/en/3.1/intro.html>`__
-  `Behavior Driven Testing with Behat (in less than 5
   minutes) <https://www.isovera.com/blog/behavior-driven-testing-behat-less-5-minutes>`__

.. |Automated test robot| image:: https://cdn2.webdamdb.com/1280_2oSJV5TrflH2.jpg?1527887499
.. |People reviewing plans| image:: https://cdn4.webdamdb.com/1280_c6aHvf5PQIn5.png?1527887499

