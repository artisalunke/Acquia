.. include:: /common/global.rst

Drupal security
===============

Drupal, the functional and foundational set of APIs and modules, powers
hundreds of thousands of websites on the Internet. As such, Drupal code
is continuously probed, scanned, and analyzed for security
vulnerabilities. Through peer review and a large and continuously
growing community of experts and enthusiasts, Drupal's core APIs have
been strengthened over the long life of Drupal to mitigate common
vulnerabilities. Drupal is designed to prevent critical security
vulnerabilities, including the Top 10 security risks identified by the
Open Web Application Security Project (OWASP). Drupal has proven to be a
secure solution for enterprise needs and is used in high profile,
critical websites. This topic includes the following sections:

-  `Drupal security team <#drupsec>`__
-  `Security-related contributed modules <#secmod>`__
-  `Drupal password security <#druppass>`__
-  `Secure Drupal hosting in |acquia-product:ac| <#sechosting>`__
-  `Drupal site security <#enssec>`__
-  `Additional platform-level best practices <#bestprac>`__

.. _drupsec:

Drupal security team
--------------------

The Drupal Security Team includes approximately 40 people, several of
whom are Acquia employees. The security team works with the `Drupal
Security Working
Group <https://www.drupal.org/governance/security-working-group>`__,
which reviews and supports the work of the security team. The security
team created a framework to report and prioritize the mitigation of
security vulnerabilities discovered both in Drupal core and in Drupal
contributed modules. The team also provides best practices for secure
module development and Drupal website creation and configuration.

.. _secmod:

Security-related contributed modules
------------------------------------

In addition to the proven security of Drupal core, numerous contributed
modules strengthen the security of a Drupal website. These modules
extend Drupal's security by adding password complexity, login, and
session controls, increasing cryptographic strength, and improving
Drupal's logging and auditing functions. For further research on
security-related Drupal modules, see `Enhancing security using
contributed modules <https://www.drupal.org/node/382752>`__ on
Drupal.org.

.. _druppass:

Drupal password security
------------------------

There has been much publicity about password breaches of service
providers' websites. Often the root cause of the breach of user
passwords is due to poor access controls at the password database and
weak encryption methodologies used to encrypt the database. Acquia
believes that both strong access controls and strong encryption
methodologies are the best means of protecting passwords. Drupal
encrypts passwords held in the database using the strong SHA512 hash
function with a per-user salt function applied.

.. _sechosting:

Secure Drupal hosting in |acquia-product:ac|
--------------------------------------------

To prevent common vectors of attack, |acquia-product:ac| is built to
ensure that Drupal websites are hosted securely in accordance with best
practices. Major points include the following:

-  The process owners of both the web server and the PHP server do not
   have write access to the web root. The PHP server can only write to a
   specific set of directories: the ``[web root]/files`` and
   ``[web root]/sites/[sitename]/files`` or the corresponding
   ``files-private`` directories. These directories are writable by
   nature, because they are intended to receive file uploads from end
   users.
-  Files in the web root (such as Drupal core and its modules) are
   written by an automated process and pulled from a version control
   system (Git) only.
-  Even customer users logged in to the OS layer on a web server do not
   have write access to files in the web root.
-  |acquia-product:ac| manages code and configuration with Puppet. This
   means that if a file *is* changed somehow, Puppet will reset this
   file back to the known good configuration.

.. _enssec:

Drupal site security
--------------------

-  **|acquia-product:ais|**
   |acquia-product:ais| is a subscription service communicates with your
   Drupal website using a Drupal module on your website. Insight
   provides a reporting interface that analyzes your Drupal website and
   reports to site administrators pertinent security-related data, such
   as configuration issues, security patch information, and other data
   to help Drupal administrators identify and action both security and
   performance-related issues.
-  **Security audits**
   Acquia provides security audits to customers as a professional
   service engagement. These security audits include penetration tests
   and comprehensive code and architecture layer review to ensure that
   any custom development of your Drupal website has not introduced
   vulnerabilities. An Acquia Security Audit is typically a one-week
   engagement on website with your development team. Many security firms
   provide penetration and code review services, but only Acquia is
   solely focused on Drupal.
-  **Remote Administration**
   Acquia offers a `Remote Administration </ra>`__ (RA) service to
   proactively keep its customers' Drupal websites up-to-date with the
   latest security patches and bug fixes to both Drupal core and
   contributed modules.

.. _bestprac:

Additional platform-level best practices
----------------------------------------

As a site administrator, you can take additional steps to ensure that
your |acquia-product:ac| Drupal website is secure. For additional steps,
see `Password protect development and staging environments using
``.htaccess`` <%5Bacquia-product:kb%5Darticles/password-protect-your-non-production-environments-acquia-hosting>`__.

.. _related:

Related topics
--------------

For more information about Drupal security, see the following:

-  `Is Drupal
   secure? <https://www.drupal.org/documentation/is-drupal-secure>`__ on
   Drupal.org
-  `Securing your
   site <https://www.drupal.org/security/secure-configuration>`__ on
   Drupal.org
-  `The importance of user roles and permissions for site
   security <%5Bacquia-product:kb%5Darticles/importance-user-roles-and-permissions-site-security>`__
