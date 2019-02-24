.. include:: /common/global.rst

Enforcing password strength
===========================

You can specify a security policy for passwords that users must use to
access the |acquia-product:ac|. The password security policy determines
how strong (resistant to guessing) user passwords must be. When you
establish a password strength policy, it applies only to users when they
sign in to the |acquia-product:ac| — it does not apply to your Drupal
websites.

.. _how:

How |acquia-product:ac| judges password strength
------------------------------------------------

|acquia-product:ac| applies several rules to determine a password's
strength, which are based on the entropy (randomness) of the sequences
in the password. Use the criteria in the following table as a guide for
determining your selected security policy's password strength:

.. list-table::
   :widths: 15 55 30
   :header-rows: 1 

   * - Password strength
     - Criteria
     - Example
   * - **Very strong**
     - At least eight characters, contains multiple capital letters, digits, and special characters
     - ``H2tr*7Qi!``
   * - 
     - At least eight characters with some combination of words or character 
       sequences that when used alone would be *Weak*
       Example: Four dictionary words
     - ``correctdonkeybatterystaple``
   * - 
     - Common words with a special character
     - ``Drupal>Wordpress``
   * - 
     - Integrated sequences
     - ``9a8b7c6d5e``
   * - **Strong**
     - Eight characters, contains at least two capital letters, digits, 
       or special characters
     -  ``HvtrscQi``
   * - 
     - Nine characters, contains at least one capital letter, digit, or special character
     -  ``hvtrscQiw``
   * - **Good**
     - Eight characters, contains at least one capital letter, digit, or special character
     -  ``hvtr*cqi``
   * - **Weak**
     - Seven characters or less, contains common alphabet letters, but no 
       capital letters, digits, or special characters
     - ``raryara``
   * - 
     - Contains dictionary words
     - ``password1``
   * - 
     - Contains a common name, with `leet <https://en.wikipedia.org/wiki/Leet>`__ substitutions
     - ``Eliz@b3th``
   * - 
     - Dates
     - ``11272015``
   * - 
     - Sequences
     - ``9876598765``

.. _policy:

How to set a password strength policy
-------------------------------------

To set a password strength policy, complete the following steps:

#. Sign in to the |acquia-product:ui| with the *Owner* or
   *Administrator* role and select the application you want to work
   with.
#. In the menu on the left side, click **Security**.
#. On the **Security settings** page, click **Edit** to open the **Edit
   security settings** page.

   |Editing security settings|

#. In the **Minimum required password strength** list, click the minimum
   required `password strength <#strength>`__, from **Weak** to **Very
   strong**.
#. Click **Save**.

.. _strict:

How to transition to stricter password policies
-----------------------------------------------

After you enable a password strength policy, user passwords are tested
for strength when the user attempts to access the subscription. If a
password fails to meet the policy, the user is not permitted access and
is prompted to change the password to one that satisfies the strength
requirement of the policy.

As a user types a new password, the Acquia password policy system tests
and reports the password's strength. When users create a password that
does not satisfy the password strength policy, they receive an error
message that indicates the strictness of the website's password strength
policy and lists the tests that caused the password to be judged as too
weak. For example:

.. code-block:: none

    The following issues were detected with your password:
    * It is fewer than seven characters.
    * It includes a dictionary word.

The |acquia-product:ui| is also protected from brute-force attacks by
the following policies that limit how many sign-in attempts can be made:

-  After three failed sign-in attempts during a 30 minute timeframe from
   a single user and IP address, that user name (email) and IP address
   combination is blocked from signing in for one hour.
-  After 50 failed sign-in attempts in an hour from a single IP address,
   that IP address is blocked from signing in for one hour.

.. |Editing security settings| image:: https://cdn2.webdamdb.com/1280_WLjRjRHWC721.png?1526475790
