.. include:: /common/global.rst

Acquia Commerce Manager security
================================

|acquia-product:acm| provides security across multiple levels of the
service. For a complete list of Acquia security information, see
`Security and compliance </acquia-cloud/arch/security>`__.

Acquia Commerce Manager authentication
--------------------------------------

|acquia-product:acm| API and modules require authentication in the form
of a HMAC-SHA256 message hash as a header within the request. HMAC is a
keyed-hash authentication code that calculates message authentication
involving a cryptographic hash function in combination with a secret
cryptographic key. Information about securing HTTP requests with HMAC
can be found in `RFC-2104 <https://tools.ietf.org/html/rfc2104>`__.

Acquia Commerce Manager Drupal module
-------------------------------------

The |acquia-product:acm| Drupal module uses HMAC along with OAuth2 to
secure communication from the Acquia |acquia-product:ccs| to Drupal. The
Drupal module uses `Simple
Oauth <https://www.drupal.org/project/simple_oauth>`__ which takes
advantage of OAuth2 Bearer tokens. Information about OAuth2 can be found
in `RFC-6749 <https://tools.ietf.org/html/rfc6749>`__.

Commerce Connector Service
--------------------------

The |acquia-product:acm| REST API calls authenticate using HMAC v2 to
protect your data and ensure that your secret keys stay secure, while
utilizing the Access Key ID and Secret Access Key associated with your
|acquia-product:acm| subscription. For more information about Acquia's
HMAC implementation, see the `Acquia HMAC
specification <https://github.com/acquia/http-hmac-spec>`__.

IP Whitelisting
---------------

The |acquia-product:ccs| service maintains a pool of IP addresses per
AWS region for its outbound client connections to eCommerce backends.
The eCommerce system can whitelist this pool of IP addresses to help
safeguard against external access.

Each IP pool is made up of a dedicated set of Amazon Elastic IP
addresses (EIP) reserved in the |acquia-product:acm| production
accounts. The EIPs can be dynamically associated to running instances of
the |acquia-product:ccs|, enabling the |acquia-product:ccs| service to
update seamlessly in the background while still providing the eCommerce
backend a known connection address.
