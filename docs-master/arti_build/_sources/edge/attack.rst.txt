.. include:: /common/global.rst

Defending your website against attacks
======================================

If your |acquia-product:ac|-hosted websites that are protected by |acquia-product:cfp| are under threat of attack or are currently being attacked, you should *immediately* take the following steps for maximum protection of your websites:

#. Sign in to your |acquia-product:cf| web user interface.
#. In the **Overview** section, click the **Quick Actions** select box, and then click `Under Attack Mode <https://support.cloudflare.com/hc/en-us/articles/200170206>`__. This enables additional protections to stop potentially malicious HTTP traffic from being passed to your server.

   |Under Attack Mode|

   .. note::

      Whenever **Under Attack Mode** is enabled, first-time visitors to your website will be briefly served an interstitial page while the additional checks are performed to verify that the traffic is legitimate.

#. Navigate to the **Firewall** section of the |acquia-product:cfp| interface, identify the Web Application Firewall option, and then click **On**.
#. Navigate to your Domain Name Server (DNS) settings in the |acquia-product:cfp| interface, and then configure your DNS settings for maximum protection:

   -  Enable the |acquia-product:cf| security on the web records you use, including SSH. Protocols with security disabled are gray; protocols with security enabled are orange. Enabling these security protocols will disable these services, protecting your servers from additional modes of attack.
   -  Use your origin IP address to perform actions like SSH, as all other IP addresses will be disallowed.
   -  Delete any wildcard records, unless they are required, as they will expose your origin IP address.
   -  Remove any mail records that expose your origin IP address.

#. Do not rate-limit or throttle requests from `Acquia Cloud Edge IP addresses <https://www.cloudflare.com/ips/>`__.
#. `Contact Acquia Support </support#contact>`__, and in the Support ticket that you create, provide detailed information about the attack to help Acquia Support better assist you in determining next steps.

.. |Under Attack Mode| image:: https://cdn3.webdamdb.com/1280_YxMFijHr8Ga0.png?1527610223
   :width: 750px
   :height: 121px
