.. include:: /common/global.rst

Modifying your security settings
================================

You can protect the |acquia-product:sfi| or any websites that use OpenID
accounts by configuring the following security settings:

-  `Minimum password strength <#minimum-password-strength>`__
-  `Two-factor authentication <#two-factor-authentication>`__


Minimum password strength
-------------------------

You can specify a security policy for passwords that users must use to
access the |acquia-product:sfi| or any of your websites that use OpenID
accounts. The password security policy determines how *strong* (or
resistant to guessing) user passwords must be to be accepted as valid by
|acquia-product:edg|.

.. note::  

   Regardless of your password security policy settings, |acquia-product:edg| 
   requires a minimum password length of seven (7) characters for 
   |acquia-product:sfi| and OpenID accounts.

Determining a password's strength
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Password strength policies enforce rules about what can be used as a
password that will not easily be compromised or guessed by another
person. At their most basic level, these policies can be as simple as
having to include at least one number, an uppercase letter, and a
lowercase letter. This does not actually result in passwords that are
hard to guess; for example, the password ``Passw0rd`` satisfies the
previous rule, but is not a very strong password.

Instead of a basic approach, the |acquia-product:edg| password strength
system applies a combination of rules to rank how difficult the password
is to guess. For example, the following examples decrease an entered
password's strength ranking:

-  Words included in a dictionary of common words, common first and last
   names, or common passwords
-  Words included in the dictionary, but with common *1337* (or *leet*)
   substitutions, such as ``4`` or ``@`` for ``a``, and ``5`` for ``s``
   — these are treated as only slightly stronger than the words
   themselves
-  Common sequences of letters or numbers (``abcde`` or ``12345``)
-  Characters in a keyboard pattern (``qwerty`` or ``zaq1``)
-  Three or more repeated characters (``1111``)
-  Dates or years (``1921`` or ``19-11-1978``)

The password strength policy prohibits users from using their Acquia
accounts' email address as a password.

The password strength levels assigned to passwords are based both on the
amount of entropy (randomness) in each password and an estimate of the
amount of time it could take to determine (or *crack*) each password
using a brute force attack (based on current estimations). The estimated
time-to-crack at each level is about two orders of magnitude greater
than the next lower level, so a Weak password might take minutes to
crack, while a Very Strong password might take years.

Examples
^^^^^^^^

-  **Weak passwords**

   For example, these are very weak passwords:

   -  ``mystrongpassword`` - Dictionary words
   -  ``el1z@b3th`` - Common name, with *leet* substitutions
   -  ``11121957`` - Date
   -  ``9876598765`` - Keyboard sequences

-  **Strong passwords**

   A password can rank as extremely strong even if it consists of only
   elements like those described here, as long as it contains enough
   distinct elements and is long enough.

   For example, these are very strong passwords:

   -  ``correctdonkeybatterystaple`` - Long password (even though it
      contains four dictionary words)
   -  ``Drupal>Wordpress`` - Long password
   -  ``9a8b7c6d5e`` - Long password without keyboard patterns

Resources for creating strong passwords
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For inspiration, see this `XKCD comic <http://xkcd.com/936/>`__. For a
method for creating strong passwords consisting of randomly chosen short
words, see the the `Diceware Passphrase Home
Page <http://world.std.com/~reinhold/diceware.html>`__ and the
`Diceware <http://en.wikipedia.org/wiki/Diceware>`__ article in
Wikipedia.

Setting the password strength policy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To enable or change the password strength policy for the
|acquia-product:sfi| and for your websites that use OpenID accounts,
complete the following steps:

#. Sign in to your *Prod* environment’s |acquia-product:sfi| using an
   account with the `platform
   admin </site-factory/users/admin/platform-admin>`__ role.
#. In the admin menu, click **Administration**, and then click the
   **Security settings** link.
