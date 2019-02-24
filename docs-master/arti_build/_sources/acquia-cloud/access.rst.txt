.. include:: /common/global.rst

Controlling access to Acquia Cloud
==================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/access/*

|acquia-product:ac| provides a comprehensive set of security features
that you can use to control who can access your Acquia applications and
how. These features include:

-  `Teams, roles, and permissions </acquia-cloud/teams>`__ - This
   feature allows you to assign roles to your team members, with
   fine-grained permissions that govern what they are allowed to access
   and do, and allows you to assign members to teams, where each team
   can have one or more applications in your organization that they can
   work on
-  `Two-step
   verification </acquia-cloud/access/two-step-verification>`__ - By
   default, all users need to sign in with a user name (email address)
   and password to sign in to the |acquia-product:ui| and access an
   Acquia application. You can also enable two-step verification, which
   requires users in addition to use a trusted device or enter a
   verification code that they receive by mobile application or text
   message
-  **Session timeout** - When you are signed in to the
   |acquia-product:ui|, your session expires after 90 minutes of
   inactivity, and you will be required to sign in again with your user
   name and password before you take any actions that require being
   signed in. This helps to secure your |acquia-product:ac| applications
-  `Password strength
   requirements </acquia-cloud/access/password-strength>`__ - You can
   optionally require that any users that sign in to the
   |acquia-product:ui| must have a password that meets a password
   strength requirement, to ensure that their passwords are not easy to
   guess
-  `IP address whitelisting </acquia-cloud/access/ip-whitelist>`__ - You
   can configure |acquia-product:ac| so that only specified IP addresses
   on a whitelist can access your applications through the
   |acquia-product:ui|

Each of these features controls access to the |acquia-product:ui| and
not access to your |acquia-product:ac| websites or other applications.

.. _tasks:

Handling user-based tasks
-------------------------

Administrators are responsible for managing all aspects of their users,
from access to permissions. The following documentation pages include
information that describes these basic organizational tasks:

-  `Adding and removing team members </acquia-cloud/teams/members>`__
-  `Adding, editing, and assigning roles </acquia-cloud/teams/roles>`__
-  `Creating custom roles </acquia-cloud/teams/roles#create>`__
-  `Managing your organization </acquia-cloud/teams/organizations>`__
