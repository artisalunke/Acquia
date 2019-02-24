.. include:: /common/global.rst

Using two-factor authentication with your Acquia user account
=============================================================

*This page describes how to sign in to the |acquia-product:ui| with
two-step verification. For information about how to enable two-step
verification for all users on your |acquia-product:aqs|, see `Setting up
two-step verification </acquia-cloud/access/two-step-verification>`__.*

.. _tfa:

What is two-step verification?
------------------------------

Two-factor authentication (TFA), sometimes called *two-step
verification*, is more secure than password authentication alone. With
two-step verification enabled, a user signing in to the
|acquia-product:ui| must supply not just a user email address and
password, but also a code sent to a trusted device, using either an
authentication application or an SMS text message.

The |acquia-product:ui| requires you to sign in again if it has been
more than 90 minutes after the last time you signed in.

.. _setup:

Setting up two-step verification on an Acquia user account
----------------------------------------------------------

When you sign in to the |acquia-product:ui|, you are directed to the
Two-Step Verification setup page. You can enable or disable two-step
verification at any time from your Acquia Profile, as described in
`Modifying two-step verification settings <#edit>`__. To set up two-step
verification, do the following:

#. Select how you want to receive verification codes (mobile
   authentication application or text message). Using a mobile
   authentication application is recommended. Using text messages is
   possible only for US or Canada phone numbers that can receive SMS
   messages.

   |Setting up two-step verification|

#. Enter your Acquia password.
#. Click **Begin** to go to the next page.
#. The two-step verification setup process will continue based on the
   method that you selected for your verification codes:

   -  | *Using a mobile application*
      | If you selected **Mobile Application** as your verification
        method, complete the following steps:

      #. Select the mobile authentication application that you want to
         use, and then click **Continue** to go to the next page. See
         `Supported mobile authentication applications <#authapps>`__.
      #. Open your mobile authentication application on your phone or
         other device. Either point it at the QR code displayed on the
         Two-Step Verification Code page, or enter the Acquia Text Code.
      #. In the **Application verification code** field on the Two-Step
         Verification Code page, enter the verification code displayed
         by your mobile authentication application.

      .. rubric:: Supported mobile authentication applications
         :name: authapps

      | Acquia two-step verification supports the following mobile
        authentication applications:

      -  `Google
         Authenticator <https://support.google.com/accounts/answer/1066447>`__
         (Android, iPhone, or BlackBerry)
      -  Authy
         (`Android <https://play.google.com/store/apps/details?id=com.authy.authy>`__
         or
         `iPhone <https://itunes.apple.com/us/app/authy/id494168017?mt=8>`__)
      -  Authenticator (`Windows
         Phone <https://www.microsoft.com/en-us/store/p/microsoft-authenticator/9nblgggzmcj6>`__)
      -  `FreeOTP <https://play.google.com/store/apps/details?id=org.fedorahosted.freeotp>`__
         (Android)

      In addition, you can use any other mobile authentication
      application, as long as it works with the `Time-Based One-Time
      Password
      Algorithm <http://en.wikipedia.org/wiki/Time-based_One-time_Password_Algorithm>`__
      (TOTP) (`RFC 6238 <http://tools.ietf.org/html/rfc6238>`__).

   -  *Using text messages*
      If you selected **Text Messages (SMS)** as your verification
      method, compete the following steps:

      #. Enter your mobile telephone number. This number must be a US or
         Canada number and must be able to receive SMS messages.
         Standard carrier rates may apply.
      #. Click **Send code**.
      #. You will receive a verification code at the phone number you
         specified. Enter it in the **SMS verification code** field, and
         then click **Verify**.

.. _trusted:

Marking your browser as trusted
-------------------------------

After you enter your verification code, you can optionally mark as
trusted the browser on the device that you used to set up two-step
verification. When you mark the browser as trusted, Acquia stores your
browser information. You can then sign in to the |acquia-product:ui|
from this browser on the same device with just a user name and password
for 30 days. After 30 days, you will need to enter a verification code
once again.

To mark a browser as trusted, complete the following steps:

