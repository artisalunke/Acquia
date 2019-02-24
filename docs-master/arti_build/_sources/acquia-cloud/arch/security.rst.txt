.. include:: /common/global.rst

Security and compliance
=======================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/arch/security/*

This topic describes how |acquia-product:ac|, building on Amazon Web
Services (AWS) and using Drupal, provides a secure environment for your
applications. It includes the following sections:

-  `|acquia-product:ac| and the shared responsibility model <#shared>`__
-  `Amazon AWS Control Environment <#aws>`__
-  `Physical security <#physicalsec>`__
-  `Customer segregation <#custseg>`__
-  `System access controls <#system>`__
-  `OS and LAMP stack security patch management <#ospatch>`__
-  `Antivirus upload scanning <#antivirus>`__
-  `File system encryption <#encryption>`__
-  `SSL and HTTPS <#ssl>`__
-  `Data and physical media destruction <#physicalmedia>`__
-  `Logging <#logging>`__
-  `|acquia-product:as| <#search>`__

.. _shared:

The shared responsibility model of |acquia-product:ac|
------------------------------------------------------

Security in |acquia-product:ac| is a shared responsibility between
Acquia, Amazon Web Services, and the customer. |acquia-product:ac|
provides a secure platform where Acquia customers may build and manage
world-class, highly secure Drupal applications. Acquia manages,
monitors, and secures the environment where our customer applications
run, including the operating system and LAMP (Linux, Apache, MySQL, PHP)
stack and network layers of |acquia-product:ac|. Additionally, Acquia
provides tools, support, and resources that enable our customers to
maintain secure Drupal applications.

Customers have numerous responsibilities in regards to the security of
the applications they host with |acquia-product:ac|. Customers must
understand what data they intend to collect and store in their Drupal
application and ensure that risks and compliance requirements are
addressed, which correlates to the importance and sensitivity of that
data. Customers must ensure that security is addressed during the
development lifecycle of their Drupal application, including ensuring
that secure development best practices are followed and that security
testing is conducted as part of the change process. Customers must
ensure that the security controls that are deployed to the Drupal
application are in line with the risk and the mission of the
application. Customers are responsible for the security of the web
applications they manage on the Acquia platform, while Acquia is
responsible for security controls at the network and platform layer.

|acquia-product:ac| is built using Amazon's AWS data centers, and uses
Amazon's Elastic Compute Cloud (EC2), Amazon Simple Storage Service
(S3), and Elastic Block Store (EBS) services. Amazon personnel do not
have logical access to |acquia-product:ac| hosts or applications, nor
can they access the data of any |acquia-product:ac| customers hosted on
|acquia-product:ac| platforms.

.. _aws:

Amazon AWS control environment
------------------------------

To maintain the high level of security Amazon provides to its customers,
it does not disclose every detail about network topology, physical
locations, and AWS-specific security procedures to the public.
|acquia-product:ac| leverages `Amazon's certifications and
attestations <https://aws.amazon.com/compliance/>`__ to provide
assurance to Acquia and its customers about the security of the
infrastructure, network, and physical security layers of
|acquia-product:ac|. Amazon shares certification information about the
AWS control environment with strategic partners such as Acquia under
nondisclosure agreements (NDAs), and thus Acquia cannot release this
information to any unauthorized party. Acquia is committed to
maintaining a high degree of transparency and trust with its customers,
so Acquia makes as much information available to its customers as it can
legally and safely disclose.

To find more information regarding the security of Amazon AWS, see
Amazon's `AWS Cloud Security <https://aws.amazon.com/security/>`__ page
or contact Acquia.

.. _physicalsec:

Physical security
-----------------

Amazon's AWS data centers follow and enhance best practices in data
center physical security. The exterior physical security is military
grade. Personnel who enter the data center are authorized and verified
by a government issued ID, as well as a two-factor authentication at
each entrance point. Each entrance is monitored by video surveillance,
and all access is logged and audited. All visitors and contractors must
present identification and sign in. They are always escorted by
authorized staff. Amazon AWS does not permit guests, customers, or
strategic partners such as Acquia to either tour or inspect its data
center. Therefore, Acquia cannot facilitate any type of physical
inspection of AWS hosting facilities for customers.

Acquia maintains some infrastructure on its premises—for example, IP
phone switches and LAN equipment—but this equipment is not used either
to host customer applications or to store sensitive customer
information. Acquia cooperates with customers who want to speak with the
Acquia security team to discuss the |acquia-product:ac| control
environment.

.. _custseg:

Customer segregation
--------------------

|acquia-product:ace| provides independent, logically separate
environments for each customer application. Each component (web servers
and databases) of the customer's technology stack in
|acquia-product:ace| is provisioned on unique, logically distinct
servers, with the exception of the load balancers. Dedicated load
balancers are available to |acquia-product:ace| customers at an
additional cost. In |acquia-product:ac|, Acquia manages host-based
firewall policy (IPTables), which provide network isolation between
logically distinct customer environments in |acquia-product:ac|.

.. _system:

Systems access controls
-----------------------

Acquia limits privileged access both to the information on the customer
servers under its management and to the servers themselves. Access is
limited to its authorized full-time operations and support teams.
Network layer controls ensure that privileged access is always enforced
through secure bastion hosts, using encrypted tunnels through
nonstandard ports. Authentication requires multi-factor authentication
using a user account, private key, passphrase, and security token. Each
privileged user's password-protected SSH key is stored on an encrypted
volume. All access attempts using SSH are logged and retained for
audits.

Customers may provision non-privileged user accounts to the customer's
web nodes using the Acquia web-based UI and APIs. The Acquia platform
gives customers the ability to create named users and upload those
users' SSH public keys, which are deployed to the customer's web
servers, enabling non-privileged access using SSH.

Acquia manages access to the cloud environment’s Apache docroot
directory using version control; there is no write access to this
directory. Acquia customers provision non-privileged access to their
|acquia-product:ac| web nodes through Acquia's web-based
|acquia-product:ac| management interface. The Acquia platform provides
application administrators with the ability to add non-privileged users'
accounts and SSH keys, which are then deployed to the customer's
|acquia-product:ac| web nodes.

.. _ospatch:

OS and LAMP stack security patch management
-------------------------------------------

Acquia’s security and operations teams subscribe to relevant security
notification feeds, including Ubuntu security notices, Tenable security
notices, and US-Cert. When a patch or update has been published at the
operating system layer or specific to a software component, the patch
and vulnerability is reviewed to determine if it is relevant to the
|acquia-product:ac| environment. If so, a tracking ticket is created for
Security Engineering teams to assess and score the vulnerability based
on applicability, likelihood, impact and mitigating factors utilizing
industry-standard scoring frameworks (such as CVSS). A fix for the
vulnerability is then incorporated into a subsequent release based on
the rating and in accordance with Acquia's standard patching cadence. If
the patch or update requires a service restart that may affect
customers, a notification is sent to |acquia-product:ac| customers to
inform them of the impending maintenance.

Acquia uses a standardized Ubuntu Linux distribution and a central
management platform to deploy security patches across all
|acquia-product:ac| server instances.

Acquia has a formal risk-rating system based on factors such as
likelihood, impact, and severity, and deploys patches according to the
following schedule:

+------------+---------------+
| Risk Level | Schedule      |
+============+===============+
| *Critical* | 7 days        |
+------------+---------------+
| *High*     | 30 days       |
+------------+---------------+
| *Medium*   | 90 days       |
+------------+---------------+
| *Low*      | Based on risk |
+------------+---------------+

.. _antivirus:

Antivirus upload scanning
-------------------------

Acquia installs ClamAV on all |acquia-product:ac| web servers. ClamAV is
an open source (GPL) antivirus engine designed for detecting Trojans,
viruses, malware, and other malicious threats. To enable ClamAV virus
scanning on files as they are uploaded to your Drupal application,
install, enable, and configure the
`ClamAV <https://www.drupal.org/project/clamav>`__ module, which
connects to the ClamAV executable on your |acquia-product:ac| server.
For more information, see `Enabling virus scanning for file
uploads </acquia-cloud/manage/antivirus>`__.

.. _encryption:

File system encryption
----------------------

You can use two approaches to enable encryption at rest. Customers may
choose to purchase encrypted EBS volumes. Data and associated keys are
encrypted using the AES-256 algorithm with `Amazon EBS
Encryption <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>`__.
This option does entail a negative performance impact.

Alternatively, you can implement Drupal modules that enable the
encryption of fields that contain confidential information in the
database. For more information, see `Encrypting and decrypting content
in Drupal <https://groups.drupal.org/node/258513>`__ on Drupal.org.

.. _ssl:

SSL and HTTPS
-------------

You should configure SSL certificates on the primary domain name for
your applications to provide SSL security for authentication functions
and for any secure transactions taking place.

-  All paid applications on |acquia-product:ac| can use SSL.
-  Dedicated load balancers are *not required*.
-  Customers may use *their own certificate* from any SSL vendor.
-  Acquia supports all valid SSL certificates: single-domain,
   multi-domain (UCC/SAN), wildcard, Extended Validation, or even
   self-signed.
-  This feature is available to all customers.
-  `Read more about this feature </acquia-cloud/ssl>`__.

*|acquia-product:acs|* – Customers can enable SSL entirely on their own
using the SSL page in the |acquia-product:ui|. Customers must provide an
SSL certificate themselves. Note that in |acquia-product:acs|, users
*cannot* use SSL on a bare domain name, such as ``https://example.com``.
It must be in the form ``https://www.example.com`` (although the ``www``
can be anything).

*|acquia-product:ace|* – Customers can enable SSL entirely on their own
using the SSL page in the |acquia-product:ui|, or can submit a support
ticket asking for SSL to be enabled. Customers must provide their own
certificate.

.. _physicalmedia:

Data and physical media destruction
-----------------------------------

Customer confidential information is never stored outside of the AWS
infrastructure for extended periods of time or on physical media, such
as a CD or removable USB media.

Customer data would only be transferred outside of Amazon's EC2
environment if it was needed to help solve a customer’s problem, local
problem resolution steps were required, and it was explicitly authorized
by the customer. After this problem was rectified, the files would be
purged. In practice, customer-sensitive information is never stored on
laptops, mobile devices, or physical media outside of the protections
AWS provides.

When a customer cancels service with Acquia, the customer's servers are
terminated, and the application data is deleted. Hard drives and other
storage media are never removed from the data centers before the data
has been sanitized, so that the data cannot be recovered. When a storage
device has reached the end of its useful life, AWS procedures include a
decommissioning process that is designed to prevent customer data from
being exposed to unauthorized individuals. AWS uses the techniques
detailed in DoD 5220.22-M (“National Industrial Security Program
Operating Manual“) or NIST 800-88 (“Guidelines for Media Sanitization”)
to destroy data as part of the decommissioning process. If a hardware
device is unable to be decommissioned using these procedures, the device
will be degaussed or physically destroyed in accordance with industry
standard practices.

Logging
-------

The |acquia-product:ac| platform ensures that the appropriate level of
logging is implemented at the application (Drupal), web server (Apache),
load balancing (Nginx), database (MySQL-Percona), and operating system
layers (Linux) necessary for analysis and investigation in the case of
an incident or issue. Each layer of the stack logs to the local
environment in real time. Logs are backed up to S3 storage daily and
retained for three months.

.. _search:

|acquia-product:as|
-------------------

`|acquia-product:as| </acquia-search>`__ is hosted on a shared
infrastructure with logical separation between each customer's data.
Each customer application's index data is segregated in separate data
files and directories. Each customer application is provisioned with a
separate account ID and key; the authorization to the search
infrastructure only allows each individual application to access its own
search data. An HMAC signature is included both in the request and the
response to ensure proper authorization and the integrity of the
content. Additionally, the session between the application server and
the search server is encrypted over SSL if available.
