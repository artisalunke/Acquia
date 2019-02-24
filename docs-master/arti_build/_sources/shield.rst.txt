.. include:: /common/global.rst

Acquia Cloud Shield
===================

.. container:: message-status

   Available only to `Acquia Cloud Enterprise </acquia-cloud>`__ subscribers

Using |acquia-product:vpc|, your |acquia-product:ace| applications run in a dedicated, logically isolated section of |acquia-product:ac|, adding more network level security and capabilities to the stack. |acquia-product:vpc| is available as an additional service to |acquia-product:ace| subscriptions.

Benefits of using Acquia Cloud Shield
-------------------------------------

|acquia-product:vpc| gives you the benefits of |acquia-product:ac| platform-as-a-service, combined with extra security benefits and capabilities. |acquia-product:vpc| provides a higher degree of isolation for your |acquia-product:ac| instances in the cloud. With |acquia-product:vpc|, your |acquia-product:ac| instances exist in a dedicated, logically isolated section that is not shared with any other users.

Optionally, you can use |acquia-product:vpc| with a VPN, which provides a secure bidirectional connection between your |acquia-product:ace| applications and your internal IT systems. In this case, instances within the dedicated cloud section can be accessed only by other instances within the same dedicated cloud section, or else over a secure internet gateway (VPN).

.. admonition:: Note for |acquia-product:as| users

  Your search installation can be accessed from your |acquia-product:vpc| applications, but the |acquia-product:as| servers will not be located in your |acquia-product:vpc| dedicated section. Therefore, your search index will not be covered by |acquia-product:vpc|.

|acquia-product:vpc| uses Dead Peer Detection, exchanging UDP packets between VPN peers to ensure that both ends are are available. If no traffic crosses the VPN tunnel in ten seconds, a request is sent. If three successive requests are sent without a response, |acquia-product:vpc| will close the VPN tunnel.

Getting started with Acquia Cloud Shield
----------------------------------------

To use |acquia-product:vpc|, simply purchase |acquia-product:vpc| with your |acquia-product:ace| subscription. Acquia then provisions your servers within your dedicated cloud section.

Getting started with Acquia Cloud Shield with VPN
-------------------------------------------------

To use |acquia-product:vpn|, you must have an |acquia-product:ace| subscription and must have purchased |acquia-product:vpc|. The following are the main steps in setting up |acquia-product:vpn|:

#. You purchase and deploy a VPN device. See `VPN device requirements. <#vpnrqts>`__
#. You provide Acquia with detailed information about your VPN device and your network. See `Network information <#info>`__.
#. Acquia provisions and configures a dedicated cloud section for your applications.
#. Acquia provides you with the IPSec (Internet Protocol Security) /IKE (Internet Key Exchange) information you need to properly configure your VPN.

Network information you provide to Acquia
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Acquia to configure |acquia-product:vpn|, you will need to provide Acquia with the following information:

-  Contact information (such as name, phone, and email) for the members of your internal network team.
-  VPN device details:

   -  VPN device type (vendor and model)
   -  The Gateway IP address of the customer VPN device

   Confirm that your VPN device meets the requirements described in `VPN device requirements <#vpnrqts>`__.
-  Network details, including the following:

   -  A network diagram, showing which systems |acquia-product:vpc| will connect to
   -  Maintenance plan or schedule for these services
   -  CIDR IP blocks
   -  Subnet allocations
   -  A list of networks that need traffic statically routed to them

-  A private, non-routable /16 or /20 private address space for |acquia-product:vpc|.
-  *(Optional)* A name for the Acquia VPN. If you have multiple VPNs, providing a name to Acquia may be useful for later communication.

Contact your Acquia account manager for more information.

VPN device requirements
~~~~~~~~~~~~~~~~~~~~~~~

To connect to |acquia-product:vpn|, your network must use a VPN (a secure Internet gateway) that uses IPsec. Your VPN device must be capable of each of the following:

-  Establish IKE Security Associations using pre-shared keys
-  Establish IPsec Security Associations in Tunnel mode
-  Use the AES 128-bit encryption function
-  Use the SHA-1 hashing function
-  Use Diffie-Hellman Perfect Forward Secrecy in "Group 2" mode
-  Perform packet fragmentation prior to encryption

The following gateway devices are compatible with |acquia-product:vpn|; other devices may work, but are not supported by Acquia:

-  Cisco ASA 5500 Series version 8.2 or greater software
-  Cisco ISR running Cisco IOS 12.4 or greater software
-  Dell SonicWALL Next Generation Firewalls (TZ, NSA, SuperMassive Series) running SonicOS5.8 or greater
-  Juniper J-Series Service Router running JunOS 9.5 or greater software
-  Juniper SRX-Series Services Gateway running JunOS 9.5 or greater software
-  Juniper SSG running ScreenOS 6.1, or 6.2 or greater software
-  Juniper ISG running ScreenOS 6.1, or 6.2 or greater software
-  Microsoft Windows Server 2008 R2 or greater software
-  Yamaha RTX1200 router

Your network's gateway must be properly configured to connect to |acquia-product:vpn|. After your dedicated cloud section is provisioned, Acquia will provide you with the IPSec/IKE information you need to properly configure your VPN.

Changes to IP addresses
-----------------------

If you have an existing application hosted on |acquia-product:ace| and you move it to |acquia-product:vpn|, your IP address will change. This includes any elastic IP addresses (EIPs). IP addresses cannot be moved into or out of a VPC.

As a result, when you set up your application in |acquia-product:vpn|, you need to point the DNS records of your application to the new IP address within the VPC. For more information, see `Pointing DNS records to your public IP addresses </acquia-cloud/manage/domains/dns>`__.