#. Optionally, enter a name for this browser on this device. If you
   don't provide a custom name, the |acquia-product:ui| uses the name of
   the browser (for example, Firefox or Chrome).

   |Trust a browser|

#. Click **Trust**.

To mark a browser as no longer trusted, complete the following steps:

#. Click your name in the upper right of the |acquia-product:ui|, and
   then click the **Edit profile** link to open your Acquia profile.
#. In your Acquia profile, click the **Credentials** tab.
#. On the Credentials page, in the **Two-Step Verification** section,
   find your browser in the **Trusted browsers** list.
#. Click the **Remove** link for the browser you no longer want to
   trust.

.. _fallback:

Setting up a fallback method
----------------------------

After you set up two-step verification, you should then set up a
fallback method. This is optional, but strongly recommended. If you set
up a mobile authentication application as your primary method of
verification, then SMS text message is your fallback method, and vice
versa.

If you set up a mobile authentication application as your primary method
of verification, complete the following steps:

#. Enter your mobile telephone number. This number must be a US or
   Canada number and must be able to receive SMS messages. Standard
   carrier rates may apply.
#. Click **Set up fallback**.
#. You will receive a verification code at the phone number you
   specified. Enter it in the **SMS verification code** field, and then
   click **Continue**.

Using your fallback method
~~~~~~~~~~~~~~~~~~~~~~~~~~

To use your fallback method, when you are prompted for a verification
code, click the **Having trouble?** link. Acquia then sends a
verification code using your fallback method. Enter this code and click
**Verify**.

.. _recovery:

Recording your recovery codes
-----------------------------

As another form of fallback verification, when you set up two-step
verification, Acquia creates a set of recovery codes that you can use to
gain access to your account when you don't have your phone available.
You should print or write them down and store in a secure place. It is
strongly recommended that you do not store your recovery codes on a
device.

You can view your recovery codes if you are already signed in to the
|acquia-product:ui|, on your **Profile > Credentials** page.

Using a recovery code
~~~~~~~~~~~~~~~~~~~~~

To use a recovery code, complete the following steps:

#. Sign in to the |acquia-product:ui| with your email and Acquia
   password.
#. Click the **Having trouble?** link or **Don't have your code?** link
   when prompted for your verification code.
#. Enter your recovery verification code and click **Recover**.

After you have recorded your recovery codes, click **Finish**.

Modifying two-step verification settings
----------------------------------------

You can modify your two-step verification settings at any time. To do
so:

#. Click your name in the upper right of the |acquia-product:ui|, and
   then click the **Edit profile** link to open your Acquia profile.

   |Editing profile credential settings|

#. In your Acquia profile, click **Credentials**.
#. On the **Credentials** page, in the **Two-Step Verification**
   section, edit the settings you want to change.

You can change your primary and fallback verification methods (mobile
authentication application or SMS text message), phone number, or
trusted browsers. You can also view your recovery codes.

.. _new:

Authorizing a new device
------------------------

If you get a new phone, you can install the mobile authentication
application of your choice on the new phone and then `modify <#edit>`__
your **Profile > Credentials** settings in the |acquia-product:ui| with
a new verification code. That, of course, assumes that you can still
sign in to the |acquia-product:ui| without a verification code, which
you can do if you have marked your browser as trusted and your browser
is still within the 30 days' trusted period. If that is not the case and
you need to enter a verification code to sign into the
|acquia-product:ui|, you can:

-  Use your `fallback method <#fallback>`__.
-  Use a `recovery code <#recovery>`__.

If neither of these methods work or are available to you, click the
**Still having trouble? Contact us** link to obtain a phone number which
you can use to `contact Acquia Support </support#contact>`__.

.. |Setting up two-step verification| image:: https://cdn4.webdamdb.com/1280_kmro78nJa81.png?1526475810
   :width: 750px
   :height: 711px
.. |Trust a browser| image:: https://cdn3.webdamdb.com/1280_YDO2y7KoEaz4.png?1526475579
   :width: 750px
   :height: 452px
.. |Editing profile credential settings| image:: https://cdn2.webdamdb.com/1280_ANJ4181Z1uE8.png?1526476118

