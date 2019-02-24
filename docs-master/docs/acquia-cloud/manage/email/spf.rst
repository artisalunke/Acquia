.. include:: /common/global.rst

Configuring SPF records for domains on |acquia-product:ac|
==========================================================

The `Sender Policy Framework <http://www.openspf.org/>`__ (SPF) is an
open standard that specifies a technical method to prevent sender
address forgery. More precisely, the current version of SPF (called
SPFv1 or SPF Classic) protects the envelope sender address that is used
for the delivery of messages. For more information, visit this `quick
explanation <http://www.openspf.org/Introduction>`__ of the different
types of sender addresses in emails.

SPFv1 allows domain owners to specify their email sending policy (for
example, which email servers they use to send email from their domain).
The technology requires actions on both sides of the email exchange: the
domain owner publishes this information in an SPF record in the domain's
DNS zone, and when someone else's email server receives a message
claiming to come from that domain, then the receiving server can check
that the message complies with the domain's stated policy. For example,
if the message comes from an unknown server, it can be considered a
fake.

If you're receiving the message ``Sender address rejected``, this is
often caused by missing or incorrect SPF records. If you are having
other email issues, you might find `Troubleshooting Drupal email
issues <%5Bacquia-product:kb%5Darticles/troubleshoot-drupal-mail-issues-without-actually-sending>`__
useful.

Some domain registrars require a TXT entry for your SPF record. In this
case, you must add all of the Acquia mail servers as one TXT record
rather than creating a separate entry for each of the servers. This is a
TXT rule versus just putting the domain name in a text field. This is
the current recommended format:

``v=spf1 mx include:_spf.acquia.com -all``

Based on information at `OpenSPF's record syntax
page <http://www.openspf.org/SPF_Record_Syntax>`__, the rule will
execute as follows:

#. Allows MX records from the host domain
#. Checks Acquia's defined SPF records for mail servers and allows them
#. Denies all others

This configuration says that you authorized the domains (in this case,
Acquia) to send email on your behalf. Directions for updating your
record will vary depending on your DNS provider. Here are links to
specific instructions for `Network
Solutions <http://www.networksolutions.com/support/how-to-manage-advanced-dns-records/>`__,
`GoDaddy <http://help.godaddy.com/article/680#spfrecs>`__, and
`EasyDNS <http://support.easydns.com/tutorials/SPF/>`__.

Note

Acquia does not currently support whitelisting of its mail server IP
addresses. These IP addresses can change at any time. Acquia only
supports SPF whitelisting.

The recommended snippet also rejects all non-Acquia domains. If you have
SPF records in your own domain, they also need to be added to ensure
outgoing mail is handled correctly. For example, Google Apps Business
users may need to use the following code:

``v=spf1 include:_spf.acquia.com _spf.google.com -all``

SPF records must all exist on the same TXT record. Adding multiple TXT
records with differing SPF data may have unexpected side effects.

If you're not sure if your SPF records are correct, there are `SPF
Record Testing Tools <http://www.kitterman.com/spf/validate.html>`__
that you can use.
