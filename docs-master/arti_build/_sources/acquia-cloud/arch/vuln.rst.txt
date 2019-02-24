.. include:: /common/global.rst

Vulnerability scans
===================

Acquia is responsible for managing the security architecture for the
operating system and LAMP (Linux, Apache, MySQL, PHP) stack layers. The
Acquia security team is responsible for reviewing, identifying, and
categorizing reported vulnerabilities related to the Acquia platform.
Acquia is not responsible for web application vulnerability scans.
Acquia does not currently offer web application vulnerability scans to
customers as a service.

.. _penetration:

Customer-initiated vulnerability scans
--------------------------------------

Important

Penetration testing requires dedicated hardware if your testing includes
elevated traffic levels. This prevents potential outages for
applications sharing the server that is undergoing testing.

Acquia allows vulnerability assessments (*penetration testing*)
initiated by the customer and at the customer’s expense. Customer
vulnerability scans may be run *only* against the environment that the
customer owns so that the scan does not impact other customers'
applications. If your testing includes elevated traffic levels, then
dedicated, not shared, hardware (such as load balancers) must also be
used. It may be possible to deploy dedicated hardware temporarily for
the purpose of a vulnerability assessment.

Before the scans, Acquia requires the following information:

-  Five business days of notice
-  The source IP addresses of the vulnerability scanner
-  Peak bandwidth in Gigabits per second (Gbps)

This information is required regardless of whether or not you or your
vulnerability testing consultants require prior approval from Amazon Web
Services.

To initiate this process, `contact Acquia Support </support#contact>`__.
Acquia's monitoring may generate critical alerts if certain conditions
are met simulating a brute-force attack, port scanning, or a similar
penetration testing technique. In that case, the |acquia-product:ac|
platform may treat the test as a presumed attack and block it. For more
information, see `Preparing for security, penetration, or load
testing <%5Bacquia-product:kb%5Darticles/preparing-security-penetration-or-load-testing>`__.

Acquia *does not* grant customer access to run operating system level
scans, either credentialed or uncredentialed. Customers can validate
that Acquia is running periodic operating system level scans and
mitigating any noted issues by reviewing our third party audit reports,
including `SOC
1 </acquia-cloud/arch/compliance-standards-and-regulations#soc1>`__ and
`SOC
2 </acquia-cloud/arch/compliance-standards-and-regulations#soc2>`__.

As described in `Drupal
security </acquia-cloud/arch/drupal-security>`__, Acquia also offers an
architecture-focused security audit service for Drupal as a professional
service engagement.
