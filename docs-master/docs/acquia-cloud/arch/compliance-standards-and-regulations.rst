.. include:: /common/global.rst

Compliance with standards and regulations
=========================================

When it comes to cloud service providers, it is in an organization’s
best interest to perform due diligence on vendor’s compliance with
applicable industry standards and regulations. What organizations deploy
to the cloud may be governed by some form of regulatory standard. If you
require additional information regarding your particular regulatory
requirements, contact Acquia.

This page summarizes Acquia's compliance with the following standards
and regulations:

-  `SOC 1 (SSAE No. 16 and ISAE No. 3402) <#soc1>`__
-  `SOC 2 <#soc2>`__
-  `PCI DSS (Payment Card Industry Data Security Standard) <#pci-dss>`__
-  `ISO 27001 certification <#iso27001>`__
-  `FedRAMP <#fedramp>`__
-  `FISMA <#fisma>`__
-  `CSA STAR (Cloud Security Alliance Security, Trust and Assurance
   Registry) <#csa>`__
-  `EU cookie regulations <#eucookie>`__
-  `Privacy <#privacy>`__

.. _soc1:

SOC 1 (SSAE No. 16 and ISAE No. 3402)
-------------------------------------

Statement on Standards for Attestation Engagement (SSAE) No. 16 is an
American auditing standard issued by the American Institute of Certified
Public Accountants (AIPCA) and is used to create a Service Organization
Control (SOC) 1 branded report. Acquia’s SSAE 16 audit report is aligned
with the International Standards for Assurance Engagements (ISAE) No.
3402 auditing standard. This allows for the report to be recognized both
in the U.S. and throughout the world.

Acquia has a SOC 1 SSAE 16/ISAE 3402 Type 2 audit performed on an annual
basis by an independent third-party audit firm. The audit report attests
to the design and operating effectiveness of Acquia’s business and
security controls in safeguarding systems and data. Acquia’s SSAE
16/ISAE 3402 audit report is available to current customers and
prospective customers upon request and with a fully executed non
disclosure agreement (NDA).

.. _soc2:

SOC 2
-----

A SOC 2 report, titled “Report on Controls at a Service Organization
Relevant to Security, Availability, Processing Integrity,
Confidentiality or Privacy” is designed to meet a broad set of reporting
needs about the controls at a service organization in the form of a CPA
firm’s independent attestation report. SOC 2 reports are based on the
following AICPA Trust Services Principles and Criteria (TSPC):

-  *Security* - The system is protected against unauthorized access
   (both physical and logical).
-  *Availability* - The system is available for operation and use as
   committed or agreed.
-  *Processing Integrity* - System processing is complete, accurate,
   timely, and authorized.
-  *Confidentiality* - Information designated as confidential is
   protected as committed or agreed.
-  *Privacy* - Personal information is collected, used, retained,
   disclosed, and destroyed in conformity with the commitments in the
   entity’s privacy notice and with criteria set forth in Generally
   Accepted Privacy Principles issued by the AICPA and CICA. The TSPC of
   security, availability, and processing integrity are used to evaluate
   whether a system is reliable.

Acquia has a SOC 2 Type 2 audit performed on an annual basis by an
independent third party audit firm. The audit report attests to the
suitability of the design and operating effectiveness of Acquia’s
controls to meet the Security, Availability and Confidentiality Trust
Services Principles. Acquia’s SOC 2 audit report is available to current
customers and prospective customers upon request and with a fully
executed NDA.

.. _pci-dss:

PCI
---

Payment Card Industry Data Security Standard (PCI DSS) compliance
applies to merchants and services providers that process, store, or
transmit credit card data. PCI DSS is a multifaceted security standard
that includes requirements for security management, policies and
procedures, network architecture, software design, and other critical
protective measures. This comprehensive standard helps organizations
proactively protect credit card data that is transmitted or stored on
the Acquia platform. Acquia’s PCI compliance is only applicable to
customers that build web applications within the Acquia shared PCI
Virtual Private Cloud (VPC) or via dedicated PCI VPC Shield offering.
Acquia has been validated by an independent Quality Security Assessor
(QSA) approved by the PCI Security Standards Council that validated
Acquia’s adherence with standards applicable to a Level 1 service
provider under PCI DSS Version 3.2. The Attestation of Compliance (AOC)
and Report on Compliance (ROC) documents validate Acquia's PCI DSS
compliance, and can be provided to prospective or current customers upon
request.

|acquia-product:ace| and |acquia-product:edg| subscribers with websites
that require PCI DSS compliant environments should contact their Account
Manager to discuss additional infrastructure changes that may be
required for their websites to meet PCI DSS requirements.

|acquia-product:ac| for Partners subscribers with websites that require
PCI DSS compliant environments should contact Acquia Support by creating
a `support ticket </support#contact%22>`__.

Although Acquia provides a PCI-compliant hosting environment as part of
|acquia-product:ace|, only your PCI QSA or your internal security
resource completing a PCI DSS self assessment questionnaire (SAQ) can
confirm if the way your website processes credit card payments will meet
PCI DSS compliance requirements. We encourage you to contact your QSA
auditor with any additional questions that you may have. Acquia cannot
determine if your website is PCI DSS compliant.

Websites is hosted on |acquia-product:ac| that processes payments
through a third party service (such as WorldPay, Paypal, or
Authorize.net) are generally PCI DSS compliant.

