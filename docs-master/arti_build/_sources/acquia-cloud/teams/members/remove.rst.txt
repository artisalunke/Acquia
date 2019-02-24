.. include:: /common/global.rst

Best practices for team member departures
=========================================

Security is important for every website. When employees leave a project
or company for whatever reason, it's a good idea to review their
security access to prevent potential future tampering or the loss of
important data. Failure to handle departures properly can result in
issues such as the following:

-  Incorrect credit card charges
-  Failure to receive |acquia-product:ac| platform notifications
-  Account and application security breaches

.. _cloud:

|acquia-product:ac| security steps
----------------------------------

If you are an |acquia-product:ac| customer, review the following steps
that you should take to secure your websites after an employee's
departure:

-  **Remove the employee from your Acquia Teams**
   The subscription administrator should terminate the employee. If the
   administrator is the departing employee, the departing employee can
   `designate a new organization
   owner </acquia-cloud/teams/organizations#transfer>`__. If this is not
   possible, contact `Acquia Support </support#contact>`__ and cc the
   previous owner (if possible) for an easier transition. If the
   previous owner is unavailable, contact your Account Manager for
   assistance. If you do not have an Account Manager, `contact Acquia
   Support </support#contact>`__.
-  **Remove any entries specific to the employee from your Users and
   Keys page**
   After you sign in to your |acquia-product:ac| subscription, go to
   **Workflow > Users and Keys** to either change the passwords for the
   private keys or to generate new keys entirely.
-  **Remove the employee from any elevated roles on your websites**
   Be sure to validate against any single sign-on solutions that you may
   be using.
-  **Remove the employee's entries from the Teams and Permissions
   pages**
   For information about how to do this, see `Managing team members:
   Removing a member from a
   team </acquia-cloud/teams/members#remove>`__.

.. _drupal:

Drupal security
---------------

Be sure to review the following items to secure your website after an
employee's departure:

-  **Change any administrative passwords to which the employee had
   access**
   Affected passwords can include the website itself, shell accounts,
   and phpmyadmin.
-  | **Review the Drupal roles and permissions**
   | From the employee's account page, you can either change an
     employee's access to a lower permission level or set it to
     **blocked**.

   .. important:: 

      Acquia does not recommend deleting accounts, because doing so can
      lead to data loss in Drupal.

-  **Review recent code changes**
   Especially in the case of a less-than-amicable parting, it is
   possible that departing individuals could commit code that allows
   continued access to the website through a back door.
-  **Revoke access to servers and version control systems**
-  **Review IP whitelists on firewalls and in Apache (or your** ``.htaccess`` **files)**
-  **Change the** |salt|_ **for your encryption**

.. |salt| replace:: **salt**
.. _salt: http://en.wikipedia.org/wiki/Salt_(cryptography)