#. In the **Minimum required password strength** section, select the
   minimum required strength from the following values:

   -  **disabled** - Passwords can have any password strength ranking
      (but must still be seven characters or longer)
   -  **weak** - Passwords must have a password strength ranking of
      *weak* or greater
   -  **good** - Passwords must have a password strength ranking of
      *good* or greater
   -  **strong** - Passwords must have a password strength ranking of
      *strong* or greater
   -  **very strong** - Passwords must have a password strength ranking
      of *very strong* or greater

#. Click **Save configuration**.

Stage environment password strength policies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are a PaaS subscription customer, you can also directly modify
the password strength policy for your *Stage* environment.

Although it is possible to use the previous password strength policy
procedure to change your Stage environment's policy, each time you stage
websites from your Prod environment to your Stage environment, your
Factory settings are also copied with your websites — this includes your
Prod password strength policy settings.

Transitioning to stricter password policies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After you enable a password strength policy, |acquia-product:sfi|
account and OpenID user passwords are tested for their strength during
sign-in. If a password fails to meet the policy, the user is not
permitted access, and is then prompted to change the password to one
that satisfies the strength requirement of the policy.

As a user types a new password, |acquia-product:edg| tests and reports
the password's strength. When users create passwords that do not satisfy
the password strength policy, they will receive an error message that
describes the reasons that the password cannot be accepted. For example:

.. code-block:: none

      The following issues were detected with your password:
      * Contains dictionary words (e.g. "password")

When changing your password, |acquia-product:edg| provides information
about acceptable password requirements following the **Confirm
password** field.

|Password strength settings|

Two-factor authentication
-------------------------

You can enable two-factor authentication (also known as *two-step
verification*) to control access to your subscription through the
|acquia-product:sfi|. Two-factor authentication is more secure than
password authentication alone. With two-factor authentication enabled, a
user signing in to the |acquia-product:sfi| or a website that uses
OpenID accounts must supply not just a user email address and password,
but also a code sent to a trusted device.

.. note::  

   This page describes how to require two-factor authentication for all of
   your user accounts. For information about how to sign in with two-factor
   authentication, see `Configuring two-factor authentication for your
   account </site-factory/users/tfa>`__.

To change your Factory two-factor authentication settings, complete the
following steps:

#. Sign in to your *Prod* environment’s |acquia-product:sfi| using an
   account with the `platform
   admin </site-factory/users/admin/platform-admin>`__ role.
#. In the admin menu, click **Administration**, and then click the
   **Security settings** link.
#. In the **Two-step verification** section, select either **Required**
   or **Not required** to indicate whether Factory accounts and website
   accounts using OpenId must use two-factor authentication or not,
   respectively.
#. Click **Save configuration**.

Controlling when idle users are signed out
------------------------------------------

To better secure your hosted websites, you can configure
|acquia-product:edg| to sign users out of websites after a configurable
period of inactivity. Doing this helps to protect accounts from
unauthorized use if a browser window is left open and unattended.

To enable or modify how |acquia-product:edg| handles inactive users,
complete the following steps:

#. Sign in to your *Prod* environment’s |acquia-product:sfi| using an
   account with the |platform admin|_ role.
#. In the admin menu, click **Administration**, and then click the
   **Security settings** link.
#. In the **Automatic logout settings** section, select the **Sign out
   inactive user accounts** check box to sign out inactive users, or
   clear the check box to allow inactive users to remain signed in to
   your websites indefinitely.
#. If the **Sign out inactive user accounts** check box is enabled, in
   the **Time in seconds** field, enter the number of seconds a user may
   be inactive before being signed out.
   For example, entering ``900`` in the field will sign out users after
   15 minutes of inactivity.
#. Click **Save configuration**.

.. |Password strength settings| image:: https://cdn2.webdamdb.com/1280_I4KnGW1ek81.png?1526475774
   :width: 590px


.. |platform admin| replace:: *Platform admin*
.. _platform admin: /site-factory/users/admin/platform-admin