The Acquia Security team has spoken at length with our PCI-Auditors, as
well as a number of PCI auditors that work with our customers. Because
your website is connected to your payment gateway, it is considered
in-scope for PCI DSS compliance.

This means that your main website, which is hosted with Acquia, is
required to be PCI DSS compliant, even though the transaction is
performed through a third party service. Consequently, your website
would need to be moved into our shared VPC to meet PCI DSS compliance.

For information about Amazon’s PCI accreditation, see Amazon's `PCI DSS
Compliance
page <https://aws.amazon.com/compliance/pci-dss-level-1-faqs/>`__. For
more information about e-commerce and PCI DSS compliance, see the PCI
Security Standards Council's documentation for `PCI DSS E-commerce
Guidelines <https://www.pcisecuritystandards.org/pdfs/PCI_DSS_v2_eCommerce_Guidelines.pdf>`__.

.. _iso27001:

ISO 27001 certification
-----------------------

Acquia is ISO 27001 certified. You can download our certificate
`here <https://cert.schellmanco.com/?certhash=qqFMzp4nFSrt>`__. ISO
27001 is a globally recognized security standard driven by the
implementation of an information security management system (ISMS). An
ISMS is a security framework of policies, procedures and controls that
includes administrative, physical and technical safeguards to manage
information security risks to internal and customer information.

FedRAMP
-------

Acquia is a `Federal Risk Authorization and Management Program (FedRAMP)
compliant
system <https://marketplace.fedramp.gov/#/product/acquia-cloud?sort=productName&productNameSearch=acquia>`__
and has received an agency Authority to Operate (ATO) from the
Department of the Treasury. As a FedRAMP compliant Cloud Service
Provider (CSP) supporting U.S. government agencies and departments,
Acquia is committed to meeting the guidelines of FedRAMP and will
provide insight into Acquia’s security architecture and the continuous
monitoring processes related to the Acquia Platform as a Service (PaaS).

Our system has been designed to meet NIST 800-53 standards for customers
who must complete their local security authorization process, sometimes
called the Risk Management Framework (RMF), or FISMA.

In addition, |acquia-product:ac| is built on Amazon AWS and thus
inherits Infrastructure layer controls from Amazon. Separately, Amazon
AWS has received `FedRAMP
authorization <https://aws.amazon.com/compliance/fedramp/>`__ for the
Infrastructure layer.

FISMA
-----

Acquia enables US government agencies to achieve and sustain compliance
with FISMA. Numerous Federal organizations have successfully achieved
security authorizations and made risk-based decisions to allow websites
to be hosted on |acquia-product:ac| in accordance with the Risk
Management Framework (RMF) process defined in the NIST Special
Publication (SP) 800-37. Acquia's platform has helped federal agencies
expand cloud computing use cases and deploy sensitive government data
and applications in the cloud, while complying with the rigorous
security requirements of federal standards.

.. _csa:

CSA STAR
--------

The Cloud Security Alliance (CSA) is a not-for-profit organization with
a mission to promote the use of best practices for providing security
assurance within Cloud Computing and to provide education on the uses of
Cloud Computing to help secure all other forms of computing. The CSA is
led by a broad coalition of industry practitioners, corporations,
associations, and other key stakeholders.

CSA's Security, Trust and Assurance Registry (STAR) is a free, publicly
accessible registry that documents the security controls provided by
cloud computing offerings, thereby helping organizations assess the
security of cloud providers they currently use or are considering
contracting with. Acquia has completed and published its Consensus
Assessments Initiative Questionnaire (CAIQ), which provides
industry-accepted ways to document the security controls in our PaaS
(platform as a service) offering. The CAIQ provides a set of over 140
questions that a cloud consumer and cloud auditor may wish to ask of a
cloud provider.

Acquia's CAIQ is available for download from the `CSA STAR
registry. <https://cloudsecurityalliance.org/star/#_registry/>`__

.. _eucookie:

EU cookie regulations
---------------------

The Privacy and Electronic Communications Regulations 2003 (a European
Community (EC) Directive) cover the use of cookies and similar
technologies for storing information and accessing information stored on
users' equipment, such as their computer or mobile phone. In 2009, this
Directive was amended by Directive 2009/136/EC. This included a change
to Article 5(3) of the E-Privacy Directive requiring consent before a
website stores cookies or similar technologies.

Drupal websites, like the vast majority of websites, make use of session
cookies and may employ other types of cookies. Acquia's customers should
consult with their legal counsel as to whether their website is required
to implement consent before storing cookies on customer devices that
serve EU users. Acquia can work with its customers to implement
technical solutions, including modules or custom code, in order to
satisfy the requirements from the customers' legal counsel.

Privacy
-------

Acquia abides by all privacy laws and regulations that are applicable to
our hosting services and to our customers that host websites that may
contain personal information on |acquia-product:ac|. Acquia personnel
have logical access to customer data stored in customer websites only if
they are authorized, and have a need for access due to their job
function. Acquia does not transfer customer data hosted on
|acquia-product:ac| outside of |acquia-product:ac| or to any third party
without customer authorization.

Customers must ensure that privacy concerns and regulations are
addressed and adhered to at the application layer where customer
personnel may have logical access to personal information uploaded or
stored in customer websites.

`Acquia’s Privacy
Policy <https://www.acquia.com/about-us/legal/privacy-policy>`__
describes how Acquia handles any personal information gathered from
visitors to its website at acquia.com and from users of our software and
services from Acquia.
