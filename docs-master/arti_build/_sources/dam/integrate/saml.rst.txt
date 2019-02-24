.. include:: /common/global.rst

Integration: SAML
=================

..  container:: message-status

  This is an add-on feature. Contact your Account Manager to add this
  feature to your subscription.

The SAML (Security Assertion Markup Language) integration with
|acquia-product:dam| should be handled by your company’s SAML
administrator. The SAML administrator will require a
|acquia-product:dam| account with admin privileges.

While you can implement SAML logins at any time, Acquia recommends
setting up SAML logins during the initial onboarding process. Customers
that implement SAML logins post-implementation may create duplicate user
accounts. To avoid duplicating existing users, ensure that the
*Username* attribute returned by your identity provider is the same as
the current username in |acquia-product:dam|. When the username
attribute is not located in |acquia-product:dam|, a new
|acquia-product:dam| user account will be created.

.. _configure:

Configuring SAML login
----------------------

To configure your |acquia-product:dam| to use SAML logins, perform the
following steps:

#. Log into |acquia-product:dam| as an admin.
#. Access the |acquia-product:dam| SAML configuration: **Settings ->
   System Preferences -> SAML Settings** (left navigation menu)
#. Download |acquia-product:dam|’s SP Metadata XML file, by clicking the
   **Download** link in the *SAML 2.0 Metadata XML file* pane.
#. Add |acquia-product:dam|’s SP Metadata XML file into your company’s
   identity provider (IdP).
#. If you are using Microsoft ADFS (Active Directory Federation
   Services), complete the following steps:

   #. Under *Relying Party Trusts*, create a claim ruled based on
      `Transform an incoming claim
      template <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/technical-reference/when-to-use-a-transform-claim-rule>`__
      with the following settings:

      +---------------------------------+----------------------+
      | Option                          | Value                |
      +=================================+======================+
      | *Incoming claim type*           | Windows Account Name |
      +---------------------------------+----------------------+
      | *Outgoing claim type*           | Name ID              |
      +---------------------------------+----------------------+
      | *Outgoing name ID format*       | Transient Identifier |
      +---------------------------------+----------------------+
      | *Pass through all claim values* | Enabled              |
      +---------------------------------+----------------------+

   #. Create a second claim rule based on `Send LDAP attributes as
      Claims
      template <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/technical-reference/when-to-use-a-send-ldap-attributes-as-claims-rule>`__,
      select Active Directory as *Attribute store*. Configure claim
      rules to send the following attributes to |acquia-product:dam|:
      ``username``, ``email``, ``first name``, and ``last name``. For
      example:

      -  *SAM-Account-Name* - Name
      -  *Given Name* - Given Name
      -  *Surname* - Surname
      -  *Email-Addresses* - Email Address

#. Upload your company’s IdP XML file into |acquia-product:dam|:

   #. Export your SAML 2.0 Metadata XML from your IdP system using the
      mechanism it provides for this.
   #. Import the XML file by clicking the **Select file** link in the
      *Upload Identity Provider's SAML 2.0 Metadata XML file* panel and
      choosing the correct XML file on your computer.

#. |acquia-product:dam| requires the following attributes from the IdP:

   -  username
   -  first name
   -  last name
   -  email fields

Configure the attributes returned by the IdP to properly map to
|acquia-product:dam|’s defined fields in the *Custom Attribute Field
Mappings* panel.

The **Last parsed attribute fields** pane displays the attribute
information returned by the IdP from the last login. Use this panel to
help properly map the IdP attributes to the |acquia-product:dam|
fieldnames.

|Last parsed example|

.. note::

  This pane will be empty until the SAML login is performed. See `Testing
  SAML login <#testing>`__ in the following section. If the panel remains
  empty after SAML login, your identity provider may not be properly
  configured to return attributes to |acquia-product:dam|.

ADFS attribute mappings:

|ADFS attributes|

OneLogin attribute mappings:

|OneLogin attributes|

Shibboleth attribute mapping:

|Shibboleth attributes|

.. _testing:

Testing SAML login
------------------

#.  Use the following URL to test your SAML login, replacing
    ``company.exampledam.com`` with your |acquia-product:dam| domain:
    ``http://company.exampledam.com/saml.php``
#.  The browser will redirect to your company’s IdP.
#.  After providing SAML credentials, the user should be redirected
    back to |acquia-product:dam| as an authenticated user.

    .. note::

      Receiving the *registration successful* notification indicates SAML
      authentication was successful, but the new user account created in
      |acquia-product:dam| has been set to inactive. To allow new users to
      automatically log into |acquia-product:dam|, log into
      |acquia-product:dam| as an admin and navigate to **Settings -> System
      Preferences**, and uncheck **New users must be approved after
      registering**.

#.  Verify the user’s account is automatically created in
    |acquia-product:dam| by logging into |acquia-product:dam| as an
    admin. Navigate to **Permissions -> Users** and check the user
    account exists. If user account is not created, check the attribute
    field configurations (Step 6 in SAML setup).

.. _enable:

Enabling SAML login
-------------------

#. After verifying the SAML login is working, access the
   |acquia-product:dam| SAML configuration page
   (``http://company.exampledam.com/cloud/#settings/settings/saml-config``)
   and enable SAML in the *SAML Page Button* pane.
#. The |acquia-product:dam| splash page
   (http://company.exampledam.com/splash.php) should now display the
   **Internal Login** button triggering SAML login.

.. |Last parsed example| image:: https://cdn4.webdamdb.com/md_2o49N7Mb5bk0.jpg?1527123199
   :width: 538px
   :height: 182px
.. |ADFS attributes| image:: https://cdn3.webdamdb.com/md_IP61POdkwJj6.png?1526475683
   :width: 550px
   :height: 323px
.. |OneLogin attributes| image:: https://cdn4.webdamdb.com/md_ouQVcXpY7r22.png?1526476113
   :width: 542px
   :height: 416px
.. |Shibboleth attributes| image:: https://cdn3.webdamdb.com/md_obFwFTY0SH10.png?1526476178
   :width: 550px
   :height: 456px
