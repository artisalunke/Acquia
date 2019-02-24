.. include:: /common/global.rst

Managing users with |acquia-product:acm|
========================================

When using |acquia-product:acm|, the commerce solution can be used both
as a customer repository and as an authentication service. A local copy
of the user is stored in Drupal, and after every update, the user's
information is pushed to the commerce solution. Drupal will send emails
to users based on user management issues; these are the only emails it
will send.

Users that are authenticated can browse their list of orders. These
orders are stored in the commerce solution and are retrieved on demand.
Everything related to order management is done by the commerce solution,
including sending emails about orders to users.

User authentication
-------------------

User authentication is handled by several components of the
|acquia-product:acm| stack.

-  *HMAC* – Between Drupal and the |acquia-product:ccs|, and between the
   |acquia-product:ccs| and your commerce solution (such as Magento).
-  *OAuth* – The OAuth module handles the actual stream of
   authentication.
-  *User accounts* – These are handled in the following ways:

   -  Accounts are handled in Drupal and your commerce solution, but the
      user only has contact with Drupal. Drupal then handles
      authentication with the commerce solution. (Preferred)
   -  The account is verified directly against the commerce solution.

Customer Creation
-----------------

If your user has an account in Drupal and your commerce solution, the
accounts will automatically be paired if they are using the same email
address. If they are not using the same email address, the store manager
can, for example, set the user's ``Magento ID`` to their Drupal user,
which will also pair the accounts across both applications.

Customer accounts are tied to Drupal users. The commerce customer ID is
stored as a field on the user entity called ``acq_customer_id``.
Customers can create orders and review order, profile, and addresses
from the commerce system.

Existing Customers (Commerce only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a customer already exists as a commerce customer, but not a Drupal
customer, creating a new order creates a Drupal account. Their commerce
customer ID will be linked to the Drupal user, using the email address
is used to match customers.

If a customer creates a new Drupal account, their account will not be
tied to the commerce account at that time and they will not be able to
see old orders until their account is linked.

Returning Customers (Drupal)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Customers who have previously created orders within Drupal will be
required to sign in to create additional orders. Because passwords are
not created during the first order, users must request a password reset
before signing in and proceeding with additional orders.

As a quick reference for creating users on your Drupal website, complete
the following steps:

#. Sign into your Drupal website as an administrator.
#. Click **People**.
#. Either click **Add user** to create a new user, or click **Edit**
   next to an existing user to change that user's information.
#. Manage user roles and permissions by clicking the **Permissions**
   tab.
#. To change the process by which users apply for accounts, click
   **Configuration > Account settings**.

For a more thorough description of the user creation and management
process in your Drupal website, see `Users, roles and
permissions <https://www.drupal.org/node/120614>`__ on Drupal.org.
