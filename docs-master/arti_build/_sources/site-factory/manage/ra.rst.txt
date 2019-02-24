.. include:: /common/global.rst

Remote administration for |acquia-product:edg|
==============================================

Acquia offers `Remote Administration </ra>`__ (RA) as an additional
service for all |acquia-product:edg| subscriptions.

What RA does
------------

With RA enabled, Acquia takes responsibility for Drupal security updates
in your |acquia-product:edg| codebase. Acquia creates an additional
environment in your |acquia-product:edg| installation. When Drupal
security updates become necessary, Acquia updates the RA environment
with the needed changes. Acquia then notifies you that the updates are
ready for you to test in the RA environment.

Standard (not Premium) RA is available for |acquia-product:edg|
subscriptions. For information about what is covered by RA updates, see
`Understanding the scope of Remote Administration </ra/scope>`__. For
details about how RA works, see the `Remote Administration </ra>`__
documentation. For |acquia-product:edg|, after the Acquia RA team
creates a new branch in your `RA environment </ra/environment>`__, your
development team is responsible for tagging and deploying branches for
additional testing, and then deploying the tested tag to production
using the Site Factory Management Console.

.. _how:

How to get started with Remote Administration
---------------------------------------------

If you think Remote Administration is a good fit for your
|acquia-product:edg|, contact your Acquia account manager. If you
already have processes in place to manage Drupal security updates, you
probably don't need Remote Administration.
