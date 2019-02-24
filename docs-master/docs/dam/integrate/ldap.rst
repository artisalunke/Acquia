.. include:: /common/global.rst

Integration: LDAP
=================

..  container:: message-status

  This is an add-on feature. Contact your Account Manager to add this
  feature to your subscription.

By integrating with your Lightweight Directory Access Protocol (LDAP)
directory, you can enable LDAP-based user accounts to authenticate with
|acquia-product:dam|. The integration should be handled by your
company’s LDAP admin, who must have an |acquia-product:dam| account with
`admin privileges </dam/admin/users>`__.

.. _configure:

Configuring an LDAP connection
------------------------------

To establish an LDAP connection from |acquia-product:dam|, complete the
following steps:

#. |sign in|_ as an admin.
#. Click the **gear** icon in the upper right corner of the page, and
   then click **System Preferences**.
#. In the left menu, scroll to **LDAP Settings**.
#. Enter values in the following fields to provide your LDAP Server
   settings: |br|

   |LDAP settings example|

   -  **Enable** check box - Select this check box to enable LDAP
      authentication for |acquia-product:dam| after you have completed
      and `verified <#verify>`__ your configuration.
   -  **Server** - LDAP server hostname or IP address
   -  **Base DN** - Search Base Distinguished Name (DN), such as in the
      following example: ``ou=users, dc=company, dc=com``
   -  **Port** - Common ports are 636 for SSL connections, and 389 for
      non-SSL connections, including TLS. Ensure proper firewall access
      is enabled to the |acquia-product:dam| production IP addresses
      (``52.70.22.230``, ``52.70.142.178``)
   -  **SSL** check box - Select this check box if SSL LDAP port is in
      use
   -  **Username** - *(not necessary for an anonymous bind)* The Bind
      DN. For example,
      ``cn=service_account, ou=admin, dc=company, dc=com``
   -  **Password** - *(not necessary for anonymous bind)* Password for
      Bind DN
   -  **Groups** - *(optional)* Group membership of the LDAP user
      account, for example, ``users``
   -  **Search** - Attribute to locate LDAP user account, such as
      ``uid``.
      For Active Directory setups, use: ``sAMAccountName``

#. To test your connection, in the **Test Connection** panel enter a
   **Username** and **Password**, and then click **Test Connection**.
   Possible test status messages are listed in the `connection messages
   table <#message>`__.
#. In the **Settings** panel, select **Enable** to enable LDAP
   authentication in |acquia-product:dam|.
   |Enable LDAP settings|
#. Click **Save** to commit your changes.

Users can now sign in using their LDAP credentials.

.. _verify:

Verifying your LDAP login
-------------------------

Complete the following steps to verify that LDAP logins are functioning
correctly:

#. Go to ``http://company.example.com/splash.php``\ to test the LDAP
   login, replacing ``company.example.com`` with your company's domain
   name.
#. At the sign-in page, enter a username and password that reside in the
   LDAP database, and then click **Login**. If the login is successful,
   you will receive a *Registration successful* notification. If the
   login was not successful, refer to the
   `troubleshooting <#troubleshoot>`__ section.

.. _approved:

Approving new users by default
------------------------------

If you would like new user accounts propagated from LDAP to be approved
by default, complete the following steps:

#. Sign in to |acquia-product:dam| as an admin.
#. Click the **gear** icon in the upper right corner of the page, and
   then click **System Preferences**.
#. In the left menu, scroll to **Preferences**.
#. In the **Users and Groups** section, clear the **New users must be
   approved after registering** check box. This change will take effect
   immediately.

.. _message:

Connection messages
-------------------

The following table describes possible connection messages from
|acquia-product:dam| when testing your LDAP connection:

+-----------------------------------+-----------------------------------+
| Message                           | Description                       |
+===================================+===================================+
| **Success. Was able to connect    | LDAP configuration is successful. |
| and authenticate user**           | LDAP authentication is ready to   |
|                                   | be enabled in                     |
|                                   | |acquia-product:dam|.             |
+-----------------------------------+-----------------------------------+
| **LDAP error message: (-1) -      | |acquia-product:dam| is unable to |
| Can't contact LDAP server**       | connect to LDAP server. Allow     |
|                                   | proper firewall access to LDAP    |
|                                   | server and LDAP port for the      |
|                                   | |acquia-product:dam| Production   |
|                                   | IP addresses 52.70.22.230 and     |
|                                   | 52.70.142.178.                    |
+-----------------------------------+-----------------------------------+
| **LDAP error message: (34) -      | Bind DN is misconfigured. Supply  |
| Invalid DN syntax**               | proper Bind DN credentials or     |
|                                   | remove for Anonymous binds.       |
+-----------------------------------+-----------------------------------+
| **LDAP error message: (49) -      | Supplied LDAP credentials may be  |
| Invalid credentials**             | incorrect. Submit proper LDAP     |
|                                   | credentials. The attribute search |
|                                   | may also be incorrect. Make to    |
|                                   | supply correct attribute to       |
|                                   | locate LDAP account.              |
+-----------------------------------+-----------------------------------+

.. |sign in| replace:: Sign in to \ |acquia-product:dam|\ 
.. _sign in: /dam/access

.. |LDAP settings example| image:: https://cdn3.webdamdb.com/1280_MkpYuGEJfg87.png?1526476169
   :width: 550px
   :height: 377px
.. |Enable LDAP settings| image:: https://cdn2.webdamdb.com/1280_YQljlgAiYK29.png?1526476158
   :width: 550px
   :height: 377px
