.. include:: /common/global.rst

Password security
=================

To ensure the security of user accounts, it is important to both select
a strong password and to change your password occasionally. Although
|acquia-product:aj| does its part by enforcing `periodic password
changes <#reset>`__ for user accounts, it's up to you to ensure that the
passwords that you select are safe and secure.

Password requirements
---------------------

To help with this, |acquia-product:aj| requires that any passwords that
you use must meet the following criteria:

-  Contain at least eight characters, with a maximum of 50 characters
-  Contain at least one of each of the following characters:

   -  Lowercase letter (``a`` through ``z``)
   -  Uppercase letter (``A`` through ``Z``)
   -  Number (``0`` through ``9``)
   -  Special character, from the following character set:
      ``! @ # $ % ^ & *``

-  Cannot be in the list of the past five passwords used for the account

Periodic password resets
------------------------

|acquia-product:aj| enforces periodic password changes every 90 days. If
your password is expired, |acquia-product:aj| will display a
notification message on the sign-in webpage.

|expired password notice|

To reset your password and choose a new password that meets the
`previously specified criteria <#req>`__, complete the following steps:

#. On the |acquia-product:aj| sign-in webpage, click the **Forgot my
   Password** link to display the **Reset Password** dialog box.
#. In the list, click **I do not have my reset token**, and then enter
   the email address associated with your account (to which
   |acquia-product:aj| will email a reset token link).
#. Click **Email Reset Token**.
#. After you receive your reset token email, open the email, and then
   click its **Set my Password** link to display the **Set Password**
   dialog box.
#. Enter your token, and then enter a new password (based on the
   previously described `password requirements <#req>`__).
#. Click **Set Password** to save your new password.

You can now use your new password to sign in to |acquia-product:aj|.

.. |expired password notice| image:: https://cdn3.webdamdb.com/1280_wvdVFhUIYR69.png?1526475744
   :width: 237px
   :height: 75px
